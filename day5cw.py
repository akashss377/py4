python = {'ashik','athul','soorya'}
data_science={'rahna','akthar','athul'}
python.add('arun')
print(python)
data_science.pop()
print(data_science)
print("names of students who are enrolled in both courses", python & data_science)
print(" students who are only in the Python course but not in Data Science", python - data_science)
print(python | data_science)
student_count={"python":len(python),"data_science":len(data_science)}
for x,y in student_count.items():
    print(f"course:{x},student {y}")
expected_growth = {x: x*x for x in student_count.items()}
print(expected_growth)


      