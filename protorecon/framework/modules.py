#listing modules and what they do

#imports
from rich.table import Table 
from protorecon.framework.ui import count_modules

def show_modules(console, state, args):
    modules = count_modules()
    table = Table(
        title=(f"Available Modules: {modules}"),
        border_style="green",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Module", style="green")
    table.add_column("Category", style="cyan")
    table.add_column("Description", style="white")

    table.add_row("whois", "web", "Domain WHOIS lookup")
    table.add_row("sherlock", "person", "Sherlock username search")

    console.print(table)
   