import os
import argparse
import hashlib

def get_files_by_size(path, file_format):
    # Collect a list of file paths and sizes in the specified directory
    files_list = []
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if not file_format or file.lower().endswith(f".{file_format}"):
                files_list.append((filepath, os.path.getsize(filepath)))
    return files_list

def get_hash_duplicates(files_list):
    # Find duplicate files based on their hash values
    dupe_list = []
    hash_dict = {}
    counter = 1

    for filepath, size in files_list:
        with open(filepath, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
            hash_dict.setdefault(file_hash, []).append(filepath)
        
        for hash_value, filepaths in hash_dict.items():
            if len(filepaths) > 1 and hash_value not in dupe_list:
                print(f"Hash: {hash_value}")
                for filepath in filepaths:
                    print(f"{counter}. {filepath}")
                    dupe_list.append(hash_value)
                    counter += 1
    return dupe_list

def delete_files(file_numbers, dupe_list):
    # Delete selected files and return total freed space
    total_freed_space = 0

    for file_num in file_numbers:
        index = int(file_num) - 1
        if 0 <= index < len(dupe_list):
            filepath, size = dupe_list[index]
            os.remove(filepath)
            total_freed_space += size
    return total_freed_space

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=None)
    args = parser.parse_args()

    if not args.path:
        print("Directory is not specified")
        return

    print("Enter file format:")
    file_format = input().lower()

    # Get the list of files in the specified directory
    files_list = get_files_by_size(args.path, file_format)

    print("\nSize sorting options:")
    print("1. Descending")
    print("2. Ascending")

    print("\nEnter a sorting option:")
    size_sort = input()
    while size_sort not in ["1", "2"]:
        print("\nWrong option")
        size_sort = input()
    print()

    # Sort files by size and print them
    sorted_files_list = sorted(files_list, key=lambda x: x[1], reverse=size_sort == "1")

    for size, paths in sorted_files_list:
        print(f"{size} bytes")
        for path in paths:
            print(path)
        print()

    print("\nCheck for duplicates?")
    check_dupes = input()
    while check_dupes not in ["yes", "no"]:
        print("Wrong option")
        check_dupes = input()
    print()
    if check_dupes == "no":
        return

    # Find and display duplicate files based on hash values
    dupe_list = get_hash_duplicates(sorted_files_list)

    print("Delete files?")
    delete_files_option = input()
    while delete_files_option not in ["yes", "no"]:
        print("Wrong option")
        delete_files_option = input()
    print()
    if delete_files_option == "no":
        return

    # Delete selected duplicate files and display freed space
    print("Enter file numbers to delete:")
    file_numbers = [x for x in input().split() if x.isdigit()]

    while not file_numbers or max(map(int, file_numbers)) > len(dupe_list):
        print("Wrong format")
        file_numbers = [x for x in input().split() if x.isdigit()]

    total_freed_space = delete_files(file_numbers, dupe_list)
    print(f"Total freed up space: {total_freed_space} bytes")

if __name__ == "__main__":
    main()
