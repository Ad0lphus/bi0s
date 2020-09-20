from cx_Freeze import setup, Executable
import adminsignup,admnchoice,createsqltable,customer1,deleteitem,frontwindow,login,payment,searchitem,searchorders,shopping,updateitem,usersearch
base = None    

executables = [Executable("frontwindow.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
