# creating and storing targets
from rich.panel import Panel

from rich.panel import Panel


def resolve_selection(items, value):

    # Accepts either a name or a numbered selection.
    # Example:
    #     target aim example.com
    #     target aim 2


    if value.isdigit():
        index = int(value) - 1

        if index < 0 or index >= len(items):
            return None

        return items[index]

    if value in items:
        return value

    return None

def target_command(console, state, args):
    # If no argument is given, show the active target.
    if not args:
        if state.target is None:
            console.print("[yellow][!][/yellow] No active target selected.")
        else:
            console.print(f"[green][+][/green] Active target: [bold]{state.target}[/bold]")
        return

    action = args[0].lower()

    # List all targets
    if action == "list":
        if not state.targets:
            console.print("[yellow][!][/yellow] No targets added yet.")
            return

        target_text = ""

        for index, target in enumerate(state.targets, start=1):
            marker = "*" if target == state.target else " "
            target_text += f"{index}. {marker} {target}\n"

        console.print(
            Panel.fit(
                target_text.rstrip(),
                title="[bold green]Targets[/bold green]",
                border_style="green",
            )
        )
        return

    # Add a new target
    elif action == "add":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: target add <target>")
            return

        target = args[1].lower()

        if target in state.targets:
            console.print(f"[yellow][!][/yellow] Target already exists: [bold]{target}[/bold]")
            return

        state.targets.append(target)
        console.print(f"[green][+][/green] Target [bold]{target}[/bold] added")
        return

    # Remove a target
    elif action == "remove" or action == "delete":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: target remove <target>")
            return

        target = resolve_selection(state.targets, args[1].lower())


        if target not in state.targets:
            console.print(f"[red][!][/red] Target does not exist: [bold]{target}[/bold]")
            return

        if target == state.target:
            console.print(
                f"[red][!][/red] Must aim at another target before deleting [bold]{target}[/bold]"
            )
            return

        state.targets.remove(target)
        console.print(f"[green][+][/green] Target [bold]{target}[/bold] removed")
        return

    # Change the active target
    elif action == "aim" or action == "use":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: target aim <target>")
            return

        target = resolve_selection(state.targets, args[1].lower())

        if target is None:
            console.print(f"[red][!][/red] Target does not exist: [bold]{args[1]}[/bold]")
            return

        state.target = target
        console.print(f"[green][+][/green] Aimed at target: [bold]{state.target}[/bold]")
        return

    # Unselect target without removing it
    elif action == "unset" or action == "drop":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: target drop <target>")
            return
        
        target = resolve_selection(state.targets, args[1].lower())

        if target not in state.targets:
            console.print(f"[red][!][/red] Target does not exist: [bold]{args[1]}[/bold]")
            return
        
        state.target = None
        console.print(f"[yellow][!][/yellow] Dropped: [bold]{target}[/bold]")
        return

    else:
        console.print(f"[red][!][/red] Unknown target action: [yellow]{action}[/yellow]")