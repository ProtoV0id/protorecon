#Workspace related content
from rich.console import Console
from rich.panel import Panel

def workspace_command(console, state, args):
    if not args:
        console.print(f"[green][+][/green] Current workspace: [bold]{state.workspace}[/bold]")
        return

    action = args[0].lower()
   
    if action == "list":
    # This string will hold every workspace line.
        workspace_text = ""

        # Build the list one line at a time.
        for workspace in state.workspaces:
            marker = "*" if workspace == state.workspace else " "
            workspace_text += f"{marker} {workspace}\n"

        # Print everything in one panel.
        console.print(
            Panel.fit(
                workspace_text.rstrip(),  # Removes the final newline
                title="[bold green]Workspaces[/bold green]",
                border_style="green",
            )
        )
        return

    # Creating a new workspace. args being less than 2 forces the usage error. must have workspace create then workspace name
    elif action == "create":
        if len(args) < 2:
            console.print("[red][!][/red] Usage: workspace create <name>")
            return

        name = args[1].lower() #arg0 is the create command args1 is the actual name of the workspace

        if name in state.workspaces:
            console.print(f"[yellow][!][/yellow] Workspace already exists: [bold]{name}[/bold]")
            return

        state.workspaces.append(name)
        console.print(f"[green][+][/green] Workspace [bold]{name}[/bold] created")
        return
    
    # Deleting a workspace created by the user
    elif action == "remove" or action == "delete": #user can use remove or delete
        if len(args) < 2:
            console.print("[red][!][/red] Usage: workspace remove <name>")
            return

        name = args[1].lower()

        if name not in state.workspaces: #first if is checking if name is not in the workspace
            console.print(f"[red][!][/red] Workspace does not exist: [bold]{name}[/bold]")
            return

        if name == "default": #doesnt allow default to be deleted
            console.print("[red][!][/red] Cannot remove default workspace")
            return

        if name == state.workspace: #must move out of the workspace before deleting it
            console.print(
                f"[red][!][/red] Must move to another workspace before deleting [bold]{name}[/bold]"
            )
            return

        state.workspaces.remove(name)
        console.print(f"[green][+][/green] Workspace [bold]{name}[/bold] removed")
        return
    
    # Changing to another workspace
    elif action == "use" or action == "select": #can change workspace with use or select
        if len(args) <2:
            console.print("[red][!][/red] Usage: workspace use <name>")
            return
        
        name = args[1].lower()

        if name not in state.workspaces: #first if is checking if name is not in the workspace
            console.print(f"[red][!][/red] Workspace does not exist: [bold]{name}[/bold]")
            return
        
        state.workspace = name
        console.print(f"[green][+][/green] Switched to workspace: [bold]{state.workspace}[/bold]")
        return
        

    else:
        console.print(f"[red][!][/red] Unknown workspace action: [yellow]{action}[/yellow]")