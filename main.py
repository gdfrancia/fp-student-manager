from os import system
import student

from rich.console import Console
from rich.panel import Panel
from manager import Manager
from views import print_menu


if __name__ == '__main__':
    student.migrate()
    exit = False
    console = Console()

    while not exit:
        manager = Manager()

        exit = manager.choice(print_menu())

        if exit == "INVINPUT":
            exit = False
            console.print(
                Panel("[bold red]\n❌ Invalid input! Please try again\n"))
            system("PAUSE")

    console.print(
        Panel("[bold yellow]\n📤 Now Exiting![/bold yellow][bold bright_green]\n✅ Thank you for using the app!\n"))

    # student.add_student(
    #     first_name="John",
    #     last_name="Doe",
    #     email="johndoe@school.edu",
    #     section="SEG32",
    #     student_no=201718239
    # )
    # student.add_student(
    #     first_name="Mark",
    #     last_name="Pearson",
    #     email="markpearson@school.edu",
    #     section="SEG31",
    #     student_no=201710101
    # )

    # student.add_student(
    #     first_name="Olea",
    #     last_name="Marco",
    #     email="oleamarco@school.edu",
    #     section="SEG32",
    #     student_no=201789012
    # )

    # student.add_student(
    #     first_name="Cindr",
    #     last_name="Mon",
    #     email="cindrmon@proton.me",
    #     section="SEG31",
    #     student_no=201901029
    # )

    # student.add_student(
    #     first_name="Gabriel",
    #     last_name="Francia",
    #     email="gdfrancia01901@proton.me",
    #     section="SEG31",
    #     student_no=201901028
    # )

    # student.add_student(
    #     first_name="Mizugame",
    #     last_name="Za",
    #     email="mizugameza@jpmail.jp",
    #     section="SEG32",
    #     student_no=201711998
    # )

    # student.delete_student(201901029)

    # students = student.get_students()
    # for student in students:
    #     print(
    #         f"Student # {student.student_number} -- {student.first_name} {student.last_name}")
    #     print(f"\tEmail: {student.email}")
    #     print(f"\tSection: {student.section}")

    # counts = student.get_sections_count()
    # for section in counts:
    #     print(f"{section}: {counts[section]}")
    #
    # seg31_count = student.get_sections_count("SEG31")
    # print(f"SEG31 count: {seg31_count}")
