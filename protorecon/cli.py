# Imports 
import os
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table 
from rich.prompt import Prompt 
#from colorist import Color, Effect

#py imports for modules and other files 
from protorecon.framework.state import SessionState
from protorecon.framework.ui import show_banner
from protorecon.framework.commands import get_commands

#Building the actual app. Runs a callback to main instead of an error
app = typer.Typer(invoke_without_command=True)
console = Console()

#colors. Created to make colors the same and easy to change WIP.
#PROTO_GREEN = "16c819"
#PROTO_CYAN = "1CDC9A"
#PROTO_RED = "B5382B"
#PROTO_AMB = "FFC107"

#Creates program state. Stores the information of the session including settings, modules, and the runtime.
class ProtoState:
    def __init__(self):
        self.workspace = "default"
        self.loaded_module = None
        self.running = True

def clear_screen():
    #Clear the terminal before making the Protorecon banner
    os.system("cls" if os.name == "nt" else "clear")

    

#This next section starts the console/shell loop. It will act like msfconsole
def start_console():
    state = SessionState()
    commands = get_commands()

    clear_screen()
    show_banner(console, state)
    

    while state.running: #Read user input as typed
        user_input = console.input(f"[bold color(46)]ProtoRecon[/bold color(46)]([cyan]{state.workspace}[/cyan]) > ").strip()
        #command = console.input(f"[bold color(46)]ProtoRecon[/bold color(46)]([cyan]{state.workspace}[/cyan]) > ").strip().lower()
        #Skip if empty
        if not user_input:
            continue
        #split input into separate words
        parts = user_input.split()

        #first word is command
        command = parts[0].lower()

        #everything else is the arg

        args = parts[1:]
        if command in ["exit", "quit"]:
           state.running = False
           console.print("[yellow]Exiting ProtoRecon...[/yellow]")
        elif command in commands:
            commands[command](console, state, args)
        else:   
            console.print(f"[red][!] Unknown command:[/red] [yellow]{command}[/yellow]")

#
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

if __name__ == "__main__":
    app()