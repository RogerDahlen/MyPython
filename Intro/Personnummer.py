

def even(number):
    return number % 2

def siffersumma(number):
    if number < 10:
        return number
    if number < 100:
        aaa = str(number)
        return int(aaa[0]) + int(aaa[1])

pnr = input("Ange personnummer utan sista kontrollsiffran \(utan -\): ")

sum = 0
for i in range(9):
    if even(i):
        delsumma = 1 * int(pnr[i])
    else:
        delsumma = 2 * int(pnr[i])
    sum = sum + siffersumma(delsumma)

kontrollsumma = 10 - sum%10
print("kontrollsumman är " + str(kontrollsumma))
