from socket import *
import random
import datetime
import sys
import threading
from random import randint
import string
from time import localtime, strftime



print("----------------------------------Mire se vini ne FIEK UDP SERVER --------------------------------------")
print("----------------------------------Fakulteti i Inxhinierise Elektrike dhe Kompjuterike--------------------")
print("\n")


SRVPORT = 14000


serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('', SRVPORT))


print('Serveri startoi ne localhost me IP adrese: '+str(gethostbyname(gethostname()))+" ne portin: "+str(SRVPORT))
print('Serveri eshte i gatshem te pranoj kerkesa...')
print("\n")

print("Serveri do te ktheje te dhenat per klientin me poshte")



def IP(address):
    return str(address[0])

def NRPORTIT(address):
    return str(address[1])


def NUMERO(str):

    Znum = 0  #counteri i zanoreve
    Bnum = 0    #counteri i bashketingelloreve


    str = str.lower()
    for i in range(0, len(str)):
        if str[i] in ('a', "e", "i", "o", "u"):
            Znum +=  1;

        elif (str[i] >= 'a' and str[i] <= 'z'):
            Bnum +=  1;
    return Znum, Bnum


def ANASJELLTAS(teksti):
    s = teksti.strip()
    reverse = ""
    indeksi = len(s)
    while indeksi > 0:
        reverse += s[indeksi - 1]
        indeksi = indeksi - 1
    return reverse


def PALINDROM(string):
    if (string == string[::-1]):
        return "Eshte Palindrom"
    else:
        return "Nuk eshte Palindrom"


