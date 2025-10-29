import sys 
import re
from collections import Counter
# Will allow us to open file for reading.
# Thanks google. I am man enough to admit that I needed a bit of help to get these things done
with open(sys.argv[1], "r") as file:
    fileContents = file.read()

fileContents = re.sub(r'[^A-Z]', '', fileContents) # regex to keep only alpha characters
# Will return frequency of characters, bigrams and trigrams
singularChar = Counter(fileContents) 
bigramChars = Counter(fileContents[i:i + 2] for i in range(len(fileContents) - 1))
trigramChars = Counter(fileContents[i:i + 3] for i in range(len(fileContents) - 2))

# Uses lambda to tell sorted function to go off of the value rather than the key for the dicts
sortedChars = sorted(singularChar.items(), key=lambda x: x[1], reverse=True) 
sortedBigrams = sorted(bigramChars.items(), key=lambda x: x[1], reverse=True)
sortedTrigrams = sorted(trigramChars.items(), key=lambda x: x[1], reverse=True)
print("Character Frequencies\n")
for char, count in sortedChars:
    print(f"{char}: {count}")

print("\n Character Bigrams")
for bg, count in sortedBigrams:
    print(f"{bg}: {count}")

print("\n Character Trigrams")
for tg, count in sortedTrigrams:
    print(f"{tg}: {count}")


                       




