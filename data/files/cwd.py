import os
def cwd():
    print("processing")
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    print("the directory contains the following files:")
    for file in os.listdir(path):
        print(file)

cwd()