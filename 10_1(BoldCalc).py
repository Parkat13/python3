a = input()
dict = {}
while len(a.split())!=0:
    if a[0] == '#':
        a = input()
        continue
    if '=' in a:
        if a.split('=')[0][-1].isalnum() and len(a.split('=')[1])>=1 and a.split('=')[1][0].isalnum():
            if a[0].isalpha():
                try:
                    dict[a.split('=')[0]] = eval(a.split('=')[1],dict)
                except Exception as inst:
                    print(inst)
            else:
                print("invalid identifier '" + a.split('=')[0] + "'")
        else:
            print("invalid assignment '" + a + "'")            
    else:
        try:
            print(eval(a,dict))
        except Exception as inst:
            print(inst)
    a = input()
print()
