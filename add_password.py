import sys

if __name__ == '__main__':
    try:
        name = sys.argv[1]
    except IndexError:
        print("Enter the name for password:")
        name = input()
