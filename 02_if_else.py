n = int(input())

if n%2 != 0:
    print("Weird")
elif n==2 or n==4:
    print("Not Weird")
elif n in range(6,21) and n%2 == 0:
    print("Weird")
elif n in range(21,101) and n%2 == 0:
    print("Not Weird")
            
