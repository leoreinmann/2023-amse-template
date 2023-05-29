#!/bin/bash

# Get the absolute path to the script
script_dir=$(dirname "$(readlink -f "$0")")

# Check if the script is inside the 'project' folder
if [[ $script_dir == */project ]]; then
    # If inside the 'project' folder, move up to the root directory
    project_dir=$(dirname "$script_dir")
    cd "$project_dir"
fi

# Run pulldata.py
python3 data/pulldata.py

# Check if the output file exists
if [ -f data/data.sqlite ]; then
    echo "Output file exists: data/data.sqlite"
else
    echo "Output file is missing!"
    exit 1
fi