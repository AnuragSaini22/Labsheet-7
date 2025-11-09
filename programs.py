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


# Program to search for a particular word in a file

word_to_search = input("Enter the word to search: ")
found = False

with open("example.txt", "r") as file:
    for line in file:
        if word_to_search in line:
            found = True
            break

if found:
    print(f"The word '{word_to_search}' was found in the file.")
else:
    print(f"The word '{word_to_search}' was NOT found in the file.")



# Program to count the occurrence of a specific word in a file

word_to_count = input("Enter the word to count: ")

with open("example.txt", "r") as file:
    text = file.read()
    words = text.split()
    count = words.count(word_to_count)

print(f"The word '{word_to_count}' occurs {count} times in the file.")



# Program to read numbers from a file and display their sum and average

with open("numbers.txt", "r") as file:
    numbers = file.read().split()

numbers = [int(num) for num in numbers]
total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum =", total)
print("Average =", average)



# Program to display the longest line in a file

with open("example.txt", "r") as file:
    lines = file.readlines()

longest_line = max(lines, key=len)
print("The longest line is:\n", longest_line.strip())



# Program to replace a word in a file with another word

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

with open("example.txt", "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open("example.txt", "w") as file:
    file.write(text)

print(f"All occurrences of '{old_word}' have been replaced with '{new_word}'.")



# Program to display the first and last lines of a file

with open("example.txt", "r") as file:
    lines = file.readlines()

if len(lines) >= 1:
    print("First line:", lines[0].strip())
    print("Last line:", lines[-1].strip())
else:
    print("The file is empty.")



# Program to remove blank lines from a file

with open("example.txt", "r") as infile, open("no_blank.txt", "w") as outfile:
    for line in infile:
        if line.strip():   # Only write non-empty lines
            outfile.write(line)

print("Blank lines removed successfully! Saved in no_blank.txt")



# Program to read a file and store only unique words into another file

with open("example.txt", "r") as infile:
    words = infile.read().split()
unique_words = set(words)

with open("unique_words.txt", "w") as outfile:
    for word in unique_words:
        outfile.write(word + "\n")

print("Unique words saved in unique_words.txt")



# Program to sort all words in a file alphabetically and save to a new file

with open("example.txt", "r") as infile:
    words = infile.read().split()

words.sort()

with open("sorted_words.txt", "w") as outfile:
    for word in words:
        outfile.write(word + "\n")

print("Words sorted alphabetically and saved in sorted_words.txt")



# Program to merge two text files into a third file

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
    f3.write(f1.read() + "\n" + f2.read())

print("Files merged successfully into merged.txt")



# Program to create and write data into a CSV file

import csv

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Course", "Marks"])
    writer.writerow(["Anita", "BCA", 85])
    writer.writerow(["Rahul", "MCA", 90])
    writer.writerow(["Neha", "B.Tech", 88])

print("Data written successfully to students.csv")



# Program to read data from a CSV file and display it

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



# Program to read a CSV file and calculate average of numeric columns

import csv

total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["Marks"])
        count += 1

average = total / count
print("Average Marks:", average)



# Program to count number of rows and columns in a CSV file

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

num_rows = len(rows) - 1  # excluding header
num_cols = len(rows[0])

print("Number of rows:", num_rows)
print("Number of columns:", num_cols)



# Program to append a new record to an existing CSV file

import csv

with open("students.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sonia", "MBA", 92])

print("New record appended successfully!")



# Program to copy data from one CSV file to another

import csv

with open("students.csv", "r") as src, open("students_copy.csv", "w", newline='') as dest:
    reader = csv.reader(src)
    writer = csv.writer(dest)
    for row in reader:
        writer.writerow(row)

print("Data copied successfully to students_copy.csv")



# Program to display specific columns (Name and Marks) from a CSV file

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Name:", row["Name"], "| Marks:", row["Marks"])




# Program to find and display the highest marks from a CSV file

import csv

highest = 0
topper = ""

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks = int(row["Marks"])
        if marks > highest:
            highest = marks
            topper = row["Name"]

print("Highest Marks:", highest, "by", topper)



# Program to search a record in a CSV file based on student name

import csv

name = input("Enter student name to search: ")
found = False

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Name"].lower() == name.lower():
            print("Record Found:", row)
            found = True
            break

if not found:
    print("Record not found!")



# Program to combine multiple CSV files into one single file

import csv
import glob

csv_files = glob.glob("*.csv")  # all CSV files in current folder

with open("combined.csv", "w", newline='') as outfile:
    writer = None
    for filename in csv_files:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            if writer is None:
                writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)

print("All CSV files combined successfully into combined.csv")



