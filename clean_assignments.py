import os
import re

def clean_assignment_file(input_file, output_file):
    """Clean up an assignment file extracted from PDF"""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove the header line if it's just "Exp X" or similar
    cleaned_lines = []
    for line in lines:
        stripped = line.rstrip()
        # Skip header lines like "Exp 1", "exp 2", etc. if they're alone on a line
        if re.match(r'^[Ee]xp\s*\d+\s*$', stripped):
            continue
        # Skip lines that are just form feed characters or excessive whitespace
        if stripped == '' or stripped == '\f':
            # Keep empty lines for readability but limit consecutive empty lines
            if cleaned_lines and cleaned_lines[-1] == '':
                continue
            cleaned_lines.append('')
            continue
        # Remove leading/trailing whitespace
        cleaned_lines.append(stripped.rstrip())
    
    # Remove trailing empty lines
    while cleaned_lines and cleaned_lines[-1] == '':
        cleaned_lines.pop()
    
    # Write cleaned content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_lines))
    
    print(f'Cleaned {input_file} -> {output_file} ({len(cleaned_lines)} lines)')

# Process assignment files
assignments_dir = '/c/Users/ishan/Downloads/python_assignments'
for i in range(1, 4):
    input_file = f'{assignments_dir}/assignment_{i}.py'
    if os.path.exists(input_file):
        # Create a backup
        backup_file = f'{input_file}.bak'
        os.rename(input_file, backup_file)
        # Clean the file
        clean_assignment_file(backup_file, input_file)
        # Remove backup
        os.remove(backup_file)
