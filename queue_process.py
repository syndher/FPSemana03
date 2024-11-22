from collections import deque

stack1 = deque()
palavras = input()
palavras = palavras.split(" ")
for x in palavras:
    stack1.appendleft(x)

print(stack1)

for palavra in palavras:
    if "o" in palavra:
        print(palavra)
