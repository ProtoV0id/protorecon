# calling the sherlock.py tool and running sherlock
# This will not accept a username typed in. must use the target add and target aim command
# useful for purposeful searches

#imports
from rich.panel import Panel 
from protorecon.tools.sherlock import sherlock_installed 
from protorecon.tools.sherlock import run_sherlock

def sherlock_command(console, state, args):
    if args:
        console.print("[red][!][/red] The Sherlock module uses the active target only.")
        console.print("Use: [bold]target add <username>[/bold]")
        console.print("Then: [bold]target aim <username> or <target number>[/bold]")
        console.print("Then run: [bold]sherlock[/bold]")
        return

    if state.target is None:
        console.print("[red][!][/red] No active target selected.")
        console.print("Use: [bold]target aim <username> or <target number>[/bold]")
        return

    username = state.target

    if not sherlock_installed():
        console.print("[red][!][/red] Sherlock is not installed or not in PATH.")
        console.print("Install Sherlock first, then try again.")
        return
    
    #for a standard output
    #console.print(f"[green][+][/green] Running Sherlock for active target: [bold]{username}[/bold]")

    console.print(f"[green][+][/green] Running Sherlock for active target: [bold]{username}[/bold]")
    with console.status("[bold amber]Searching username across sites...[/bold amber]", spinner="dots"):
        stdout, stderr, returncode = run_sherlock(username)
    

    if returncode != 0:
        console.print(f"[red][!][/red] Sherlock exited with code {returncode}")
    
    if stderr:
        console.print(
            Panel.fit(
                stderr.strip(),
                title="[red]Sherlock Errors[/red]",
                border_style="red",
            )
        )

    if stdout:
        console.print(
            Panel.fit(
                stdout.strip(),
                title=f"[bold green]Sherlock Results: {username}[/bold green]",
                border_style="green",
            )
        )
    else:
        console.print("[yellow][!][/yellow] No results returned.")