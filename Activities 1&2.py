try:
    with open('cs.txt') as f:
        cs = {line.strip() for line in f}
except FileNotFoundError:
    print("Error: 'cs.txt' not found.")
    cs = set()

try:
    with open('math.txt') as f:
        math = {line.strip() for line in f}
except FileNotFoundError:
    print("Error: 'math.txt' not found.")
    math = set()

year_dict = {}
try:
    with open('studentYear.txt') as f:
        for line in f:
            line_parts = line.strip().split(',')
            if len(line_parts) == 2 and line_parts[1].isdigit():
                name, year = line_parts
                year_dict[name] = int(year)
except FileNotFoundError:
    print("Error: 'studentYear.txt' not found.")
    year_dict = {}
print("Double Majors (CS & Math):")
print(cs & math)
print("\nMath or CS Majors:")
print(cs | math)
print("\nStrictly CS Majors:")
print(cs - math)
print("\nSophomore CS Majors:")
sophomore_cs_majors = {name for name in cs if year_dict.get(name) == 2}

