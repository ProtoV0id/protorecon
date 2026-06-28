#Creates the banner for ProtoRecon. Easily can change the banner for updates

#imports
from rich.panel import Panel
from pathlib import Path




BANNER = r"""
██████╗ ██████╗  ██████╗ ████████╗ ██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
"""

#Counts available ProtoRecon modules.
    # Looks inside:
    #   protorecon/modules/
    # Ignores:
    #   __init__.py

def count_modules():
    

    modules_dir = Path(__file__).resolve().parent.parent / "modules"

    if not modules_dir.exists():
        return 0

    module_files = [
        file
        for file in modules_dir.rglob("*.py")
        if file.name != "__init__.py"
    ]

    return len(module_files)

def show_banner(console, state):
    module_count = count_modules()
    console.print(f"[bold green]{BANNER}[/bold green]")
    console.print("[cyan]Passive OSINT Framework[/cyan]")
    console.print("[green]Reconnaissance. Intelligence. Control.[/green]\n")

    console.print(
        Panel.fit(
            "[green]Author[/green]     : Protovoid\n"
            "[green]Version[/green]    : 0.2.0\n"
            f"[green]Workspace[/green] : {state.workspace}\n"
            f"[green]Target[/green]    : {state.target or 'None'}\n"
            f"[green]Modules[/green]    : {module_count}",
            title="[bold cyan]ProtoRecon Console[/bold cyan]",
            border_style="green",
        )
    )


    console.print("\nType [green]help[/green] to view available commands.")