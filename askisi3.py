with open(file1, 'r') as f:
    lines = f.readlines()

with open(file2, 'w') as f:
    for line in lines:
        if line[0:2] == "#!":
            f.writelines(line)
        elif not line.strip():
            f.writelines(line)
        else:
            line = line.split('#')
            stripped_string = line[0].rstrip()
            if stripped_string:
                f.writelines(stripped_string)
                f.writelines('\n')
