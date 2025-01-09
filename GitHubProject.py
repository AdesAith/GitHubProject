# Gib alle Zahlen von 1 - 100 aus

#i = 1
#while (i<101):
#    print (i)
#    i = i+1

# test
# Ersetze alle Zahlen, die durch 3 teilbar sind, durch "digital"

#n = 1
#while (n<=100):
#    if(n%3==0):
#        print("digital")
#    else: print(nondigital)
#    n = n+1

#m = 1
#while(m<=100):
#    if(m % 5==0):
#        print("history")
#    else:
#        print(m)
#    m=m+1

#q = 0

#while q < 100:
#    q+= 1
#    if(q%15 == 0):
#        print("digital history")
#    elif (q%5 ==0):
#        print("history")
#    elif (q%3 == 0):
#        print("digital")
#    else:
#        print(q)

with open("persons.txt", mode="r", encoding="utf-8") as f:
    print(f.readline()[3])
    print(f.readline()[7])
3 5
