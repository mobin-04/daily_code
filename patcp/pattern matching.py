import re

# Sample text string
text = "The quick brown fox jumps over the lazy dog"

# 1. re.match(): Match at the beginning of the string
pattern1 = "He"  # Define a pattern to match
match1 = re.match(pattern1, text)  # Attempt to match the pattern at the beginning of the string
print("re.match():", match1.group() if match1 else "No match")  # Output the match or "No match" if not found

# 2. re.search(): Search for a pattern anywhere in the string
pattern2 = "brown"  # Define a pattern to search for
match2 = re.search(pattern2, text)  # Search for the pattern anywhere in the string
print("re.search():", match2.group() if match2 else "No match")  # Output the match or "No match" if not found

# 3. re.findall(): Find all occurrences of a pattern in the string
pattern3 = "o"  # Define a pattern to find all occurrences of
matches3 = re.findall(pattern3, text)  # Find all occurrences of the pattern in the string
print("re.findall():", matches3)  # Output all matches
