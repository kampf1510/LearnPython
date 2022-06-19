# Python Modules

# A module is a package of python code (often referred to as a code-library) which is installed via pip in the terminal.
# you must first import the module then can call to it, imports should always be at the top of code.

# To start, practice importing a built-in python module such as os, dir, platform, sys etc. - in this case we'll
# import the sys (system with the platform or OS method), then print the result, this should print your OS.

import sys

print(sys.platform)

# To install a non-builtin module use pip in a terminal/cmd - pip is installed with Python to manage python packages.
# the general format to install a package is pip install Package.

# Importing from another python file is the most common use of modules, to import a block of code from another file
# simply specify the file within the project directory and the specific code you'd like to import. In this case we'll
# import a function from the Functions_and_Methods file, pass it some parameters and run it in this file.

from Functions_and_Methods import function_test

print(function_test(3))

# Importing code from another file is a vital concept and will play a critical role in any project.

# Import the function named fun from the Functions_and_Methods python file then pass it parameters if required and
# return the value of the imported function.


# END of Python Modules
