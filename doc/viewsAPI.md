## Display All Students

### Usage:
```python
import student
import views
...
students = student.get_students()
views.display_students(students)
```

### Output:
```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ School ID    ┃ First Name ┃ Last Name ┃ Email                    ┃ Section ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ 201710101    │ Mark       │ Pearson   │ markpearson@school.edu   │ SEG31   │
│ 201711998    │ Mizugame   │ Za        │ mizugameza@jpmail.jp     │ SEG32   │
│ 201718239    │ John       │ Doe       │ johndoe@school.edu       │ SEG32   │
│ 201789012    │ Olea       │ Marco     │ oleamarco@school.edu     │ SEG32   │
│ 201901028    │ Gabriel    │ Francia   │ gdfrancia01901@proton.me │ SEG31   │
│ 201901029    │ Acindo     │ Monter    │ acindomonter@school.edu  │ SEG41   │
└──────────────┴────────────┴───────────┴──────────────────────────┴─────────┘
```

## Display Single Student

### Usage:
```python
import student
import views
...
found_student = student.get_student_by_id(201901028)
views.display_student(found_student)
```

### Output:
```
╭──────────────────────────╮
│ 201901028                │
│ Francia, Gabriel         │
│ gdfrancia01901@proton.me │
│ SEG31                    │
╰──────────────────────────╯
```

## Display Sections Count

### Usage:
```python
import views
...
views.display_sections_count()
```

### Output:
```
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Section ┃ No. of Students ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ SEG31   │ 2               │
│ SEG32   │ 3               │
│ SEG41   │ 1               │
├─────────┼─────────────────┤
│ Total   │ 6               │
└─────────┴─────────────────┘
```

## Display Section

### Usage:
```python
import views

views.display_section("SEG31")
```

### Output:
```
                                Section SEG31                                 
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ School ID    ┃ First Name ┃ Last Name ┃ Email                    ┃ Section ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ 201710101    │ Mark       │ Pearson   │ markpearson@school.edu   │ SEG31   │
│ 201901028    │ Gabriel    │ Francia   │ gdfrancia01901@proton.me │ SEG31   │
├──────────────┼────────────┼───────────┼──────────────────────────┼─────────┤
│              │            │           │           Student Count: │       2 │
└──────────────┴────────────┴───────────┴──────────────────────────┴─────────┘
```

