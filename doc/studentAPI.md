# Student API

## Add a new student

```python
import student
...
student.add_student(
    first_name="John",
    last_name="Doe",
    email="johndoe@school.edu",
    section="SEG32",
    student_no=201718239
)
```

## Update an existing student

```python
import student
...
updated_student = student.Student()

updated_student.student_number = 201901028
updated_student.first_name = "Gabriel"

student.find_and_update_student(updated_student)
```

## Delete an existing student

```python
import student
...
student.delete_student(201901029)
```

## Get all students

```python
import student
...
students = student.get_students()
for student in students:
    print(f"Student # {student.student_number} -- {student.first_name} {student.last_name}")
    print(f"\tEmail: {student.email}")
    print(f"\tSection: {student.section}")
```

## Search for Student by Student Number

```python
import student
...
student = student.get_student_by_id(201901028)
print(f"Student # {student.student_number} -- {student.first_name} {student.last_name}")
print(f"\tEmail: {student.email}")
print(f"\tSection: {student.section}")
```

## Search for Student by Last Name

```python
import student
...
students = student.get_students_by_last_name(last_name="Francia")
for student in students:
    print(f"Student # {student.student_number} -- {student.first_name} {student.last_name}")
    print(f"\tEmail: {student.email}")
    print(f"\tSection: {student.section}")
```

## Get All Sections and count number of students for each section

```python
import student
...
counts = student.get_sections_count()
for section in counts:
    print(f"{section}: {counts[section]}")
```

## Get a specific section's student count

```python
import student
seg31_count = student.get_sections_count("SEG31")
print(f"SEG31 count: {seg31_count}")
```
