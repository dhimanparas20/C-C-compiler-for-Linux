# Compile and Run Script

This script simplifies the process of compiling and running C/C++/java code, saving you time and effort. Provide a C/C++ source code file, and the script will handle the compilation and execution.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Ensure you have Python 3.x installed on your system. If not, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/dhimanparas20/compileNRun.git
   cd compileNRun
   ```

3. Run the requirements.sh script to install gcc and g++ compilers:

  ```bash
  chmod +x requirements.sh
  ./requirements.sh
  ```

## Usage

1. Run the run.py script and provide the required arguments to compile and run your C/C++ code.

  ```bash
  runf source_code_file.cpp
  ```
Replace source_code_file.cpp with the name of your C++ source code file.
NOTE: The source_code_file.cpp file and run.py should be in same directory.


## Examples

1. To compile and run the test.cpp file provided in this repository:

  ```bash
  python3 run.py -f test.cpp
  ```
The script will compile and execute the code, displaying the output in the terminal.

2. To compile and run the test.c file provided in this repository:

  ```bash
  python3 run.py -f test.c
  ```
The script will compile and execute the code, displaying the output in the terminal.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please [create an issue](https://github.com/dhimanparas20/compileNRun/issues) or submit a pull request.


