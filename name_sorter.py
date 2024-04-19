def sort_names(names):
    # Splits each name into parts and sorts first by last name, then by up to 3 given names
    valid_names = []
    for name in names:
        parts = name.split(" ")
        if 1 < len(parts) <= 4:  #  For names to be valid they must have at least a surname, 1 given name and at most 3 given names plus their surname
            valid_names.append(name)
        else:
            print(f"Error: Invalid name on the list - '{name}'. A name must have 1 to 3 given names and a surname.")
    return sorted(valid_names, key=lambda name: (name.split(" ")[-1], name.split(" ")))

def read_names_from_file(filename):
    # Reads the names from the file and returns them as a list
    try:
        with open(filename, 'r') as file:
            return file.read().strip().split('\n')
    except FileNotFoundError:
        print(f"Error: An error occurred while accessing the file {filename}: {e}")
        return []

def write_names_to_file(filename, names):
    # Writes the sorted names to the file
    try:
        with open(filename, 'w') as file:
            for name in names:
                file.write(f"{name}\n")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main(input_file):
    # Read names from the input file
    names = read_names_from_file(input_file)
    
    # Proceed only if names were successfully read
    if names:
        # Sort the names with validation for given names count
        sorted_names = sort_names(names)
        
        # Display the sorted names
        for name in sorted_names:
            print(name)
        
        # Write the sorted names to a new file
        write_names_to_file('sorted-names-list.txt', sorted_names)
    else:
        print("No names to sort due to earlier error.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        main(input_file)
    else:
        print("Usage: name-sorter <path-to-unsorted-names-list.txt>")