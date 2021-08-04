import sys

from reverse import reverse_file
from matching import is_matched

print("Pilih Menu:\n"
      "1. Reversing Data\n"
      "2. Matching Delimiters\n"
      "3. Close Program")

coice = int(input("Masukkan pilihan: "))
if coice == 1:
    reverse_file('listname.txt')
elif coice == 2:
    expression = input("Masukkan Expression : ")
    match = is_matched(expression)
    if match:
        print("\nDelimiters cocok")
    else:
        print("\nDelimiters tidak cocok")
else:
    sys.exit()