from collections import deque
palavras = input()
stack1 = deque(palavras.split())
for x in palavras:
    stack1.append(x)
print(stack1)

for palavra in palavras:
    if "o" in palavra:
        print(palavra)
