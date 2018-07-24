import os
from os.path import expanduser

ACCESS_RIGHT = 0o755


def write_file(path, content):
    try:
        file = open(path, "w+")
        file.write(content)
        file.close()
    except EnvironmentError as e:
        print("File operation failed\nError: %s" % e)
        return "", -1
    return path, 0


def create_file(path):
    write_file(path + "/gcp.yml", "Ashish Ranjan")
    write_file(path + "/aws.yml", "Ashish Ranjan")
    write_file(path + "/azure.yml", "Ashish Ranjan")


def create_directory(path):
    try:
        os.makedirs(path, ACCESS_RIGHT)
    except OSError as e:
        print("Directory %s creation failed\nError: %s " % (path, e))
        return path, -1
    print("Successfully created directory %s" % path)
    return path, 0


def main():
    path = expanduser('~')+'/e2e'
    create_directory(path)
    create_file(path)


if __name__ == '__main__':
    main()
