from os import system
import student

from rich.console import Console
from rich.panel import Panel
from manager import Manager
from views import print_menu

def main():
    student.migrate()
    exit = False
    console = Console()

    while not exit:
        manager = Manager()
        exit = manager.choice(print_menu())

        if exit == "INVINPUT":
            exit = False
            manager.pause(Panel("[bold red]\n❌ Invalid input! Press ENTER and try again.\n"))

    console.print(
        Panel("[bold yellow]\n📤 Now Exiting![/bold yellow][bold bright_green]\n✅ Thank you for using the app!\n"))

if __name__ == '__main__':
    main()
