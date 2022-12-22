text = """Strings Operators
Python offers operatos to process text (ie string values).
Like numbers, strings can be compared using comparison operators: ==, !", <, > and so on.
The ==operator, for example, returns True if the strings on both sides of the operator have the same value (Perkovic p 23, 2016)"""

print(f"text size = {len(text)}")
text = text.lower()
text = text.replace(",","").replace(".","").replace("(","").replace(")","").replace("\n"," ")
list_words = text.split()
print(f"words size list = {len(list_words)}")

total = list_words.count("string") + list_words.count("strings")

print(f"Number of times string or strings appear = {total}")

