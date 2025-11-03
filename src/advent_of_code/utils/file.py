def read_file_into_array(file_path):
    
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line)

    return lines
