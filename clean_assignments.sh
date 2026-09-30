#!/bin/bash
# Clean assignment files in the assignments directory

for file in assignments/assignment_*.py; do
    if [ -f "$file" ]; then
        echo "Cleaning $file"
        # Remove form feed characters, remove the header line (Exp X or exp X), and clean up extra blank lines
        sed 's/\f//g' "$file" | \
        sed '/^[[:space:]]*[Ee]xp[[:space:]]*[0-9][[:space:]]*$/d' | \
        sed '/^$/N;/^\n$/D' | \
        sed 's/^[[:space:]]*//;s/[[:space:]]*$//' > "${file}.tmp" && mv "${file}.tmp" "$file"
    fi
done
