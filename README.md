# CONSOLE CALCULATOR VERSION 0.0.1

Author: J.M.B. Downing

Modified: 2019-02-24

## About Console Calculator

Console calculator performs basic arithmatic operations on integers.  It runs from a terminal command line and takes text input.  It is written in Python 3 and has been tested in Linux Mint 18.1.

## Installation Instructions

Console calculator is provided in two ways:

1. A python script file called `ConsoleCalc.py`

2. A stand-alone executable called `ConsoleCalc` that was created with Pyinstaller 3.4 for Python 3.  The `ConsoleCalc` executable is located in the `dist` directory.

### Running the Python Script

To run Console Calculator from the python script:

1. Ensure that a Python 3 interpreter is installed on your system (a Python 3 interpreter is installed as standard on most modern Linux systems).
2. Place the `ConsoleCalc.py` script file in the directory from which you want to run it.
3. Run the script with the following command: `python3 ConsoleCalc.py`
4. Follow the on-screen instructions.

### Running the Stand-alone Executable

The stand-alone executable has been created with Pyinstaller 3.4 on a Linux Mint 18.1 system.  From the Pyinstaller manual:

> PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! – and puts them with your script in a single folder, or optionally in a single executable file.
> https://pyinstaller.readthedocs.io/en/v3.4/operating-mode.html

As such the stand-alone executable should run on most Debian-based linux systems even if they do not have Python 3 installed (it may also work on many other linux distributions but will not work on Windows or MacOS).

To run the stand-alone executable:

1. Copy the `ConsoleCalc` executable from the `dist` directory to the directory from which you want to run it.
2. Ensure you have execute permission on the executable.  If not use `chmod` to change the permissions as follows: `chmod u+x ConsoleCalc`.
3. Run the executable as follows `./ConsoleCalc`.
4. Follow the on-screen instructions.

## Using Console Calculator

Console calculator performs basic arithmatical operations on integers.

Once Console Calculator has been opened the instructions will be printed and a prompt will appear.  At the prompt enter the first integer, a space, the desired mathematical operation, a second space, and then the second integer.  Finally hit the ENTER key to perform the calculation.  Allowed mathematical operations are addition (+), subtraction (-), multiplication (*), and division (/) Output will be a single integer in the case of addition, subtraction, or multiplication and will be a lowest common divisor fraction in the case of division.

Input format:
* Addition: a + b
* Subtraction: a - b
* Multiplication: a * b
* Division: a / b

The instructions can be re-printed simply by hitting ENTER at the prompt.
