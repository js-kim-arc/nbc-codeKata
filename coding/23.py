import re

def solution(s):
    return re.sub(r'\S+', lambda m:m.group()[0].upper() + m.group()[1:].lower(), s)