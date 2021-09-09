print('Please provide with txt file directory: ')
x = input()

print("Please type a digit you need to add to each line: ")
y = input()



with open(x, 'r') as f:
    char = ''
    for line in f:
        char += line.strip()+ f"{y} \n"
    f.close()

with open(x, 'w') as p:
    p.write(char)
    p.close()
