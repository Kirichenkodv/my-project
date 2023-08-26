command_list = ["камень", "ножницы", "бумага", "ящерица","Спок"]
timur = input()
ruslan = input()
def command(command_list, name):
    for i, c in enumerate(command_list):
        if c == name:
            return i 

print(command(command_list, timur))
print(command(command_list, ruslan))


