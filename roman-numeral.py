object = {'I':1,
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000,
'IV': 4,
'IX': 9,
'XC': 90,
'CD': 400,
'CM': 900
}

def roman_to_int(s):
    arr = []
    for i, char in enumerate(s):
        curr = object[s[i]]
        prev = object[s[i-1]]

        if ((curr == 5 and prev ==1) or (curr == 50 and prev ==10) or (curr == 500 and prev ==100)):
            curr *= .6
        elif ((curr == 10 and prev ==1) or (curr == 100 and prev == 10) or (curr == 1000 and prev == 100)):
            curr *= .8

        arr.append(curr)

    total = sum(arr)
    print(total)
    return total



roman_to_int('III')
roman_to_int('IV')
roman_to_int('V')
roman_to_int('LVIII')
roman_to_int('II')