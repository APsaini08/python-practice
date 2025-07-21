print("Welcome to the temprature Converter")
print("Enter the value in a formate like - (10F-> 10 ferhanite,C-> celcius,K->kelvin)")
resultTemp = input("Enter the unit in which you have to convert it into like (C->Celcius,F->Fehranite,K->Kelvin):->").lower()
temp = input("Ente the temprature:-").replace(" ","").lower()
if(len(temp)==0):
    print("Error:Input is empty")
    exit()
if(len(temp)==1 or temp[-1] not in ('c','f','k')):
    print("Error:Temprature is not mentioned")
    exit()
if(temp[-1] in ('c','f','k')):
    val = float(temp[:-1])
    if(resultTemp == temp[-1]):
        print("= "+temp)
    elif( temp[-1]=='c'):
        if(resultTemp == 'k'):
            print(str(val+273) + " K")
        if(resultTemp == 'f'):
            print(str(val*9/5+32 )+ " F")
    elif(temp[-1] == 'k'):
        if(resultTemp == "c"):
            print(str(val-273) +" C")
        if(resultTemp == 'f'):
            print(str((val-273)*9/5+32) +" F")
    elif(temp[-1] == 'f'):
        if(resultTemp == 'c'):
            print(str((val-32)/1.8 )+ "C")
        if(resultTemp == 'k'):
            print(str((val-32)/1.8+273 )+ "K")