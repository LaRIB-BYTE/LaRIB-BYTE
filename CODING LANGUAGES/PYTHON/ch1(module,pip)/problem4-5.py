import os

# Define the directory path
directory_path = '.'  # '.' refers to the current directory

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory '{}':".format(directory_path))
for item in contents:
    print(item)
