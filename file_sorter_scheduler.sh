#!/bin/bash

# Assume the script is run in the target folder
PYTHON_SCRIPT="file_sorter.py"

# Check if the Python script exists in the current directory
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "Error: Python script not found in the current folder ($PWD)."
    exit 1
fi

# Run the Python script
python3 "$PYTHON_SCRIPT"

# Add a cron job to run this script weekly
(crontab -l 2>/dev/null; echo "@weekly bash $PWD/file_sorter_scheduler.sh") | crontab -

echo "File sorter scheduled to run weekly in $PWD."
