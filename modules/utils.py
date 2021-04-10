import os


def get_file_names(folderpath, out="../output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    file_list = os.listdir(folderpath)
    with open(out, "w") as file2:
        for object_name in file_list:
            file2.write(str(object_name) + "\n")


def get_all_file_names(folderpath, out="../output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    print("folder pathh: ", folderpath)
    file_list = os.listdir(folderpath)
    print("file_list:")
    print(file_list)
    with open(out, "a") as file2:
        for object_name in file_list:
            file2.write(str(object_name) + "\n")
            dir_path = os.path.join(folderpath, str(object_name))
            if os.path.isdir(
                    dir_path
            ):  #                Return True if path is an existing directory. This follows symbolic links, so both islink() and isdir() can be true for the same path.)

                print("Is dir", dir_path)
                get_all_file_names(dir_path, out)


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

    for file_name in file_names:
        if (os.path.isfile(file_name)):
            with open(file_name, "r") as file1:
                file_lines = file1.readlines()
                if not file_lines:
                    print("EMPTY")
                else:
                    print(file_lines[0])
        else:
            print("File ", file_name, " is not a file")


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file_name in file_names:
        with open(file_name, "r") as file1:
            lines = file1.readlines()
            for line in lines:
                if "@" in line:
                    print(line)


def write_headlines(md_files, output_file):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for file_name in md_files:
        with open(file_name, "r") as file1:
            lines = file1.readlines()
            for line in lines:
                if line.startswith("#"):
                    print(line)
                    with open(output_file, "a") as file2:
                        file2.write(line)