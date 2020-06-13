import os


def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
    except OSError:
        print ("Creation of the directory %s failed" % directory_name)
    else:
        print ("Successfully created the directory %s " % directory_name)


def read_from_file(path):
    directory_list = []

    with open(path) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            directory_list.append(line.strip())
            line = fp.readline()
            cnt += 1

    return directory_list


filePath = 'directoryList.in'
directoryList = read_from_file(filePath)

for directoryName in directoryList:
    create_directory(directoryName)
