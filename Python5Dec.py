#1st
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=0
for x in range(a, b+1):
    c+=x
print("Here's the sum: ",c)

#2nd
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a%b==0:
    print("Well yes, one number surely does divide another, it is infact", b, "which eats", a, "completely without leaving any crumbs")
elif b%a==0:
    print("Well yes, one number surely does divide another, it is infact", a, "which eats", b, "completely without leaving any crumbs")
else:
    print("None of the numbers are hungry enough to eat each other completely, #no_to_cannibalism")

#3rd
import math
rn=int(input("gib the diameter: "))
area=(math.pi*rn**2)/4
perimeter=math.pi*rn
print("The big fat circle (or small but fat indeed) wastes", round(area,2), "sq. units of area and", round(perimeter,2), "units of perimeter")

#4th
fact=int(input("Dear user, you are requested to kindly lend this program a number from the fragment of your imagination for it to showcase how efficiently it can find its factorial: "))
res=1
for x in range(1,fact+1):
    res*=x
print("And here you go, the factorial of", fact, "is", res)

#5th
for x in range(1,6):
    for y in range(1,x+1):
        print(y, end="")
    print("")
print(":)")




