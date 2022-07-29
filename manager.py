import student

from os import system, name
from rich.console import Console
from rich.panel import Panel

from views import display_student

# Clear function for dynamic os


def clear():

    # For Windows
    if name == 'nt':
        system('cls')

    # For Mac and Linux(here, os.name is 'posix')
    else:
        system('clear')


def pause():
    system("PAUSE")


class Manager:
    console = Console()

    def choice(self, choice):
        default = "INVINPUT"

        return getattr(self, "case" + str(choice), lambda: default)()

    def case0(self):
        return True

    def case1(self):
        """Add a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold green blink]📋 Add Student"))
        first_name = self.console.input("[1] First Name: ")
        last_name = self.console.input("[2] Last Name: ")
        email = self.console.input("[3] Email: ")
        section = self.console.input("[4] Section: ")
        student_no = self.console.input("[5] Student No.: ")
        exists = student.get_student_by_id(int(student_no))

        if exists:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student already exists!\n"))
            pause()
        else:
            student.add_student(first_name,
                                last_name,
                                email,
                                student_no,
                                section)
            self.console.print(Panel("[bold green]\n✅ Student added!\n"))
            display_student(student.get_student_by_id(student_no))
            pause()

        return False

    def case2(self):
        """Search a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold cyan blink]🔍 Search Student"))
        student_no = self.console.input("[1] Student No.: ")
        exists = student.get_student_by_id(student_no)

        if not exists:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student does not exist!\n"))
            pause()
        else:
            self.console.print(Panel("[bold green]\n🔍 Student found!\n"))
            display_student(exists)
            pause()
        return False

    def case3(self):
        """Edit a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold yellow blink]📝 Edit Student"))
        student_no = self.console.input("[1] Student No.: ")
        result = student.get_student_by_id(student_no)

        if not result:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student does not exist!\n"))
            pause()
        else:
            edited = False
            self.console.print(Panel("[bold green]\n🔍 Student found!\n"))
            display_student(result)
            self.console.print("[italic dim]What do you want to edit?")
            self.console.print("[1] [italic dim]First Name?")
            self.console.print("[2] [italic dim]Last Name?")
            self.console.print("[3] [italic dim]Email?")
            self.console.print("[4] [italic dim]Section?")
            edit_field = int(self.console.input("Enter your choice: "))

            if edit_field == 1:
                result.first_name = self.console.input(
                    f"Enter new first name ({result.first_name}): ")
                edited = True
            elif edit_field == 2:
                result.last_name = self.console.input(
                    f"Enter new last name ({result.last_name}): ")
                edited = True
            elif edit_field == 3:
                result.email = self.console.input(
                    f"Enter new email ({result.email}): ")
                edited = True
            elif edit_field == 4:
                result.section = self.console.input(
                    f"Enter new section ({result.section}): ")
                edited = True

            if edited:
                student.find_and_update_student(result)
                self.console.print(Panel("[bold green]\n✅ Saved Edits!\n"))
                display_student(student.get_student_by_id(student_no))
                pause()
            else:
                self.console.print(
                    Panel("[bold red blink]\n❌ Error:[/] No edits done!\n"))
                pause()
        return False

    def case4(self):
        """Delete a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        self.console.print("Case 4")
        return False

    def case5(self):
        """List all students

        Returns:
            Boolean: Wether to exit the app or not
        """
        self.console.print("Case 5")
        return False

    def case6(self):
        """List sections

        Returns:
            Boolean: Wether to exit the app or not
        """
        self.console.print("Case 6")
