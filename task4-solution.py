annee=int(input("donnez une annee : "))
if (annee%4==0 and annee%100!=0)or annee%400==0:
    print(f"{annee} is a leap year")
else:
    print(f"{annee} is not a leap year")
