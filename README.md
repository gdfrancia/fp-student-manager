# Final Project -- Student Manager

> A Python CLI Application that manages students and saves it to a local sqlite3 database file.

## Credits

- [Gabriel Dominic Francia](https://github.com/cindrmon)
  - Backend API and Database ORM Setup
- [Paolo Steven Santos](https://github.com/mahomuri)
  - Frontend CLI Commands
- [Lance David Selga](https://github.com/lyonlancer5)
  - Validation checks and general cleanup

## Features/Specifications:

- Display a menu with the following options:
  1. Add student
     - allow the user to enter a student's First Name, Last Name, Email and Student Number and Section
     - for each student added, save that student into a database of all added students through the application
     - note that the student number has to be unique
  2. Search
     - allow the user to search a student through Last Name or Student Number
     - if the student exists in the database, display the student's info. Otherwise, display the necessary message.
  3. Edit
     - allow a user to search and edit a student's information
  4. Delete a student
     - allow the user to delete a student from the database through Last Name or Student Number.
     - if more than one student matches the result, ask the user to enter the Student Number of the student to be deleted
  5. Display all students
     - display the student info in a table format sorted by student number
  6. Display sections
     - display all the sections and their student count
     - this can be extracted from the students' info
  7. Persistence
     - Have a persistent student record through files. It can be in any file format you like

## Development Environment Setup

### Requirements
- `python 3.10.x`
- `pip`
- `pipenv`

### Procedure
> presuming you have set up the aforementioned requirements

1. Clone the Project
```shell
$ git clone https://github.com/cindrmon/fp-student-manager.git
```

2. Enter into project virtual environment with `pipenv`
```shell
$ pipenv shell
```

3. Install Dependencies using `pipenv`
```shell
$ pipenv install
```

4. Run Main Program with `python`
```shell
$ python main.py
```
