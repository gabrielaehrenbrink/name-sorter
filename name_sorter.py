class NameValidator:
    @staticmethod
    def validate(names):
        # Validate names to ensure each consists of 2 to 4 parts (1 surname and up to 3 given names)
        valid_names = []
        for name in names:
            parts = name.split(" ")
            if 1 < len(parts) <= 4:
                valid_names.append(name)
            else:
                print(f"Error: Invalid name on the list - '{name}'.")
        return valid_names

class NameSorter:
    @staticmethod
    def sort(names):
        # Sort names by surname and then by given names
        return sorted(names, key=lambda name: (name.split(" ")[-1], name.split(" ")))

class FileManager:
    @staticmethod
    def read_from_file(filename):
        # Read names from a file and return them as a list
        try:
            with open(filename, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError as e:
            print(f"Error: File not found {filename}: {e}")
            return []

    @staticmethod
    def write_to_file(filename, names):
        # Write names to a file, each name on a new line
        try:
            with open(filename, 'w') as file:
                for name in names:
                    file.write(f"{name}\n")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

def process_names(input_file):
    # Main processing function to handle the flow of reading, validating, sorting, and writing names
    names = FileManager.read_from_file(input_file)
    if names:
        valid_names = NameValidator.validate(names)
        sorted_names = NameSorter.sort(valid_names)
        FileManager.write_to_file('sorted-names-list.txt', sorted_names)
        for name in sorted_names:
            print(name)
    else:
        print("No names to process.")

if __name__ == "__main__":
    # Entry point of the script, handling command line arguments
    import sys
    if len(sys.argv) > 1:
        process_names(sys.argv[1])
    else:
        print("Usage: name-sorter <path-to-unsorted-names-list.txt>")