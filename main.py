import writer
import argparse

parser = argparse.ArgumentParser()

#-db DATABASE -u USERNAME -p PASSWORD -size 20000
parser.add_argument("word", help="Word to write")
parser.add_argument("-s", "--symbol", dest = "symbol", default = "@", help="Symbol to write with")
parser.add_argument("-o", "--output-file", dest = "output", default = "", help="Output file with the text to write")
args = parser.parse_args()

symbol = args.symbol
word = args.word
output = args.output
verbose = False
if output == "":
    verbose = True
writer.print_ascii_art(word, symbol=symbol, output_file=output, verbose=verbose)

if output != "":
    print(f"The phrase { word } has been written in the file {output} using the symbol '{symbol}'.")
