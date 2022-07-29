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

    def pause(self,custom_prompt="\n[italic]Press ENTER to continue."):
        self.console.input(custom_prompt)

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
        self.console.print(Panel("[bold green blink]📋 Add Student[/bold green blink]\n\n[italic]Leave any field empty to return to top menu"))
        first_name = self.console.input("[1] First Name: ")
        if first_name == "":
            return False
        last_name = self.console.input("[2] Last Name: ")
        if last_name == "":
            return False
        email = self.console.input("[3] Email: ")
        if email == "":
            return False
        section = self.console.input("[4] Section: ")
        if section == "":
            return False
        student_no = self.console.input("[5] Student No.: ")
        if not student_no.isdigit():
            self.pause("[red]❌ Student ID is invalid. Press ENTER to continue.")
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
        self.console.print(Panel("[cyan blink]🔍 Search Student - Select Search Mode"))
        self.console.print("[1] Search by ID")
        self.console.print("[2] Search by Last Name")
        self.console.print("[0] Return to Top")
        search_mode = self.console.input("Enter your choice: ")
        if not search_mode.isdigit():
            self.pause("[red]Invalid choice, press ENTER to try again.")
            return False

        if search_mode == "0":
            return False

        clear()
        if search_mode == "1":
            self.console.print(Panel("[bold cyan blink]🔍 Search Student by ID"))
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


        if search_mode == "2":
            self.console.print(Panel("[bold cyan blink]🔍 Search Student by Last Name"))
            student_name = self.console.input("[1] Last Name: ")
            if student_name == "":
                self.console.print("[red]❌ No student name provided.")
                self.pause()
                return False
            exists = student.get_students_by_last_name(student_name)
            if len(exists) == 0:
                self.console.print(
                    Panel("[bold red blink]\n❌ Error:[/] No matches found.\n"))
            else:
                self.console.print(Panel("[bold green]\n🔍 Matches found.\n"))
                display_students(exists)

        self.pause()
        return False

    def case3(self):
        """Edit a student

        Returns:
            Boolean: Wether to exit the app or not
        """
        clear()
        self.console.print(Panel("[bold yellow blink]📝 Edit Student[/bold yellow blink]\n\n[italic]Leave any field blank to return to top menu."))
        student_no = self.console.input("[1] Student No.: ")
        if student_no == "":
            return False
        if not student_no.isdigit():
            self.console.print("[red]❌ Student ID provided is invalid")
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
            edit_field = self.console.input("Enter your choice: ")

            if edit_field == "1":
                result.first_name = self.console.input(
                    f"Enter new first name ({result.first_name}): ")
                edited = True
            elif edit_field == "2":
                result.last_name = self.console.input(
                    f"Enter new last name ({result.last_name}): ")
                edited = True
            elif edit_field == "3":
                result.email = self.console.input(
                    f"Enter new email ({result.email}): ")
                edited = True
            elif edit_field == "4":
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
        self.console.print(Panel("[red blink]🔍 Delete Student - Select Search Mode"))
        self.console.print("[1] Delete by ID")
        self.console.print("[2] Delete by Last Name")
        self.console.print("[0] Return to Top")
        search_mode = self.console.input("Enter your choice: ")
        if not search_mode.isdigit():
            self.pause("[red]Invalid choice, press ENTER to try again.")
            return False

        if search_mode == "0":
            return False

        clear()
        student_delete_target = None

        if search_mode == "1":
            self.console.print(Panel("[red blink]❌ Delete Student"))
            student_no = self.console.input("[1] Student No.: ")
            if not student_no.isdigit():
                self.console.print("[red] Student ID provided is invalid")
                self.pause()
                return False
            student_delete_target = student.get_student_by_id(student_no)
            if not student_delete_target:
                self.console.print(
                    Panel("[bold red blink]\n❌ Student ID does not exist.\n"))
                self.pause()
                return False

        if search_mode == "2":
            self.console.print(Panel("[bold red blink]🔍 Delete Student by Last Name"))
            student_name = self.console.input("[1] Last Name: ")
            if student_name == "":
                self.console.print("[red]❌ No student name provided.")
                self.pause()
                return False
            exists = student.get_students_by_last_name(student_name)
            if len(exists) == 0:
                self.console.print(
                    Panel("[bold red blink]\n❌ Error:[/] No matches found.\n"))
                self.pause()
                return False
            elif len(exists) == 1:
                student_delete_target = exists[0]
            else:
                self.console.print(Panel("[bold green]\n🔍 Matches found.\n"))
                display_students(exists)
                student_id_target = self.console.input("Please type the student ID you wish to remove: ")
                if not student_id_target.isdigit():
                    self.console.print("[red]❌ Invalid ID provided.")

                student_delete_target = student.get_student_by_id(student_id_target)
                if not student_delete_target:
                    self.console.print(
                        Panel("[bold red blink]\n❌ Student ID does not exist.\n"))
                    self.pause()
                    return False
                if not student_delete_target in exists:
                    self.pause(Panel("[bold red blink]\n❌ Student ID does not match search query.\n\n[/bold red blink][italic]Press ENTER and try again."))
                    return False

        display_student(student_delete_target)
        self.console.print("\n[bold red blink]!! THIS ACTION IS IRREVERSIBLE !!")
        self.console.print("[red]Are you sure you want to remove this student record? Type[/red] [yellow italic]confirm[/yellow italic] [red]to confirm this action.")
        delete_confirm = self.console.input("> ")
        if delete_confirm == "confirm":
            student.delete_student(student_delete_target.student_number)
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
