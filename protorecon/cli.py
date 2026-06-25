# Imports 
import os
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table 
from rich.prompt import Prompt 
from colorist import Color, Effect


#Building the actual app. Runs a callback to main instead of an error
app = typer.Typer(invoke_without_command=True)
console = Console()

#colors. Created to make colors the same and easy to change
proto_green = "16c819"
proto_cyan = "1CDC9A"
proto_red = "B5382B"
proto_amb = "FFC107"

#Creates program state. Stores the information of the session including settings, modules, and the runtime.
class ProtoState:
    def __init__(self):
        self.workspace = "default"
        self.loaded_module = None
        self.running = True

def clear_screen():
    #Clear the terminal before making the Protorecon banner
    os.system("cls" if os.name == "nt" else "clear")

BANNER = r"""
██████╗ ██████╗  ██████╗ ████████╗ ██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
"""


def show_banner():
    clear_screen()
    console.print(f"[bold green]{BANNER}[/bold green]")
    console.print("[cyan]Passive OSINT Framework[/cyan]")
    console.print("[green]Reconnaissance. Intelligence. Control.[/green]\n")

    console.print(
        Panel.fit(
            "[green]Author[/green]     : Protovoid\n"
            "[green]Version[/green]    : 0.1.0\n"
            "[green]Workspace[/green]  : default\n"
            "[green]Database[/green]   : not connected\n"
            "[green]Modules[/green]    : loading soon",
            title="[bold cyan]ProtoRecon Console[/bold cyan]",
            border_style="green",
        )
    )

    console.print("\nType [green]help[/green] to view available commands.")
    
#Table to display command lists
def show_commands():
    table = Table(
        title="Available Commands",
        border_style="green",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Command", style="green")
    table.add_column("Description", style="white")

    table.add_row("banner", "Display the banner")
    table.add_row("username <target>", "Run username lookup placeholder")
    table.add_row("help", "Show available commands")
    table.add_row("clear", "Clears the screen")

    console.print(table)

#This next section starts the console/shell loop. It will act like msfconsole
def start_console():
    state = ProtoState()
    clear_screen()
    show_banner()

    while state.running:
        command = console.input(f"[bold color(46)]ProtoRecon[/bold color(46)]([cyan]{state.workspace}[/cyan]) > ")
        
        if command in ["exit", "quit"]:
            console.print("[yellow]Exiting ProtoRecon[/yellow]")
            state.running = False
        elif command == "help":
            show_commands()
        elif command == "clear":
            clear_screen()
            show_banner()
        elif command =="banner":
            show_banner()
        elif command.startswith("username "):
            target=command.replace("username","",1).strip()
            username(target)
        elif command=="":
            continue
        else:
            console.print(f"[red][-][/red] Unknown Command: {command}")
            console.print("Type [green]help[/green] for available commands.")


@app.callback()
def main(ctx: typer.Context):
    """
    ProtoRecon passive OSINT framework.
    """
    if ctx.invoked_subcommand is None:
        start_console()

#show available ProtoRecon commands
@app.command()
def commands():
    show_commands()
    
@app.command()
def banner():
    """Display the ProtoRecon banner."""
    show_banner()


@app.command()
def username(target: str):
    """Run a basic username lookup placeholder."""
    console.print(f"[green][+][/green] Running username scan for: [bold]{target}[/bold]")
    console.print("[yellow][!][/yellow] Username module not built yet.")


if __name__ == "__main__":
    app()