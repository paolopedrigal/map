import sys

if __name__ == "__main__":

    # Command line arguments
    # sys.argv[1] : FILE_NAME

    input_file = open(sys.argv[1])
    for line in input_file.readlines():
        print(line.strip("\n\t"), end=" ")
    print()