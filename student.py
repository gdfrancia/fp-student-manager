from sqlalchemy import Column, Integer, String, func
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


def migrate():
    Model.metadata.create_all(bind=database.Engine)


def add_student(first_name, last_name, email, student_no, section):
    new_student = Student()
    new_student.student_number = student_no
    new_student.first_name = first_name
    new_student.last_name = last_name
    new_student.email = email
    new_student.section = section

    ct = database.Session()
    ct.add(new_student)
    ct.commit()
    ct.close()


def get_students(student_no=0, last_name=""):
    ct = database.Session()

    # if student number is specified
    if student_no != 0:
        students = ct.query(Student).where(Student.student_number == student_no)
    # if last name is specified
    elif last_name != "":
        students = ct.query(Student).where(Student.last_name == last_name)
    # otherwise, return all
    else:
        students = ct.query(Student).all()

    ct.close()

    return students


def get_sections_count(section=""):
    # get sections count as tuple
    ct = database.Session()
    # if a section is specified
    if section != "":
        section_count = ct.query(func.count(Student.section))\
            .filter(Student.section == section)\
            .group_by(Student.section)\
            .scalar()
        return section_count

    # otherwise return all sections
    else:
        sections_count = dict(
            ct.query(Student.section, func.count(Student.section))
            .group_by(Student.section)
            .all()
        )
    ct.close()

    # returns array of dictionaries of {section: count}
    return sections_count


# def update_student(student_no):
#     selected_student =


def delete_student(student_no):
    ct = database.Session()
    student_to_del = ct.query(Student).filter(Student.student_number == student_no).one()
    ct.delete(student_to_del)
    ct.commit()
    ct.close()
