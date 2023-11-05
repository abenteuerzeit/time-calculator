#!/bin/bash

# A script to run various parts of the Time Calculator application or its tests

echo "Select the script to run:"
echo "1 - Run main.py (default execution)"
echo "2 - Run add_time.sh wrapper script"
echo "3 - Run example.sh to see usage examples"
read -p "Enter your choice (1/2/3): " choice

case $choice in
  1)
    python main.py
    ;;
  2)
    ./add_time.sh
    ;;
  3)
    ./example.sh
    ;;
  *)
    echo "Invalid option selected. Exiting."
    exit 1
    ;;
esac
