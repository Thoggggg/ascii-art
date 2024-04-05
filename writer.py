import os

MAX_DEF = 390 # Last line with a valid ascii art, all ascii art above must be valid

def ascii2index(ascii):
    return (ord(ascii) - 32) * 6

def print_line(output_file, line, verbose=False):
    # Write the ascii art in the command line and in the output file
    if output_file != '':
        with open(output_file, 'a') as o:
            o.write(line + "\n")

    # Print in the command as well
    if verbose:
        print(line)

def print_ascii_art(word, symbol='@', alphabet_file="fonts/ascii_5x5.art", output_file="output.txt", verbose=False):
    # Delete unwanted symbols
    for s in symbol:
        if ord(s) < 32:
            symbol = symbol.replace(s, '')

    with open(alphabet_file) as f:
        # read all the lines of the aphabet
        lines = f.readlines()

        # Delete the output file if it exists
        if(output_file != ''):
            if os.path.exists(output_file):
                os.remove(output_file)
            open(output_file, 'a').close()
            
        for row in range(1, 6):
            line = []
            for w in word:
                # Maximize every letters
                if w >= 'a' and w <= 'z':
                    w = w.upper()

                index = ascii2index(w)

                # Check if index exists
                if index > MAX_DEF:
                    word = word.replace(w, "")
                    continue
                line.append(lines[index + row][:-1])
            whole_row = ''.join(line)
            
            # Change the symbol used to write
            symbol_sz = len(symbol)

            # Ad spaces if the symbole used is to big
            if symbol_sz > 1:
                whole_row = whole_row.replace(' ', ' ' * symbol_sz)    
            whole_row = whole_row.replace('@', symbol)

            for _ in range(symbol_sz):
                print_line(output_file, whole_row, verbose=verbose)
                
            
if __name__ == "__main__":
    word = "Hi"
    print_ascii_art(word, symbol=word)
