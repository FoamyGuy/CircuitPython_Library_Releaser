import subprocess

#result = subprocess.check_output(['gh', 'release', 'list', '-L', '1', '|', 'awk', '2'])
result = subprocess.getoutput("git log -1 --pretty='format:%cd' --date=format:'%Y-%m-%dT%H:%M:%SZ'")



print(f"last commit: {result}")