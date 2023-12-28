command = "/add 31.12.2023 Задача 1"

splitted_command = command.split(maxsplit=2)
print(splitted_command)
date = splitted_command[1]
task = splitted_command[2]

print(date, task)