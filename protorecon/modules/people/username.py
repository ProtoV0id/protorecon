# calling the sherlock.py tool and running sherlock

#imports
from rich.panel import Panel 
from protorecon.tools.sherlock import sherlock_installed run_sherlock

def username_command(console, state, args):
    if len(args) <1:
        console.()