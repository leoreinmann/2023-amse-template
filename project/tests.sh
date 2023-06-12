#!/bin/bash

# Get the absolute path to the script
script_dir=$(dirname "$(readlink -f "$0")")

# Check if the script is inside the 'project' folder
if [[ $script_dir == */project ]]; then
    # If inside the 'project' folder, move up to the root directory
    project_dir=$(dirname "$script_dir")
    cd "$project_dir"
fi

# Run automated_pipeline.py
python3 data/automated_pipeline.py

# Check if the output file exists
if [ -f data/data.sqlite ]; then
    echo "Output file exists: data/data.sqlite"
else
    echo "Output file is missing!"
    exit 1
fi

# Perform additional tests

# Test if the 'bikes' table exists in the database
python3 -c "
import sqlite3

# Connect to the database
conn = sqlite3.connect('data/data.sqlite')
c = conn.cursor()

# Check if the 'bikes' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'bikes\'')
table_exists = c.fetchone()

if table_exists:
    print('\'bikes\' table exists in the database')
else:
    print('\'bikes\' table does not exist in the database')

conn.close()
"

# Test if the 'air' table exists in the database
python3 -c "
import sqlite3

# Connect to the database
conn = sqlite3.connect('data/data.sqlite')
c = conn.cursor()

# Check if the 'air' table exists
c.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'air\'')
table_exists = c.fetchone()

if table_exists:
    print('\'air\' table exists in the database')
else:
    print('\'air\' table does not exist in the database')

conn.close()
"

# Test if the 'bikes' table has data
python3 -c "
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/data.sqlite')

# Read the 'bikes' table into a DataFrame
df_bikes = pd.read_sql_query('SELECT * FROM bikes', conn)

if not df_bikes.empty:
    print('\'bikes\' table has data')
else:
    print('\'bikes\' table is empty')

conn.close()
"

# Test if the 'air' table has data
python3 -c "
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/data.sqlite')

# Read the 'air' table into a DataFrame
df_air = pd.read_sql_query('SELECT * FROM air', conn)

if not df_air.empty:
    print('\'air\' table has data')
else:
    print('\'air\' table is empty')

conn.close()
"
