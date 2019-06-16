# Dependencies
import sys, subprocess

# Main Process
try:
    batch_config_path = sys.argv[1]
except:
    batch_config_path = "static/batch_config.txt"
batch_document = open(batch_config_path, "r", encoding="utf8").read()
commands = []
for post in batch_document.split("\n"):
    command = "py main.py {}".format(command)
    commands.append(command)
command = commands.join(" & ")
subprocess.call(command)
exit()
