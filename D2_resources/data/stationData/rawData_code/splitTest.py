import re

tests = ["P1A", "UP1", "P", "PT20A"]

for string in tests:

    print(re.findall("^[A-Z]*", string))
