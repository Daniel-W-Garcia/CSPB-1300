with open('new_file', 'r') as file:
    content = file.read()
    print(content)
with open('another_file.txt', 'w') as file:
    file.write("This is the content of another_file.txt")
    print('new file created')