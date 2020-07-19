import sys
from functools import partial
def new():
    filename1=input("Input name of file1")
    filename2 = input("Input name of file2")

    with open(filename1, 'r') as f1:
        with open(filename2, 'r') as f2:
            same = set(f1).intersection(f2)

    same.discard('\n')

    with open('some_output_file.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)
            print("printing the lines containing plagarism: " + line)

def main():
    new()


if __name__ == '__main__':
    main()