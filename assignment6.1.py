def convert_to_uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                uppercase_line = line.upper()
                print(uppercase_line, end='')

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    convert_to_uppercase(file_name)
