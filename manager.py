import student

from os import system, name
from rich.console import Console
from rich.panel import Panel

from views import display_student, display_students, display_sections_count

# Clear function for dynamic os
def clear():
    # For Windows
    if name == 'nt':
        system('cls')

    # For Mac and Linux(here, os.name is 'posix')
    else:
        system('clear')

class Manager:
    console = Console()

    def pause(self):
        self.console.input("\n[italic]Press ENTER to continue.")

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
        if first_name == "":
            self.console.print("[red] First Name is empty")
        last_name = self.console.input("[2] Last Name: ")
        if last_name == "":
            self.console.print("[red] Last Name is empty")
        email = self.console.input("[3] Email: ")
        if email == "":
            self.console.print("[red] Email is empty")
        section = self.console.input("[4] Section: ")
        if section == "":
            self.console.print("[red] Section is empty")
        student_no = self.console.input("[5] Student No.: ")
        if not student_no.isdigit():
            self.console.print("[red] Student ID is invalid.")
            self.pause()
            return False
        exists = student.get_student_by_id(int(student_no))
        if exists:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student already exists!\n"))
        else:
            student.add_student(first_name,
                                last_name,
                                email,
                                student_no,
                                section)
            self.console.print(Panel("[bold green]\n✅ Student added!\n"))
            display_student(student.get_student_by_id(student_no))

        self.pause()
        return False

    def case2(self):
        """Search a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold cyan blink]🔍 Search Student"))
        student_no = self.console.input("[1] Student No.: ")
        if not student_no.isdigit():
            self.console.print("[red] Student ID provided is invalid")
            self.pause()
            return False
        exists = student.get_student_by_id(student_no)

        if not exists:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student does not exist!\n"))
        else:
            self.console.print(Panel("[bold green]\n🔍 Student found!\n"))
            display_student(exists)
        self.pause()
        return False

    def case3(self):
        """Edit a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold yellow blink]📝 Edit Student"))
        student_no = self.console.input("[1] Student No.: ")
        if not student_no.isdigit():
            self.console.print("[red] Student ID provided is invalid")
            self.pause()
            return False

        result = student.get_student_by_id(student_no)
        if not result:
            self.console.print(
                Panel("[bold red blink]\n❌ Error:[/] Student does not exist!\n"))
            self.pause()
        else:
            edited = False
            self.console.print(Panel("[bold green]\n🔍 Student found!\n"))
            display_student(result)
            self.console.print("[italic dim]What do you want to edit?")
            self.console.print("[1] [italic dim]First Name")
            self.console.print("[2] [italic dim]Last Name")
            self.console.print("[3] [italic dim]Email")
            self.console.print("[4] [italic dim]Section")
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
                self.console.print(Panel("[bold green]\n✅ Changes saved!\n"))
                display_student(student.get_student_by_id(student_no))
                self.pause()
            else:
                self.console.print(
                    Panel("[bold red blink]\n❌ No changes made.\n"))
                self.pause()
        return False

    def case4(self):
        """Delete a student

        Returns:
            Boolean: Wether to exit the app or not
        """

        clear()
        self.console.print(Panel("[red blink]❌ Delete Student"))
        student_no = self.console.input("[1] Student No.: ")
        if not student_no.isdigit():
            self.console.print("[red] Student ID provided is invalid")
            self.pause()
            return False

        exists = student.get_student_by_id(student_no)
        if not exists:
            self.console.print(
                Panel("[bold red blink]\n❌ Student ID does not exist.\n"))
            self.pause()
        else:
            display_student(exists)
            self.console.print("\n[bold red blink]!! THIS ACTION IS IRREVERSIBLE !!")
            self.console.print("[red]Are you sure you want to remove this student record? Type[/red] [yellow italic]confirm[/yellow italic] [red]to confirm this action.")
            delete_confirm = self.console.input("> ")
            if delete_confirm == "confirm":
                student.delete_student(student_no)
                self.console.print("[bold green]✅ Student record deleted!")
            else:
                self.console.print("[bold red]❌ Action aborted.")
            self.pause()
        return False

    def case5(self):
        """List all students

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[orange3]📃 List all students"))
        student_list = student.get_students()
        display_students(student_list)
        self.pause()
        return False

    def case6(self):
        """List sections

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[orange3]📄 List sections"))
        display_sections_count()
        self.pause()
        return False
