#This function relies on the sherlock file. it will search for it, run it, and display the response in ProtoRecon

#imports
import shutil
import subprocess
 
def sherlock_installed(): #lets check and make sure sherlock is even installed
    return shutil.which("sherlock") is not None

def run_sherlock(): #if sherlock is installed run it
    command = ["sherlock", username, "--print-found"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=90,
    )

    return result.stdout, result.stderr, result.returncode