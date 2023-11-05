# Time Calculator

This is the boilerplate for the Time Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

The Time Calculator is a Python-based command-line utility that allows users to add time durations to a given start time. It can handle different time formats, calculate the resulting time, and account for the day of the week.

## Features

- Add time durations to a specified start time.
- Support for 12-hour time format (with AM/PM).
- Weekday calculation to show the resulting day of the week.
- Interactive mode for ease of use.
- Error handling for invalid time formats.

## Prerequisites

- Python 3.x
- Bash (for the wrapper scripts)

## Files

- `time_calculator.py`: The main Python module containing the logic for adding time durations.
- `example.sh`: A Bash script that showcases various examples of how to use `time_calculator.py`.
- `add_time.sh`: A simple wrapper script for `time_calculator.py` that passes along command-line arguments.
- `test_time_calculator.py`: Unit tests for verifying the correctness of `time_calculator.py`.

## Usage

### Python Module

Run the Python script directly with the desired arguments:

```bash
python time_calculator.py -s '3:00 PM' -d '2:12' -w 'Monday'
```

### Bash Wrapper Scripts

#### `example.sh`

Execute this script to see examples of common usage scenarios:

```bash
./example.sh
```

#### `add_time.sh`

Use this wrapper script to pass command-line arguments directly to `time_calculator.py`:

```bash
./add_time.sh -s '3:00 PM' -d '2:12' -w 'Monday'
```

### Options

- `-i`, `--interactive`: Run in interactive mode.
- `-h`, `--help`: Show help message and usage information.
- `-s`, `--start`: Specify the start time in the format 'hh:mm AM/PM'.
- `-d`, `--duration`: Specify the duration to add in the format 'hh:mm'.
- `-w`, `--weekday`: Specify the starting weekday (e.g., 'Monday').
- `-c`, `--current`: Use the current time as the start time.

## Development and Testing

To contribute or run tests, clone the repository, and execute the test module:

```bash
python -m unittest test_time_calculator
```

## License

This project is licensed under the European Union Public License (EUPL). The full text of the license can be found in the LICENSE file included in this repository.

The EUPL is a copyleft license that covers the use and distribution of the software within the European Union. It is compatible with several other open-source licenses, allowing for mixing and redistribution under different terms.

For more details on the EUPL, visit the official EUPL website.