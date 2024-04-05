new_file = ""

with open(new_file, 'w') as f:
    for i in range(32, 128):
        f.write(chr(i) + " : \n\n")