

student_data = []


try:
    with open("studentYear.txt", "r") as file:
        students = file.readlines()
except FileNotFoundError:
    print("Error: The file 'studentYear.txt' was not found.")
    students = []  


student_data = []
for line in students:
  
    try:
        name, major, year = line.strip().split(",")
        student_data.append({"name": name, "major": major, "year": int(year)})
    except ValueError:
        print(f"Skipping improperly formatted line: {line.strip()}")


sophomore_cs_majors = [student["name"] for student in student_data if student["year"] == 2 and student["major"] == "CS"]


freshmen_not_math_cs = [student["name"] for student in student_data if student["year"] == 1 and student["major"] not in ["Math", "CS"]]


senior_math_cs_majors = [student["name"] for student in student_data if student["year"] == 4 and student["major"] in ["Math", "CS"]]

if 4 in [student["year"] for student in student_data]:
    print("Senior []Math and CS Majors")

print("Sophomore CS Majors:", sophomore_cs_majors)
print("Freshmen not in Math or CS:", freshmen_not_math_cs)
print("Senior Math and CS Majors:", senior_math_cs_majors)
