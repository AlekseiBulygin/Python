# Boyer–Moore–Horspool algorithm
Pattern = input()
Text = input()

entries = []
d = {}
offset = len(Pattern)
for i in range(len(Pattern) - 2, -1, -1):  # find the offset for each character in the Pattern from the end
    if Pattern[i] not in d:
        d[Pattern[i]] = offset - i - 1

i = 0
while i + offset <= len(Text):
    flag = 0  # change this flag if equality break not on last characters
    for ch in range(offset-1, -1, -1):
        if Pattern[ch] != Text[ch + i] and flag == 0:
            if Text[ch + i] in d:
                i += d[Text[ch + i]]
            else:
                i += offset
            break
        elif Pattern[ch] != Text[ch + i] and flag != 0:
            i += d[Pattern[ch]]
            break
        flag = 1
    else:
        entries.append(i)
        i += 1

print(*entries)
