with open("C:/Users/32573/Desktop/doubantop250.txt", "r", encoding="utf-8") as f:
    content = ""
    for i in range(0, 50, 1):
        content += f.readline()
    count = 0
    for i in content:
        if i == "-":
            count += 1
    print(count)


