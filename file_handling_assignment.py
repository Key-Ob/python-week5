filename = "my_file.txt"

#Writing the initial file
def write_file(file_path):
    try:
        with open(file_path, "w") as file:
            file.writelines([
                "1. Provide a file",
                "\n2. Read the file",
                "\n3. Use the file"
            ])

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while writing to the file: {e}")

#Appending the file
def append_file(file_path):
    try:
        with open(file_path,"a") as file:
            file.writelines([
                "\n4. Edit everything",
                "\n5. Cook some more",
                "\n6. On the grind"
            ])
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")

#Reading the file
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content) 

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    finally:
        print(f"Finished attempting to read the file.")

#Execution
write_file(filename)
append_file(filename)
read_file(filename)