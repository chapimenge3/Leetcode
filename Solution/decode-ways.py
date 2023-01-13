def numDecodings(s: str):
    if s[0] == '0' or "00" in s:
        return 0
    
    st = list()
    
    first = ""
    for i in range(len(s)):
        if s[i] == '0':
            continue
        letter = s[i]
        if i < len(s) - 1 and s[i+1] == '0':
            letter += s[i+1]
        
        first += f"{letter},"

    first = first.rstrip(',')

    for i in range(1, len(s)):
        num = s[i-1] + s[i]
        if s[i] == '0' and len(st):
            st.pop()

        if not num.startswith('0') and int(num) <= 26 and num not in first:
            st.append(num)
    print(st)
    tmp = 1 if len(st) > 2 else 0
    return 1 + len(set(st)) + tmp


num = input()

print(numDecodings(num))
 