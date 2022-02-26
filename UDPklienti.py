from socket import *

print("-------------------------------FIEK_UDP_KLIENT----------------------------------------------")
print("--------------------------------Lenda Rrjeta Kompjuterike - Profesoret: Blerim Rexha dhe Haxhi Lajqi")
serverName = '127.0.0.1'  #127.0.0.1 ose mund te shkruanii localhost
SRVPORT = 14000

s = socket(AF_INET, SOCK_DGRAM)

print("\n")

print("Jeni lidhur ne serverin ",serverName," ne portin ",SRVPORT)


print("\nZgjedhni ndonjeren nga metodat: ")
print("-IP\n-NRPORTIT\n-NUMERO [hapsire] teksti\n-ANASJELLTAS [hapsire] teksti \n-PALINDROM [hapsire] teksti\n-KOHA\n-LOJA\n-GCF [hapsire] Numri1 [hapsire] Numri2\n-KONVERTO [Hapesire] operacioni Hapesire NumriNe:cmNeInch,inchNeCm,kmNeMiles,mileNeKm\n-UPPLOWCHAR [hapesire] teksti\n-ROCK_PAPER_SCISSORS [hapesire] opsioni\n-RRITE teksti\n\n")


print("Nese deshironi te ndalni programin, shkruani ne console EXIT")

while 1==1: #ketu e kemi bere nje while loop dmth while true(qe i bie 1==1 eshte true)
    try:
        kerkesa = input('Shkruani kerkesen dhe opsionet nese ajo metode ka: ') 
        if kerkesa!="" and kerkesa.upper()!="EXIT":
            
            s.sendto(str(kerkesa).encode(), (serverName, SRVPORT))
        else:
            break
        
        data, serverAddress = s.recvfrom(128)
        print('Te dhenat e pranuara nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------------\n")
    except Exception as mesazhi:
        print(str(mesazhi))
        break

s.close()   




