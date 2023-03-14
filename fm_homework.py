
import string

str1 = "The quick brown fox jumps over the lazy dog"
alphabet=list(string.ascii_lowercase)
str1.lower()
str2 = list(str1.lower().replace(" ",""))
uniq_str2 = []
for item in str2:
    if item not in uniq_str2:
        uniq_str2.append(item)
uniq_str2.sort()

if uniq_str2 == alphabet:
     print("The str1 is pangram")
else:
     print("The str1 is NOT pangram")
