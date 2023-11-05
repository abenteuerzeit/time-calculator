#!/bin/bash

# A wrapper script for running time_calculator.py with command-line arguments

# Path to the Python script - adjust if it's located elsewhere
SCRIPT="python time_calculator.py"

# Pass all the arguments to the Python script
$SCRIPT "$@"
