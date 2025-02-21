import random
import pandas as pd
import os

def load_ssa_data(data_dir, filenames):
    name_data = {}
    if isinstance(filenames, str):
        filenames = [filenames]
    for filename in filenames:
        filepath = os.path.join(data_dir, filename)  # Construct full file path
        with open(filepath, 'r') as file:
            for line in file:
                name, gender, count = line.strip().split(',')
                if gender not in name_data:
                    name_data[gender] = []
                name_data[gender].append((name, int(count)))
    return name_data

def get_names_by_gender(name_data, gender):
    if gender in name_data:
        return [name for name, count in name_data[gender]]
    else:
        return []

# Welcome page
print('Welcome to the Baby Name generator!')

# user input
gender = input('Enter the desired gender (male/female): ').strip().lower()

# Load SSA data
data_directory = "."
filenames = ["yob2023.txt"]

name_data = load_ssa_data(data_directory, filenames)

if name_data is not None:
    female_names = get_names_by_gender(name_data, "F")
    male_names = get_names_by_gender(name_data, "M")

    def generate_name(gender):
        if gender == 'male':
            first_name = random.choice(male_names)
        elif gender == 'female':
            first_name = random.choice(female_names)
        else:
            first_name = random.choice(male_names + female_names)
        
       
        new_name = f"{first_name}"
        return new_name

    new_name = generate_name(gender)
    print(f"Generated Baby Name: {new_name}")

else:
    print("Could not load or process the data. Check the file and directory.")


