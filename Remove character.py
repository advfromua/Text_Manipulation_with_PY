print("Please input a single character you need to remove from txt file: ")
x = input()

print("Please provide for a txt file directory in the following format: C:\downloads\mytext.txt")
y = input()

with open(y) as f:
    line = f.read()

res_str = line.replace(x, '')

with open(y, mode='w') as p:
    p.write(res_str + "\n")
    p.close()