#command pallet for ProtoRecon. Lists commands and can be called across the cli
# Imports 
import os
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table 
from rich.prompt import Prompt 
from protorecon.framework.ui import show_banner
from protorecon.framework.workspaces import workspace_command
from protorecon.framework.targets import target_command
from protorecon.modules.web.whois import whois_command
from protorecon.modules.people.username import sherlock_command
#main

# def show_help(console, state):
#     console.print("[bold green]Available Commands[/bold green]")
#     console.print(" [cyan] help        Show available commands[/cyan]")
#     console.print(" [cyan] banner      Redraw the banner[/cyan]")
#     console.print(" [cyan] clear       Clear the screen[/cyan]")
#     console.print(" [cyan] cls         Clear the screen[/cyan]")
#     console.print(" [cyan] exit        Exit ProtoRecon[/cyan]")
#     console.print(" [cyan] quit        Exit ProtoRecon[/cyan]")

#Building the actual app. Runs a callback to main instead of an error
app = typer.Typer(invoke_without_command=True)
console = Console()

#Area for different commands for help and program
def clear_screen():
    #Clear the terminal before making the Protorecon banner
    os.system("cls" if os.name == "nt" else "clear")

# @app.command()
# def username(target: str):
#     """Run a basic username lookup placeholder."""
#     console.print(f"[green][+][/green] Running username scan for: [bold]{target}[/bold]")
#     console.print(f"[yellow][!][/yellow] Username module not built yet.")
def clear_command(console, state, args):
    clear_screen()
    show_banner(console, state)


def banner_command(console, state, args):
    show_banner(console, state)


# def username_command(console, state, args):
    # if not args:
        # console.print("[red][!][/red] Usage: username <target>")
        # return
    # target = args[0]
# 
    # console.print(f"[green][+][/green] Running username scan for: [bold]{target}[/bold]\n[yellow][!] Module under construction...[/yellow]")
    
@app.command()
def banner():
    """Display the ProtoRecon banner."""
    show_banner(console, None)


    #Table to display command lists
def show_commands(console, state, args):
    table = Table(
        title="Available Commands",
        border_style="green",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Command", style="green")
    table.add_column("Description", style="white")

    table.add_row("help", "Show available commands")
    table.add_row("banner", "Redisplay the ProtoRecon banner")
    table.add_row("clear", "Clear the console")
    table.add_row("cls", "Clear the console")

    table.add_row("username <target>", "Run the username lookup module")

    table.add_row("workspace", "Show the active workspace")
    table.add_row("workspace list", "List all workspaces")
    table.add_row("workspace create <name>", "Create a new workspace")
    table.add_row("workspace use <name>", "Switch to a workspace")
    table.add_row("workspace remove <name>", "Remove a workspace")
    table.add_row("workspace delete <name>", "Remove a workspace")

    table.add_row("target", "Show the active target")
    table.add_row("target list", "List all targets")
    table.add_row("target add <target>", "Add a target")
    table.add_row("target aim <target>", "Set the active target")
    table.add_row("target use <target>", "Set the active target")
    table.add_row("target clear", "Clear the active target")
    table.add_row("target remove <target>", "Remove a target")
    table.add_row("target delete <target>", "Remove a target")

    table.add_row("whois", "Run a WHOIS lookup against the active target")

    table.add_row("exit", "Exit ProtoRecon")
    table.add_row("quit", "Exit ProtoRecon")

    console.print(table)

#Command and call to function

def get_commands():
    return {
        "help": show_commands,
        "clear": clear_command,
        "cls": clear_command,
        "banner": banner_command,
        "sherlock": sherlock_command,
        "workspace": workspace_command,
        "target": target_command,
        "whois": whois_command,

    }