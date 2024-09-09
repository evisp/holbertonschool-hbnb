#!/bin/bash

# Navigate to the root of the project
cd "$(dirname "$0")"

# Remove existing docs
rm -rf docs/*

# Create the docs directory if it doesn't exist
mkdir -p docs

# Find all Python files and generate HTML documentation
for file in $(find . -name "*.py"); do
    module_path=$(echo "${file}" | sed -e 's/.\///' -e 's/\.py$//g' -e 's/\//./g')
    pydoc -w ${module_path}
done

# Move all generated HTML files to the docs/ directory
mv *.html docs/
