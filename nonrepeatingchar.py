str = "ANKURSHARMA"
l = len(str)
flag = 0
for i in range(l):
    flag = 0
    for j in range(l):
        if str[i] == str[j] and i != j:
            flag = 1
            break
    if flag == 0:
        print("First non-repeating character is :", str[i])
        break

if flag == 1:
    print("No non-repeating character")
