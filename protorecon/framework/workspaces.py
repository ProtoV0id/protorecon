# Workspace related content
from rich.panel import Panel


def resolve_selection(items, value):
    """
    Accepts either a name or a numbered selection.

    Example:
        workspace use default
        workspace use 1
    """

    if value.isdigit():
        index = int(value) - 1

        if index < 0 or index >= len(items):
            return None

        return items[index]

    if value in items:
        return value

    return None


def workspace_command(console, state, args):
    if not args:
        console.print(f"[green][+][/green] Current workspace: [bold]{state.workspace}[/bold]")
        return

    action = args[0].lower()

    if action == "list":
        workspace_text = ""

        for index, workspace in enumerate(state.workspaces, start=1):
            marker = "*" if workspace == state.workspace else " "
            workspace_text += f"{index}. {marker} {workspace}\n"

        console.print(
            Panel.fit(
                workspace_text.rstrip(),
                title="[bold green]Workspaces[/bold green]",
                border_style="green",
            )
        )
        return

    elif action == "create":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: workspace create <name>")
            return

        name = args[1].lower()

        if name in state.workspaces:
            console.print(f"[yellow][!][/yellow] Workspace already exists: [bold]{name}[/bold]")
            return

        state.workspaces.append(name)
        console.print(f"[green][+][/green] Workspace [bold]{name}[/bold] created")
        return

    elif action == "remove" or action == "delete":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: workspace remove <name or number>")
            return

        name = resolve_selection(state.workspaces, args[1].lower())

        if name is None:
            console.print(f"[red][!][/red] Workspace does not exist: [bold]{args[1]}[/bold]")
            return

        if name == "default":
            console.print("[red][!][/red] Cannot remove default workspace")
            return

        if name == state.workspace:
            console.print(
                f"[red][!][/red] Must move to another workspace before deleting [bold]{name}[/bold]"
            )
            return

        state.workspaces.remove(name)
        console.print(f"[green][+][/green] Workspace [bold]{name}[/bold] removed")
        return

    elif action == "use" or action == "select":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: workspace use <name or number>")
            return

        name = resolve_selection(state.workspaces, args[1].lower())

        if name is None:
            console.print(f"[red][!][/red] Workspace does not exist: [bold]{args[1]}[/bold]")
            return

        state.workspace = name
        console.print(f"[green][+][/green] Switched to workspace: [bold]{state.workspace}[/bold]")
        return

    else:
        console.print(f"[red][!][/red] Unknown workspace action: [yellow]{action}[/yellow]")