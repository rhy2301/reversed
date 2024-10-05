N = int(input())

for i in range(1,N+1):
    line = input()
    words = line.split()

    stack=[]
    for word in words:
        stack.append(word)

    reverse =[]
    while stack:
        reverse.append(stack.pop())


    print(f"Case #{i}: {' '.join(reverse)}")