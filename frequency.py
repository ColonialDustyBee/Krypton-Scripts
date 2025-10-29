import sys 
from collections import Counter
# Will allow us to open file for reading.
with open(sys.argv[1], "r") as file:
    fileContents = file.read()

# Will return frequency of characters, bigrams and trigrams
singularChar = Counter(fileContents) 
bigramChars = Counter(fileContents[i:i + 2] for i in range(len(fileContents) - 1))
trigramChars = Counter(fileContents[i:i + 3] for i in range(len(fileContents) - 2))


print("Character Frequencies\n")
for char, count in singularChar.items():
    print(f"{char}: {count}")

print("\n Character Bigrams")
for bg, count in bigramChars.items():
    print(f"{bg}: {count}")

print("\n Character Trigrams")
for tg, count in trigramChars.items():
    print(f"{tg}: {count}")


                       




