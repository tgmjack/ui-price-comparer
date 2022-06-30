from cx_Freeze import setup, Executable
  
setup(name = "arval full auto" ,
      version = "1.1" ,
      description = "arval full auto, now takes input config.txt " ,
      executables = [Executable("main.py")])
