# Duplicate File Handler

Duplicate File Handler is a useful tool that can free some space on your drive.

# How to use:

## Step 1: Run the Program
Save the optimized code into a .py file, for example, duplicate_finder.py. Open a terminal or command prompt and navigate to the directory containing the file. Then run the program using the command:

```python
python duplicate_finder.py
```

## Step 2: Provide Directory Path
The program will prompt you to provide the path of the directory you want to search for duplicate files in. Enter the directory path or leave it empty and press Enter if you want to use the current directory.

```python
duplicate_finder.py D:\YOUR FOLDER HERE
```

Enter File Format (Optional):
The program will prompt you to enter a file format to filter the search for specific file types (e.g., "txt", "jpg"). If you want to search for all file types, simply press Enter.

## Step 3: Choose Sorting Option
The program will prompt you to choose a sorting option for the list of files. Enter either "1" for descending order (largest files first) or "2" for ascending order (smallest files first).

View File List:
The program will display the list of files in the chosen sorting order along with their sizes.

## Step 4: Check for Duplicates
The program will ask if you want to check for duplicate files based on their hash values. Enter "yes" or "no".

View Duplicate List:
If you chose to check for duplicates, the program will display a list of duplicate files based on their hash values, along with their hash values. Each duplicate group will be numbered.

## Step 5: Delete Duplicate Files
The program will ask if you want to delete any of the duplicate files. Enter "yes" or "no". If you choose to delete, you'll be prompted to enter the numbers of the duplicate groups you want to delete. Separate the numbers with spaces.

## Step 6: View Freed Space
After deleting duplicate files, the program will display the total amount of freed-up space in bytes.

That's it! The program will guide you through the process of searching for duplicate files, showing you the list of duplicates, and allowing you to delete them if desired.
