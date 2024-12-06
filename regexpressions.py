import re

# split a string by commas or spaces
text = "apple, banana, orange, grape"
result = re.split(r'[\s]+', text)

print(result)