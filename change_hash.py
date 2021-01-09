import string
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="point to the file that needs hash changed", type=str)
args = parser.parse_args()
N = 128 #Sets the length of the hash changer, larger means more iterations before same hash is generated
comment = "#"
hash_change = ''.join(random.choices(string.ascii_letters + string.digits, k=N)) #Generates a string of ascii letters and numbers the length of N
string_to_add = comment + hash_change # Puts the comment character before the string
with open(args.filename, 'a') as c: 
    c.write(string_to_add) # Adds the comment to the file you put into the program.