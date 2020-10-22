extern crate pyo3;

use pyo3::prelude::*;

#[allow(unused_mut)]
#[allow(unused_variables)]
#[allow(dead_code)]
#[pymodule]
fn skydive(_py: Python, _m: &PyModule) -> PyResult<()> {
    #[pyfn(_m, "process_data")]
    fn process_data(
        _py: Python,
        dropheight: f32,
        toptemp: f32,
        bottomtemp: f32,
        gravity: f32,
        cabefore: f32,
        caafter: f32,
        divercoef: f32,
        chutecoef: f32,
        timestep: f32,
        mass: f32,
        humidity: f32,
        chuteopen: f32,
        chutetimeoralt: &str,
    ) -> PyResult<Vec<Vec<f32>>> {
        let mut time_finished = f32::MAX;
        let mut current_distance: f32 = 0.0;
        let mut current_velocity: f32 = 0.0;
        let mut current_acceleration: f32 = 0.0;
        let mut current_time: f32 = 0.0;
        let mut current_pressure: f32 = 0.0;
        let mut current_density: f32 = 0.0;
        let mut current_altitude: f32 = 0.0;
        let mut current_temp: f32 = 0.0;
        let mut current_vapourpressure: f32 = 0.0;
        let mut current_drypressure: f32 = 0.0;
        let mut time: Vec<f32> = vec![];
        let mut velocity: Vec<f32> = vec![];
        let mut acceleration: Vec<f32> = vec![];
        let mut distance: Vec<f32> = vec![];
        let mut pressure: Vec<f32> = vec![];
        let mut density: Vec<f32> = vec![];
        let mut temp: Vec<f32> = vec![];
        let mut altitude: Vec<f32> = vec![];
        let mut vapourpressure: Vec<f32> = vec![];
        let mut drypressure: Vec<f32> = vec![];
        while current_time + 10.0 < time_finished {
            current_altitude = dropheight - current_distance;
            altitude.push(current_altitude);
            current_temp = bottomtemp + (current_altitude/dropheight) * (toptemp - bottomtemp);
            temp.push(current_temp);
            current_pressure = 101325.0*f32::exp(-gravity*0.0289644*((current_altitude)/(8.31432*current_temp)));
            pressure.push(current_pressure);
            current_vapourpressure = current_pressure * humidity;
            vapourpressure.push(current_vapourpressure);
            current_drypressure = current_pressure - current_vapourpressure;
            drypressure.push(current_drypressure);
            current_density = (current_drypressure / (287.058 * current_temp))
                + (current_vapourpressure / (461.495 * current_temp));
            density.push(current_density);
            current_acceleration = get_acceleration(
                gravity,
                current_density,
                current_velocity,
                cabefore,
                caafter,
                divercoef,
                chutecoef,
                mass,
                chuteopen,
                chutetimeoralt,
                current_time,
                current_altitude,
            );
            acceleration.push(current_acceleration);
            current_time = current_time + timestep;
            time.push(current_time);
            if current_altitude > 0.0 {
                current_velocity = current_velocity + (current_acceleration * timestep);
            } else {
                current_velocity = 0.0;
            }
            velocity.push(current_velocity);
            current_distance = current_distance + (current_velocity * timestep);
            distance.push(current_distance);
            if current_velocity == 0.0 {
                time_finished = current_time;
            }
        }
        let out: Vec<Vec<f32>> = vec![
            time,
            velocity,
            acceleration,
            distance,
            pressure,
            density,
            temp,
            altitude,
            vapourpressure,
            drypressure,
        ];
        Ok(out)
    }
    Ok(())
}

fn get_acceleration(
    gravity: f32,
    density: f32,
    velocity: f32,
    cabefore: f32,
    caafter: f32,
    divercoef: f32,
    chutecoef: f32,
    mass: f32,
    chuteopen: f32,
    chutetimeoralt: &str,
    time: f32,
    altitude: f32,
) -> f32 {
    if altitude > 0.0 {
        let coef: f32;
        let weight = mass * gravity;
        let coef: f32;
        let area: f32;
        match chutetimeoralt {
            "time" => {
                if chuteopen < time {
                    coef = chutecoef;
                    area = caafter;
                } else {
                    coef = divercoef;
                    area = cabefore;
                }
            }
            _ => {
                if chuteopen > altitude {
                    coef = chutecoef;
                    area = caafter;
                } else {
                    coef = divercoef;
                    area = cabefore;
                }
            }
        }
        return (weight - (0.5 * coef * density * velocity.powi(2) * area)) / mass;
    } else {
        return 0.0;
    }
}

// dropheight, toptemp, bottomtemp, gravity, cabefore, caafter, divercoef, chutecoef, timestep, mass, humidity, chuteopen, chutetimeoralt, x, y
