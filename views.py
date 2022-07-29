from typing import List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from os import system, name

from student import Student
import student as s

console = Console()


def clear():

    # For Windows
    if name == 'nt':
        system('cls')

    # For Mac and Linux(here, os.name is 'posix')
    else:
        system('clear')


def _get_content(std: Student):
    """Extract text from student class and add card-like formatting"""

    student_no = std.student_number
    name = f"{std.last_name}, {std.first_name}"
    email = std.email
    section = std.section
    return f"[yellow]Student No: [/][b green]{student_no}[/]\n[yellow]Name: [/][b cyan]{name}[/]\n[yellow]Email: [/][b u]{email}[/]\n[yellow]Section: [/][b red]{section}[/]"


def display_students(student_list: List[Student],
                     show_footer=False,
                     table_title="", school_id_footer="", first_name_footer="", last_name_footer="",
                     email_footer="", section_footer=""):
    """Displays a table of a particular student list, with optional footer parameters"""

    table = Table(title=table_title, show_header=True,
                  show_footer=show_footer, header_style="bold red")
    table.add_column("School ID", style="dim", width=12,
                     footer=Align.right(school_id_footer))
    table.add_column("First Name", footer=Align.right(first_name_footer))
    table.add_column("Last Name", footer=Align.right(last_name_footer))
    table.add_column("Email", footer=Align.right(email_footer))
    table.add_column("Section", footer=Align.right(section_footer))
    for std in student_list:
        table.add_row(
            str(std.student_number),
            std.first_name,
            std.last_name,
            std.email,
            std.section
        )

    console.print(table)


def display_student(std: Student):
    """displays a card for a particular student"""
    student_renderable = [Panel(_get_content(std), expand=True)]
    console.print(Columns(student_renderable))


def display_sections_count():
    """displays a table of sections and the student count for each section, with the total student count
    as the footer"""
    table = Table(show_header=True, show_footer=True, header_style="bold red")
    table.add_column("Section", style="dim", footer="Total")
    table.add_column("No. of Students", footer=str(s.get_total_students()))
    students_count = s.get_sections_count()
    for section in students_count:
        if section != 'Total':
            table.add_row(
                section,
                str(students_count[section])
            )
    console.print(table)


def display_section(section: str):
    """displays a list of students in a selected section

    :param section: the section to show the students of
    """
    section_list = s.get_students_by_section(section)
    display_students(section_list, table_title=f"Section {section}",
                     show_footer=True,
                     email_footer="Student Count:",
                     section_footer=f"{s.get_section_count(section)}")


def print_menu():
    """Prints the menu
    """
    clear()
    console.print(Panel("[bold cyan]🎓 Student Management System"))
    console.print("[1] [green]📋 Add Student")
    console.print("[2] [cyan]🔍 Search Student")
    console.print("[3] [yellow]📝 Edit Student")
    console.print("[4] [red]❌ Delete Student")
    console.print("[5] [orange3]📃 List all students")
    console.print("[6] [orange3]📄 List sections")
    console.print("[0] [magenta]📤 Exit")
    return console.input("Enter your choice: ")
