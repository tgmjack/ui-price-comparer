from cx_Freeze import setup, Executable
  
setup(
    name = "big ui system" ,
    version = "0.1" ,
    description = "a ui to tie together some web scrappers " ,
    executables = [Executable("close test.py")]
      )
