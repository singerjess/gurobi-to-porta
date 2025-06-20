import re

import re

def replace_strings_at_end(input_file, output_file, replacements):
    """
    Replace occurrences of strings in the replacements dictionary only when they appear at the end of a word.

    :param input_file: Path to the input file.
    :param output_file: Path to the output file.
    :param replacements: Dictionary mapping strings to their replacements.
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Replace occurrences of strings with the specified conditions
    processed_lines = []
    for line in lines:
        for key, value in replacements.items():
            # Match the key only if it is followed by +, -, or end of word
            line = re.sub(rf'{re.escape(key)}(?=\+|-|\s|$)', value, line)
        processed_lines.append(line)

    # Write the updated content to the output file
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)


def process_mappings(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract the variable mapping from the last line
    variable_mapping_line = lines[-1].strip()
    variable_mapping = {}
    for mapping in re.findall(r"x(\d+):\s*([\w\[\],]+)", variable_mapping_line):
        variable_mapping[f"x{mapping[0]}"] = mapping[1]
    return variable_mapping

# Example usage
input_file = './examples/3_sensores_prueba.poi.ieq'
output_file = './processed/processed_3_sensores_prueba.poi.ieq'
replacements = process_mappings(input_file)

replace_strings_at_end(input_file, output_file, replacements)