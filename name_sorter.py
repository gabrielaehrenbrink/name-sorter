def sort_names(names):
    # Split each name into parts and sort by last name, then by given names
    # Added validation for the number of given names
    valid_names = []
    for name in names:
        parts = name.split(" ")
        if 1 < len(parts) <= 4:  # Ensure there's at least 1 given name and at most 3 given names plus a surname
            valid_names.append(name)
        else:
            print(f"Error: Invalid name on the list - '{name}'. A name must have 1 to 3 given names and a surname.")
    return sorted(valid_names, key=lambda name: (name.split(" ")[-1], name.split(" ")))

def read_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip().split('\n')
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []

def write_names_to_file(filename, names):
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