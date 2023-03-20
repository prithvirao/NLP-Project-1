def read_file(file_path):
    file_contents = ""
    file_obj = open(file_path, "r")
    file_data = file_obj.read()
    lines = file_data.splitlines()
    for line in lines:
        file_contents = file_contents + line[11:]
        #print(line[11:])
    return file_contents





