def read_file():
    try:
        with open('sample.txt', 'r') as file:
            print("File content:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    read_file()