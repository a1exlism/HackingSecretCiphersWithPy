msg = input()
i = len(msg) - 1
reversedMsg = ''
while i > -1:
    reversedMsg += msg[i]
    i -= 1

print(reversedMsg)
