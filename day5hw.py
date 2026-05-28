frontend_course = {'athul','akthar','ashik'}
backend_course = {'soorya','rahna','ashik'}
backend_course.add("akash")
print(backend_course)
frontend_course.pop()
print(frontend_course)
print("enrolled in both courses",  frontend_course & backend_course)
print("enrolled only in Backend, but not in Frontend", frontend_course-backend_course)
student_count = {"frontend":len(frontend_course),"backend":len(backend_course)}
print(student_count)
for course , count in student_count.items():
    print(f"{course}{count} students")
    