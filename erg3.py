low="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowlist=list(low)
upperlist=list(upper)
text=raw_input("Pliktrologiste to keimeno sas: ")
txt=list(text)
space=" "
keno=list(space)
output=""
for i in range(len(txt)):
    if txt[i] in lowlist:
        for j in range(len(lowlist)):
            if txt[i]==lowlist[j]:
                if j + 13 > 25:
                    output=output + lowlist[j-13]
                else:
                    output=output + lowlist[j+13]
                    
    elif txt[i] in upperlist:
        for j in range(len(upperlist)):
            if txt[i]==upperlist[j]:
                if j + 13 > 25:
                    output=output + upperlist[j-13]
                else:
                    output=output + upperlist[j+13]

    elif txt[i] in keno:
        output= output + keno[0]



print output