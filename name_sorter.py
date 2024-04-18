def sort_names(names):
    # Split each name into parts and sort by last name, then by given names
    return sorted(names, key=lambda name: (name.split(" ")[-1], name.split(" ")))

def read_names_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip().split('\n')

def write_names_to_file(filename, names):
    with open(filename, 'w') as file:
        for name in names:
            file.write(f"{name}\n")

def main(input_file):
    # Read names from the input file
    names = read_names_from_file(input_file)
    
    # Sort the names
    sorted_names = sort_names(names)
    
    # Display the sorted names
    for name in sorted_names:
        print(name)
    
    # Write the sorted names to a new file
    write_names_to_file('sorted-names-list.txt', sorted_names)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        main(input_file)
    else:
        print("Usage: name-sorter <path-to-unsorted-names-list.txt>")