def GCF(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return str(x)


def KOHA():
    return strftime("%Y-%m-%d %H:%M:%S ", localtime())


def LOJA():
        numrat = []
        while len(numrat) <= 5:
            nr = randint(1,35)
            if nr in numrat:
                continue
            else:
                numrat.append(nr)
        numrat.sort()
        return ' '.join(str(v) for v in numrat)


def KONVERTO(operacioni, rezultati):
    
    rezultati = float(rezultati)

    if operacioni == "cmNeInch":
        return str(rezultati * 0.393701)
    elif operacioni == "inchNeCm":
        return str(rezultati * 2.52)
    elif operacioni == "mileNeKm":
        return str(rezultati * 1.609)
    elif operacioni == "kmNeMiles":
        return str(rezultati / 1.609)
    
    else:
        return "Keni gabuar operacionin"

# metodat shtese

def UPPLOWCHAR(s):
    d = {"u": 0, "l": 0}
    u = 0;
    l = 0;
    for c in s:
        if c.isupper():
            u += 1
        elif c.islower():
            l += 1
    return u, l

def RRITE(teksti):
    type(teksti)
    return teksti.lower().upper()

def ROCK_PAPER_SCISSORS(Zgj_jone):
    Zgj_jone = Zgj_jone.lower()
    if Zgj_jone == 'rock':
        zgjedhja = 1
    elif Zgj_jone == 'paper':
        zgjedhja = 2
    elif Zgj_jone == 'scissors':
        zgjedhja = 3
    else:
        return "Keni gabuar gjate shtypjes se opsionit! Vendos rock, paper apo scissors nese deshironi te vazhdoni"

    Pc_zgj = random.randint(1, 3)

    if Pc_zgj == 1:
        comp_Zgj_jone = 'Rock'
    elif Pc_zgj == 2:
        comp_Zgj_jone = 'paper'
    else:
        comp_Zgj_jone = 'scissor'

    if (zgjedhja == 1 and Pc_zgj == 3) or (zgjedhja == 2 and Pc_zgj == 1) or (zgjedhja == 3 and Pc_zgj == 2):
        return "Ju keni fituar. Kompjuteri zgjodhi " + comp_Zgj_jone
    elif (zgjedhja == Pc_zgj):
        return "Barazim. Edhe kompjuteri zgjodhi " + comp_Zgj_jone
    else:
        return "Fitoi kompjuteri . Kompjuteri zgjodhi " + comp_Zgj_jone


def CILINDRI(lartesia, radius):
     pi=22/7
     volume = pi * radius * radius * lartesia
     sur_area = ((2*pi*radius) * lartesia) + ((pi*radius**2)*2)
     return volume, sur_area




while 1==1:
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper()!="EXIT" and str(kerkesa.decode())!="":
            
            
            kerkesa, clientAddress = serverSocket.recvfrom(128)
            kerkesaStr = str(kerkesa.decode()).strip()
            kerkesaArray = kerkesaStr.split(' ')
            kerkesaArray[0] = kerkesaArray[0].upper()
           
            # metoda IP
            if kerkesaArray[0]=="IP":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("IP adresa juaj si klient eshte: "+IP(clientAddress)).encode(), clientAddress)
                    print(("Klienti ka kerkuar metoden IP dhe IP e tij eshte: "+IP(clientAddress)))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    serverSocket.sendto("Kerkesa juaj eshte gabim ose nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print(" Keni gabuar, shiko perseri ...")
            
             # metoda NRPORTIT
            elif kerkesaArray[0]=="NRPORTIT":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Numri i portit tuaj eshte: "+NRPORTIT(clientAddress)).encode(), clientAddress)
                    print(("Klienti ka kerkuar metoden NRPORTI dhe PORTI i tij eshte: "+NRPORTIT(clientAddress)))
                    print("-----------------------------------------------------------------------------------------")

                else:
                    serverSocket.sendto("Kerkesa juaj eshte gabim ose nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")
  
               #metoda NUMERO
            elif kerkesaArray[0]=="NUMERO":
                if len(kerkesaArray) == 2:
                    var1, var2 = NUMERO(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    serverSocket.sendto(("Numri i zanoreve eshte : " + var1 + " Numri i bashtinglloreve " + var2).encode(),clientAddress)
                    print(("Numri i zanoreve dhe i bashtinglloreve eshte : " + var1 + " zanore dhe " + var2 + " bashketingellore"))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")   
                    
                    #metoda ANASJELLTAS
            elif kerkesaArray[0]=="ANASJELLTAS":
                if len(kerkesaArray) == 2:
                    serverSocket.sendto(("Fjala e kthyer mbrapsht eshte : " + ANASJELLTAS(kerkesaArray[1])).encode(),clientAddress)
                    print(("Klienti ka kerkuar metoden Anasjelltas dhe fjala e kthyer mbrapsht eshte: " + ANASJELLTAS(kerkesaArray[1])))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(clientAddress), clientAddress)
                    print("Keni gabuar, shiko perseri ...")

                    #metoda PALINDROM
            elif kerkesaArray[0]=="PALINDROM":
                if len(kerkesaArray) == 2:
                    serverSocket.sendto(("Fjala e dhene eshte : " + PALINDROM(kerkesaArray[1])).encode(), clientAddress)
                    print(("Klienti ka kerkuar metoden Palindrom dhe fjala e dhene: " + PALINDROM(kerkesaArray[1])))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")

                  # metoda KOHA
            elif kerkesaArray[0]=="KOHA":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Koha e tanishme eshte: " + KOHA()).encode(), clientAddress)
                    print(("Koha e tanishme eshte: " + KOHA()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte gabim ose nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")
            # metoda LOJA
            elif kerkesaArray[0]=="LOJA":
                if len(kerkesaArray) == 1:
                    serverSocket.sendto(("Rezultati nga loja: " + LOJA()).encode(), clientAddress)
                    print(("Rezultati nga loja: " + LOJA()))
                else:
                    serverSocket.sendto("Kerkesa juaj eshte gabim ose nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")

             #metoda GCF
            elif kerkesaArray[0]=="GCF":
                if len(kerkesaArray) == 3:
                    serverSocket.sendto(("GCF eshte : " + GCF(kerkesaArray[1],kerkesaArray[2])).encode(), clientAddress)
                    print(("GCF eshte : " + GCF(kerkesaArray[1],kerkesaArray[2])))
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(clientAddress), clientAddress)
                    print("Keni gabuar, shiko perseri ...")
  
            # metoda KONVERTO
            elif kerkesaArray[0] == "KONVERTO":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray) > 3 or len(kerkesaArray) < 3:
                    serverSocket.sendto( ("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!").encode(), clientAddress)
                    print("GABIM / ERROR")
                else:
                    Konvertimi = str(kerkesaArray[1]).lower().split("ne")
                    pergjigja = kerkesaArray[2] + " " + str(Konvertimi[0]) + " jane te barabarte me " + KONVERTO(
                        str(kerkesaArray[1]), kerkesaArray[2]) + " " + str(Konvertimi[1])
                    serverSocket.sendto(str(pergjigja).encode(),clientAddress)
                    print(pergjigja)
                    print("---------------------------------------------------------------------------")

            # metodat shtese
            # metoda UPLOWCHAR
            elif kerkesaArray[0] == "UPPLOWCHAR":
                if len(kerkesaArray) == 2:
                    var1,var2 = UPPLOWCHAR(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    serverSocket.sendto(("Jane: "+ var1 +" shkronja te medha dhe "+ var2 +" shkronja te vogla").encode(),clientAddress)
                    print(("Numri i shkronjave te medha dhe te vogla eshte:"+ var1 + " te medha dhe " + var2 + " te vogla"))

                   
            elif kerkesaArray[0]=="ROCK_PAPER_SCISSORS":
                if len(kerkesaArray) == 2:
                    serverSocket.sendto((ROCK_PAPER_SCISSORS(kerkesaArray[1])).encode(), clientAddress)
                    print(("Klienti ka kerkuar metoden ROCK_PAPER_SCISSORS"))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")


            elif kerkesaArray[0]=="RRITE":
                if len(kerkesaArray) == 2:
                    serverSocket.sendto(("Fjala e kthyer ne Shkronja te medha eshte: "  + RRITE(kerkesaArray[1])).encode(), clientAddress)
                    print(("Klienti ka kerkuar metoden RRITE dhe fjala e kthyer ne shkronja te medha eshte eshte: " + RRITE(kerkesaArray[1])))
                    print("-----------------------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                    print("Keni gabuar, shiko perseri ...")



            elif kerkesaArray[0] == "CILINDRI":
                if len(kerkesaArray) == 2:
                    connectionSocket.sendto((CILINDRI(kerkesaArray[1])).encode(),clientAddress)
                    print(("Klienti ka kerkuar metoden CILINDRI dhe fjala e kthyer ne shkrnja te medha eshte eshte: " + CILINDRI(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.sendto("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode(),clientAddress)
                    print("Keni gabuar, shiko perseri ...")

        else:
                serverSocket.sendto("Kerkesa juaj eshte gabim ose nuk ekziston, ju lutem provoni perseri!".encode(), clientAddress)
                print("Keni gabuar, shiko perseri ...!")



    except Exception as mesazhi:
        print("\n Keni gabuar, shiko perseri ...: ")
        print(str(mesazhi))
