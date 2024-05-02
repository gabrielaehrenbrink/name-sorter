class FileReader:
    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError as e:
            print(f"Error: File not found {filename}: {e}")
            return []

class FileWriter:
    def write_to_file(self, filename, names):
        try:
            with open(filename, 'w') as file:
                for name in names:
                    file.write(f"{name}\n")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

class NameValidator:
    # Validates that each name has at least 1 surname and up to 3 given names
    def validate(self, names):
        valid_names = []
        for name in names:
            parts = name.split(" ")
            if 1 < len(parts) <= 4:
                valid_names.append(name)
            else:
                print(f"Error: Invalid name on the list - '{name}'.")
        return valid_names

class NameSorter:
    # Sorts names first by surname and then by given names
    def sort(self, names):
        return sorted(names, key=lambda name: (name.split(" ")[-1], name.split(" ")))

def process_names(input_file, file_reader, name_validator, name_sorter, file_writer):
    # Process names through the steps of reading, validating, sorting, and writing
    names = file_reader.read_from_file(input_file)
    if names:
        valid_names = name_validator.validate(names)
        sorted_names = name_sorter.sort(valid_names)
        file_writer.write_to_file('sorted-names-list.txt', sorted_names)
        for name in sorted_names:
            print(name)
    else:
        print("No names to process.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_names(sys.argv[1], FileReader(), NameValidator(), NameSorter(), FileWriter())
    else:
        print("Usage: name-sorter <path-to-unsorted-names-list.txt>")

