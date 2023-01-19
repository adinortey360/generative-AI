import os

directory_path = 'TRN'
combined_file = 'combined_files.txt'

with open(combined_file, 'w') as out_file:
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".trn"):
            try:
                with open(os.path.join(directory_path, file_name), 'r', encoding='latin-1') as in_file:
                    out_file.write(in_file.read())
            except UnicodeDecodeError:
                continue

with open(combined_file, 'r') as file:
    lines = file.readlines()

with open(combined_file, 'w') as file:
    for line in lines:
        file.write(line[19:])