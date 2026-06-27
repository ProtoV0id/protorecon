#Whois search module

#imports
from rich.panel import Panel

try:
    import whois
except ImportError:
    whois = None

def whois_command(console, state ,args): #Running a whois against active target

    if whois is None:
        console.print("[red][!][/red] Missing dependency: python-whois")
        console.print("Install it with: [bold]pip install python-whois[/bold]")
        return

    if state.target is None:
        console.print("[red][!][/red] No target selected.")
        console.print("Use: [bold]target aim <target>[/bold]")
        return
    

    target = state.target

    console.print(f"[green][+][/green] Running WHOIS lookup for [bold]{target}[/bold]")

    try:
        result = whois.whois(target)
    except Exception as error:
        console.print(f"[red][!][/red] WHOIS lookup failed: {error}")
        return

    output = f"""
        Domain Name: {result.domain_name}
        Registrar: {result.registrar}
        WHOIS Server: {result.whois_server}
        Updated Date: {result.updated_date}
        Creation Date: {result.creation_date}
        Expiration Date: {result.expiration_date}
        Name Servers: {result.name_servers}
        Status: {result.status}
        DNSSEC: {result.dnssec}
        """

    console.print(
        Panel.fit(
            output.strip(),
            title=f"[bold green]WHOIS: {target}[/bold green]",
            border_style="green",
        )
    )