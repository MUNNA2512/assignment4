def write_and_append():
    # Get user input
    user_input = input("Enter some text to write to the file: ")
    
    # Write to file
    try:
        with open('output.txt', 'w') as file:
            file.write(user_input + "\n")
            print("Text written to file successfully!")
        
        # Append more data
        additional_data = input("Enter additional text to append: ")
        with open('output.txt', 'a') as file:
            file.write(additional_data + "\n")
            print("Additional text appended successfully!")
        
        # Read and display final content
        print("\nFinal content of the file:")
        with open('output.txt', 'r') as file:
            print(file.read())
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    write_and_append()