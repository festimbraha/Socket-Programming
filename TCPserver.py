from socket import *
import random
import datetime
import math
import sys
import threading
import string
from time import localtime, strftime
from random import randint



print("----------------------------------Mire se vini ne FIEK TCP SERVER --------------------------------------")
print("----------------------------------Fakulteti i Inxhinierise Elektrike dhe Kompjuterike--------------------")
print("\n")

SRVPORT = 14000
serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind(('', SRVPORT))

print('Serveri eshte ne LocalHost me IP: ' + str(gethostbyname(gethostname())) + " ne portin e dhene: " + str(
    SRVPORT))


serverSocket.listen(5)

print('Serveri eshte i gatshem te pranoj kerkesa...')
print("\n")

print("Serveri do te ktheje te dhenat per klientin me poshte")
print("\n")


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


def NUMERO(teksti):
    zan = 0
    bashk = 0
    for z in teksti:
        if z in 'aeëiouyAEËIOUY':
            zan = zan + 1
        elif z in "bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ":
            bashk = bashk + 1
    x = "Zanore :" + str(zan)
    y = "Bashketingellore : " + str(bashk)
    return [x, y]


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

def KOHA():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


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


def GCF(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return str(x)




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

def ROCK_PAPER_SCISSORS(choice_name):
    choice_name = choice_name.lower()
    if choice_name == 'rock':
        choice = 1
    elif choice_name == 'paper':
        choice = 2
    elif choice_name == 'scissors':
        choice = 3
    else:
        return "Keni shtypur opsion jo-valid. Shtyp rock , paper apo scissors per te vazhduar"

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    if (choice == 1 and comp_choice == 3) or (choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2):
        return "Ju keni fituar. Kompjuteri zgjodhi " + comp_choice_name
    elif (choice == comp_choice):
        return "Barazim. Edhe kompjuteri zgjodhi " + comp_choice_name
    else:
        return "Fitoi kompjuteri . Kompjuteri zgjodhi " + comp_choice_name






#def MATH(a,b,c):
#   global discriminant   
#if(discriminant > 0):
#    root1 = (-b + math.sqrt(discriminant) / (2 * a))
#    root2 = (-b - math.sqrt(discriminant) / (2 * a))
#    print("two distinct real roots exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
#elif(discriminant == 0):
#    root1 = root2 = -b / (2 * a)
#    print("two equal and real roots exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
#elif(discriminant < 0):
#    root1 = root2 = -b / (2 * a)
#    imaginary = math.sqrt(-discriminant) / (2 * a)
#    print("two distinct complex roots exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))




def newClient(connectionSocket, addr):
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper() != "EXIT" and str(kerkesa.decode()) != "":
            
            kerkesa = connectionSocket.recv(128)
            kerkesaStr = str(kerkesa.decode()).strip()
            kerkesaArray = kerkesaStr.split(' ')
            kerkesaArray[0] = kerkesaArray[0].upper()

            #Metoda IP
            if kerkesaArray[0] == "IP":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("IP adresa juaj si klient eshte: " + IP(addr)).encode())
                    print(("Klienti ka kerkuar metoden IP dhe IP e tij eshte: " + IP(addr)))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")
            #Metoda NRPORTI
            elif kerkesaArray[0] == "NRPORTIT":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Numri i portit tuaj eshte: " + NRPORTIT(addr)).encode())
                    print(("Klienti ka kerkuar metoden NRPORTI dhe PORTI i tij eshte: " + NRPORTIT(addr)))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")
                 # Metoda NUMERO
            elif kerkesaArray[0] == "NUMERO":
                if len(kerkesaArray) == 2:
                    var1, var2 = NUMERO(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    connectionSocket.send(
                        ("Numri i zanoreve eshte: " + var1 + " Numri i bashtinglloreve " + var2).encode())
                    print(("Numri i zanoreve dhe i bashtinglloreve eshte : " + var1 + " " + var2))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")

             # metoda ANASJELLTAS
            elif kerkesaArray[0] == "ANASJELLTAS":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala e kthyer mbrapsht eshte : " + ANASJELLTAS(kerkesaArray[1])).encode())
                    print(("Klienti ka kerkuar metoden Anasjelltas dhe fjala e kthyer mbrapsht eshte: " + ANASJELLTAS(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")


            # metoda PALINDROM
            elif kerkesaArray[0] == "PALINDROM":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala e dhene: " + PALINDROM(kerkesaArray[1])).encode())
                    print(("Klienti ka kerkuar metoden Palindrom dhe fjala e dhene: " + PALINDROM(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")
            #Metoda KOHA
            elif kerkesaArray[0] == "KOHA":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Koha tani per momentin eshte: " + KOHA()).encode())
                    print(("Klienti ka kerkuar metoden KOHA dhe koha momentale eshte:" + KOHA()))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")
           #Metoda LOJA
            elif kerkesaArray[0] == "LOJA":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Rezultatet nga loja: " + LOJA()).encode())
                    print(("Klienti ka kerkuar metoden LOJA dhe rezultati eshte:" + LOJA()))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")
            # metoda GCF
            elif kerkesaArray[0] == "GCF":
                if len(kerkesaArray) == 3:
                    connectionSocket.send(("GCF eshte : " + GCF(kerkesaArray[1], kerkesaArray[2])).encode())
                    print(("Klienti ka kerkuar metoden GCF dhe GCF e dy numrave eshte:" + GCF(kerkesaArray[1], kerkesaArray[2])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode(clientAddress),
                        clientAddress)
                    print("Keni gabuar, shiko perseri ...")
            #Metoda KONVERTO
            elif kerkesaArray[0] == "KONVERTO":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray) > 3 or len(kerkesaArray) < 3:
                    connectionSocket.send( ("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!").encode())
                    print("Keni gabuar, shiko perseri ...")
                else:
                    Konvertimi = str(kerkesaArray[1]).lower().split("ne")
                    pergjigja = kerkesaArray[2] + " " + str(Konvertimi[0]) + " jane te barabarte me " + KONVERTO(
                        str(kerkesaArray[1]), kerkesaArray[2]) + " " + str(Konvertimi[1])
                    connectionSocket.send(str(pergjigja).encode())
                    print(pergjigja)
                    print("---------------------------------------------------------------------------")

           
          
            # metodat shtese
       
            elif kerkesaArray[0] == "UPPLOWCHAR":
                if len(kerkesaArray) == 2:
                    var1,var2 = UPPLOWCHAR(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    connectionSocket.send(("Jane "+ var1 +" shkronja te medha dhe "+ var2 +" shkronja te vogla").encode())
                    print(("Numri i shkronjave te medha dhe i shkronjave te vogla eshte : " + var1 + " " + var2))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...!")



             # metoda ROCK_PAPER_SCISSORS
            elif kerkesaArray[0] == "ROCK_PAPER_SCISSORS":
                if len(kerkesaArray) == 2:
                    connectionSocket.send((ROCK_PAPER_SCISSORS(kerkesaArray[1])).encode())
                    print((ROCK_PAPER_SCISSORS(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden  apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")


            # metoda RRITE
            elif kerkesaArray[0] == "RRITE":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala e kthyer ne Shkronja te medha eshte: " + RRITE(kerkesaArray[1])).encode())
                    print(("Klienti ka kerkuar metoden RRITE dhe fjala e kthyer ne shkrnja te medha eshte eshte: " + RRITE(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")



            elif kerkesaArray[0] == "CILINDRI":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala e kthyer ne Shkronja te medha eshte: " + CILINDRI(kerkesaArray[1])).encode())
                    print(("Klienti ka kerkuar metoden RRITE dhe fjala e kthyer ne shkrnja te medha eshte eshte: " + CILINDRI(kerkesaArray[1])))
                    print("---------------------------------------------------------------------------")
                else:
                    connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                    print("Keni gabuar, shiko perseri ...")

          
            
            else:
                connectionSocket.send("Keni gabuar metoden apo ajo nuk ekziston. Provoni Perseri!".encode())
                print("Keni gabuar, shiko perseri ...!")
#-------------------------------------------------------------------------------------------------------------------------

        
        connectionSocket.close()
    except Exception as mesazhi:
        print("\n Keni gabuar, shiko edhe njehere kerkesen: ")
        print(str(mesazhi))
        connectionSocket.close()

while 1==1:
    
    connectionSocket, addr = serverSocket.accept()
    print('Klienti me IP-ne %s dhe me numer te portit %s eshte lidhur me server' % (addr))

    threading._start_new_thread(newClient, (connectionSocket, addr))
