
with open('cs.txt', 'r') as cs_file:
    cs_majors = set(cs_file.read().splitlines())
with open('math.txt', 'r') as math_file:
    math_majors = set(math_file.read().splitlines())
double_majors = cs_majors.intersection(math_majors)

print("Math-CS Double Majors:", double_majors)
all_majors = cs_majors.union(math_majors)
print("People majoring in Math or CS:", all_majors)
strict_cs_majors = cs_majors.difference(math_majors)
print("Strictly CS Majors:", strict_cs_majors)