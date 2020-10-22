from cx_Freeze import setup, Executable

setup(name="Skydiver Sim",
      version="0.1",      description="",
      executables=[Executable("skydiver_sim.py", base = "Win32GUI")])
