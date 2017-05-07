
def get_longest_line(filename):
    # input_file = open(filename, 'r')
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
        lengths = [len(line.strip()) for line in lines]
        max_length = max(lengths)
        which_line = lengths.index(max_length)
    # input_file.close()
    return which_line + 1, max_length

print(get_longest_line("lines.csv"))
