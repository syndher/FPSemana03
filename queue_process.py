from collections import deque

stack1 = deque()
stack2 = deque()
palavras = input()
palavras = palavras.split(" ")
for x in palavras:
    stack1.append(x)
for i in palavras:
    stack2.append(stack1.pop())

print(stack2)

for palavra in palavras:
    if "o" in palavra:
        print(palavra)
