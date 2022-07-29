"""Student Repository

A basic student repository model that acts as the DAO (Data Access Object) for the `student` table,
which uses sqlalchemy for handling SQL requests to and from the database (sqlite3).
"""
from typing import List, Any

from sqlalchemy import Column, Integer, String, func, text
from sqlalchemy.ext.declarative import declarative_base

import database

Model = declarative_base(name='Model')


class Student(Model):
    __tablename__ = "student"
    student_number = Column('student_number', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    email = Column('email', String)
    section = Column('section', String)

    def __init__(self, first_name: str = "", last_name: str = "", email: str = "", section: str = "",
                 student_number: int = 0, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.student_number = student_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.section = section

    def __eq__(self, other):
        return type(self) is type(other) and self.student_number == other.student_number

    def __ne__(self, other):
        return not self.__eq__(other)


def migrate():
    """Initialises the Student table if it had not already exist
    """
    Model.metadata.create_all(bind=database.Engine)


def add_student(first_name: str, last_name: str, email: str, student_no: int, section: str):
    """Adds a student to the database.

    Parameters
    ----------
    :param first_name: Student's first name
    :param last_name: Student's last name
    :param email: Student's email
    :param student_no: Student's School ID
    :param section: Student's Section
    """

    # sets the student as a Model first before adding to database
    new_student = Student()
    new_student.student_number = student_no
    new_student.first_name = first_name
    new_student.last_name = last_name
    new_student.email = email
    new_student.section = section

    # run database query
    ct = database.Session()
    ct.add(new_student)
    ct.commit()
    ct.close()


def get_students() -> List[Student]:
    """gets all students from the database

    :return: a list of students
    """
    ct = database.Session()
    students = ct.query(Student).all()
    ct.close()
    return students


def get_students_by_last_name(last_name: str) -> List[Student]:
    """gets all students from the database with a specific last name

    :param last_name: search parameter for a student's last name
    :return: a list of students
    """
    ct = database.Session()
    students = ct.query(Student).where(Student.last_name == last_name).all()
    ct.close()
    return students


def get_student_by_id(student_no: int) -> Student:
    """gets a single student with that specific student number

    :param student_no: search parameter for a student's number
    :return: a single student
    """
    ct = database.Session()
    found_student = ct.query(Student).get(student_no)
    ct.close()
    return found_student


def get_sections_count() -> dict[str, int]:
    """gets student counts for all sections

    :return: a dictionary where the key is the section, and the value is the student count for that section
    """
    ct = database.Session()
    sections_count = ct.query(Student.section, func.count(Student.section))\
        .group_by(Student.section)\
        .all()
    return dict(sections_count)


def get_total_students() -> int:
    """gets the total number of students in the database

    :return: the total number of students in the database
    """

    ct = database.Session()
    total_count = ct.query(func.count(Student.section)).scalar()
    ct.close()
    return total_count


def get_section_count(section: str) -> int:
    """gets a student count for a specific section

    :param section: search parameter to select only a specific student count for that section
    :return: an int that specified the section's student count
    """
    ct = database.Session()
    if section != "":
        section_count = ct.query(func.count(Student.section)) \
            .filter(Student.section == section) \
            .group_by(Student.section) \
            .scalar()
    ct.close()
    return section_count


def find_and_update_student(student: Student):
    """finds and updates a student matching the student ID using a student object as a parameter

    :param student: a student object that must contain a student ID and data to update the student
    """
    ct = database.Session()
    selected_student = ct.query(Student).get(student.student_number)

    # if all parameters are empty or the same as current object
    # does premature break
    if (student.first_name == "" and student.first_name == selected_student.first_name) and \
            (student.last_name == "" and student.last_name == selected_student.last_name) and \
            (student.email == "" and student.email == selected_student.email) and \
            (student.section == "" and student.section == selected_student.section):
        print("Nothing Updated. Please update at least 1 parameter.")
        ct.rollback()
        ct.close()
        return

    # checks which object parameters are not empty or the same as dataset and updates it
    # istg im not yanderedev pls don't sue me ;-;
    if (student.first_name != "") and (student.first_name != selected_student.first_name):
        selected_student.first_name = student.first_name
    if (student.last_name != "") and (student.last_name != selected_student.last_name):
        selected_student.last_name = student.last_name
    if (student.email != "") and (student.email != selected_student.email):
        selected_student.email = student.email
    if (student.section != "") and (student.section != selected_student.email):
        selected_student.section = student.section

    # adds the updated student based on the if statements, please.. im sorry na ;-;
    ct.add(selected_student)
    ct.commit()
    ct.close()


def delete_student(student_no: int):
    """deletes the specified student using a student number.

    :param student_no: student number of student to delete
    """
    ct = database.Session()
    student_to_del = ct.query(Student).filter(
        Student.student_number == student_no).one()
    if student_to_del is not None:
        ct.delete(student_to_del)
        ct.commit()
    else:
        print("Student not found, no changes were made.")
        ct.rollback()
    ct.close()
