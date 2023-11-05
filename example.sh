#!/bin/bash

# Function to create separators with repeated characters
separator() {
    printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' "$1"
}

# Function to print colored text
print_color() {
    local text="$1"
    local color="$2"
    local reset_color="\e[0m"
    printf "${color}${text}${reset_color}\n"
}

# Function to execute the Python script and color the output
execute_script() {
    local args=("$@") # Store all arguments in an array
    local cmd="${args[0]}"
    local params=("${args[@]:1}") # Get all parameters excluding the first element (script name)
    
    # Construct the command string with properly quoted arguments
    local full_cmd="$cmd"
    for param in "${params[@]}"; do
        if [[ $param == *" "* ]]; then
            full_cmd+=" \"$param\"" # Add double quotes around parameters with spaces
        else
            full_cmd+=" $param"
        fi
    done
    
    # Execute the command and capture the output and exit status
    local output
    output=$(eval $full_cmd 2>&1) # Use eval to correctly handle spaces within quotes
    local status=$?
    
    if [ $status -ne 0 ]; then
        # If the command failed, print the output in red
        print_color "Error: $output" "\e[1;31m"  # Red color for error
    else
        # If the command succeeded, just print the output
        echo "$output"
    fi
}

# Example usages of time_calculator.py
SCRIPT="python time_calculator.py"

# Usage 1: Help
print_color "$(separator '-')" "\e[1;36m"  # Cyan separator
print_color "Example 1: Help" "\e[1;34m"  # Blue text for header
print_color "$(separator '-')" "\e[1;36m"
execute_script "$SCRIPT" "-h"

# Usage 2: Start and Duration
print_color "$(separator '-')" "\e[1;36m"
print_color "Example 2: Start and Duration" "\e[1;34m"
print_color "$(separator '-')" "\e[1;36m"
execute_script "$SCRIPT" "-s" "4:15 PM" "-d" "2:45" "-w" "Monday"

# Usage 3: Using Current Time
print_color "$(separator '-' 40)" "\e[1;36m"
print_color "Example 3: Using Current Time" "\e[1;34m"
print_color "$(separator '-' 40)" "\e[1;36m"
current_time=$(date +"%I:%M %p")
print_color "Current time is $current_time" "\e[1;32m"
execute_script "$SCRIPT -c -d '00:30'"

# Usage 4: Incorrect Input
print_color "$(separator '-')" "\e[1;36m"
print_color "Example 4: Incorrect Input" "\e[1;34m"
print_color "$(separator '-')" "\e[1;36m"
execute_script "$SCRIPT" "-s" "24:60 AM" "-d" "2:30"

# Usage 5: Start and Duration (with hardcoded values)
print_color "$(separator '-')" "\e[1;36m"
print_color "Example 5: Start and Duration (with hardcoded values)" "\e[1;34m"
print_color "$(separator '-')" "\e[1;36m"
execute_script "$SCRIPT" "-s" "2:45 AM" "-d" "1:15" "-w" "Tuesday"

# Add more examples if needed, following the same pattern...

# Separator at the end
print_color "$(separator '-')" "\e[1;36m"
