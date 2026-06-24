# imports
import typer
from rich.console import Console 
from rich.panel import Panel 

app = typer.Typer()
console = Console()

@app.command()
def banner():
    """Show Protorecon banner."""
    console.print(Panel.fit( 
        "[bold green]ProtoRecon[/bold green]\nPassive OSINT Framework",
        title="PROTOVOID"

    ))

@app.command()
def username(target: str):
    """Run a basic ussername lookup placeholder."""
    console.print(f"[green][+][/green] Running username scan for: [bold]{target}[/bold]")
    console.print(f"[yellow][!][/yellow] Username module not built yet. Humanity survives another day.")

    if __name__ == "__main__":
        app()