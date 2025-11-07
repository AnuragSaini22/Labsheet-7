# Program to create and write text into a file

file = open("example.txt", "w")   # Open file in write mode
file.write("Hello, this is a sample text file.\nWelcome to Python file handling!")
file.close()
print("Text written successfully to example.txt")



# Program to read the entire content of a text file

file = open("example.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()



# Program to read a file line by line

file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()



# Program to count the number of words in a text file

file = open("example.txt", "r")
text = file.read()
words = text.split()
print("Total number of words:", len(words))
file.close()



# Program to count the number of lines and characters in a file

file = open("example.txt", "r")
lines = file.readlines()
num_lines = len(lines)
num_chars = sum(len(line) for line in lines)
print("Number of lines:", num_lines)
print("Number of characters:", num_chars)
file.close()



# Program to display only even-numbered lines from a file

file = open("example.txt", "r")
lines = file.readlines()

print("Even-numbered lines:")
for i in range(1, len(lines), 2):   # Index starts from 0
    print(lines[i].strip())

file.close()



# Program to write multiple lines of input from the user into a file

file = open("user_input.txt", "w")

print("Enter multiple lines (type 'exit' to stop):")
while True:
    line = input()
    if line.lower() == 'exit':
        break
    file.write(line + "\n")

file.close()
print("User input saved successfully to user_input.txt")



# Program to append new content to an existing file

file = open("example.txt", "a")  # Open in append mode
file.write("\nThis is new content appended to the file.")
file.close()
print("Content appended successfully!")



# Program to copy the contents of one file into another

source = open("example.txt", "r")
destination = open("copy_example.txt", "w")

for line in source:
    destination.write(line)

source.close()
destination.close()
print("File copied successfully to copy_example.txt")



# Program to read a file and convert its content to uppercase

file = open("example.txt", "r")
content = file.read()
print("File content in uppercase:\n", content.upper())
file.close()


