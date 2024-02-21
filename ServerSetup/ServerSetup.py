# Runs out SetUp.txt
import subprocess

with open("SetUp.txt", "r") as fin:
    commands = fin.readlines()

    for command in commands:
        subprocess.run(command.split(" "))
