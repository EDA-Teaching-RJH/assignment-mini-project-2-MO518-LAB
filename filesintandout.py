filename = 'complete_example.txt'

# Write to the file
with open(filename, 'w') as file:
    file.write("Come to the next lecture. \n")
    file.write("EENG03130 is a Great Module.")

# Read from the file
with open(filename, 'r') as file:
    content = file.read()
    print("Contents:")
    print(content)