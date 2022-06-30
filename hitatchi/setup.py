from cx_Freeze import setup, Executable
  
setup(name = "hitatchi  getter" ,
      version = "0.3" ,
      description = "automates getting prices for 1 car from hitatchi " ,
      executables = [Executable("main.py")])
