#Zadania;[1, 2, 3, 5, 7, 10, 14, 22, 24, 25, 27, 31, 32]

#1. Napisz skrypt, który będzie wyświetlać wszystkie 
#   kolejne dzielniki wprowadzonej liczby

try:
    liczba = int(input("Wprowadź liczbę całkowitą : "))
    for i in range(1, liczba + 1):
        if (liczba % i == 0):
            print(i)
except ValueError:
    print("To nie jest liczba całkowita")
    
#2. Korzystając z pojęcia funkcji utwórz skrypt, 
#   który będzie miał możliwość zamiany temperatury pomiędzy skalami 
#   Celsjusza i Fahrenheita (w obie strony). C = (F-32)x(5/9), F = (C*9/5)+32
        
""" Funkcja zmieniająca podaną temperaturę z Celsjusza na Fahrenheita """
def Cel2Fah(temp):
    fah = (temp * 9 / 5) + 32
    return fah

""" Funkcja zmieniająca podaną temperaturę z Fahrenheita na Celsjusza """
def Fah2Cel(temp):
    cel = (temp - 32) * (5 / 9)
    return cel

""" Wybór skali temperaturowej wejciowej, 
na tej podstawie skrypt wybiera skalę wyjciową"""
skala = input("Podaj źródłową skalę temperaturową C/F : ")

if ((skala == 'F') or (skala == 'f')):
    temp = float(input("Wprowadź temperaturę w skali Fahrenheita : "))
    print("Wrtosć temperatury w skali Celsjusza to : "+str(round(Fah2Cel(temp),1)))
elif ((skala == 'C') or (skala == 'c')):
    temp = float(input("Wprowadź temperaturę w skali Celsjusza : "))
    print("Wrtosć temperatury w skali to Fahrenheita : "+str(round(Cel2Fah(temp),1)))
else:
    print("Tej skali nie obsługujemy")
    
#3. Utwórz skrypt do zamiany kilometrów na mile i na odwrót

""" Funkcja przelicza podaną wartoć z mil na kilometry """
def Mile2Km(dist):
    km = dist * 1609.344 / 1000
    return km

""" Funkcja przelicza podaną wartoć z kilometrów na mile """
def Km2Mile(dist):
    mile = dist * 1000 / 1609.344
    return mile

""" Wczytanie jednostki wejciowej, 
na taj podstawie jes wybierana jednostka wyjciowa"""
jedn = input("Podaj źródłową jednostkę odległoci Mile/Km [m/k]: ")

if ((jedn == 'm') or (jedn == 'M')):
    dist = float(input("Wprowadź odległosć w milach : "))
    print("Odległosć w kilometrach to : "+str(round(Mile2Km(dist),1))+' [km]')
elif ((jedn == 'k') or (jedn == 'K')):
    dist = float(input("Wprowadź odległosć w kilometrach : "))
    print("Odległosć w milach to : "+str(round(Km2Mile(dist),1))+' [mile]')
else:
    print("Tej skali nie obsługujemy")

# 5. Utwórz skrypt, który będzie komunikować, 
#   czy wprowadzona liczba jest dodatnia czy nie

try:
    liczba = float(input("Wprowadż dowolną liczbę rzeczywistą : "))
    if (liczba > 0):
        print("Wprowadzono liczbę dodatnią.")
    elif(liczba < 0):
        print("Wprowadzono liczbę ujemną.")
    else:
        print("Wprowadzono zero")
except ValueError:
    print("Wprowadzona wartoć nie jest liczbą Rzeczywistą")
    

#7. Utwórz skrypt z interfejsem tekstowym, 
#   który pobierze od użytkownika zdanie i wyświetli 
#   w kolejnych wierszach litery tego zdania w odwróconej kolejności

ciag = str(input("Wpisz dowolne zdanie \n"))
""" Obliczenie długoci ciągu """
dlug = len(ciag)
wynik = ""
""" przepisanie liter zdania w odwrotnej kolejnoci z wykorzystaniem ciągu jako tablicy """
for i in range(dlug - 1, -1, -1):
    wynik = wynik + ciag[i]
print(wynik)

#10. Utwórz skrypt z interfejsem tekstowym, 
#    który przyjmie od użytkownika ile elementów 
#    chce on wprowadzić do listy, przyjmie te elementy, 
#    a następnie wyliczy: średnią i odchylenie standardowe średniej. 
#   Wykonać zadanie na dwa sposoby: poprzez utworzenie funkcji 
#   własnych obliczających średnią i odchylenie standardowe 
#   oraz korzystając z gotowych funkcji np. z pakietu numpy

import numpy, math
# Funkcja licząca rednią arytmetyczną podanej listy wartoci 
# funkcja otrzymuję 2 parametry, listę wartoci i liczbę elementów
def fSrednia(wart, liczba):
    srednia = 0
    for i in range(0, liczba):
        srednia = srednia + wart[i]
    srednia = srednia / liczba
    return srednia

# Funkcja licząca odchylenie standardowe podanej listy wartoci 
# funkcja otrzymuję 2 parametry, listę wartoci i liczbę elementów
def fOdchylSt(wart, liczba):
    srednia = fSrednia(wart, liczba)
    odchylst = 0
    for i in range(0, liczba):
        odchylst = odchylst + (srednia - wart[i]) * (srednia - wart[i])
    odchylst = math.sqrt(odchylst / liczba)
    return odchylst

# Wczytanie liczby elementów
liczba = int(input("Podaj liczbę elementów : "))
wart = []
# Pobieranie wartoci w pętli for
for i in range(1, liczba + 1):
    # Pętla while jest potrzebna w przypadku błędu przy wprowadzaniu
    while True:
        try:
            wart.append(float(input("Podaj wartoć "+str(i)+" : ")))
            break
        except:
            print("Błędna wartosć")

# obliczenie wartosci redniej
srednia = fSrednia(wart, liczba)
print("Wartoć srednia wrowadzaonego ciągu liczb to : ")
print("Funkcja własna "+str(srednia))
print("NumPy          "+str(numpy.average(wart)))
# obliczenie odchylenia standardowego
odchylst = fOdchylSt(wart, liczba)
print("Wartoć odchylenia standardowego to : ")
print("Funkcja własna "+str(odchylst))
print("NumPy          "+str(numpy.std(wart)))

#14. Utworzyć skrypt z interfejsem tekstowym, 
#   który będzie zwracać wiersz n-tego rzędu z trójkąta Pascala 
#   (użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta)

# Funkcja licząca wartosć silni podanej liczby całkowitej
def fFrational(liczba):
    silnia = 1
    for i in range(1, liczba + 1):
        silnia = silnia * i
    return silnia

# Funkcja wyliczająca wartosć dwumianu Newtona
def dwumian(ln, lk):
    silniak = fFrational(lk)
    silnian = fFrational(ln)
    silniar = fFrational(ln - lk)
    return silnian / silniak / silniar

print("program liczący n-ty wiersz trójkąta pascala ")
print("podaj numer wiersza n >= 0")
while True:
    try:
        wiersz = int(input())
        break
    except:
        print("Błędna wartosć")
rozklad = list()
if (wiersz == 0):
    # Wiersz pierwszy dla n=0
    rozklad.append(1)
elif (wiersz == 1):
    # wiersz pierwszy dla n=1
    rozklad.append(1)
    rozklad.append(1)
else:
    # wstawienie pierwszego elementu dla wiersza n > 1
    rozklad.append(1)
    for i in range(1, wiersz):
        # wyliczenie wartosci pozostałych elementów za pomocą dwumianu
        rozklad.append(int(dwumian(wiersz, i)))
    # wstawienie ostatniego elementu dla wiersza n > 1
    rozklad.append(1)
print("Współczynniki trójkąta Pascala  w wierszu "+str(wiersz))
print(rozklad)

# 22. Utwórz fukcję, która jako argument będzie przyjmować listę 
#   liczb zmiennoprzecinkowych, a jej wynikiem będzie mediana 
# (skorzystaj z metody sort działającej na standardowych listach)
import numpy, math

# funkcja wylicz wartosć srodkową podanej listy wartosci
def fMediana(wart):
    length = len(wart)
    # sortowanie listy
    wart.sort()
    if ((length % 2) == 0):
        # obliczenia dla parzystej liczby elementów
        return ((wart[int(length / 2 - 1)] + wart[int(length / 2)]) / 2)
    else:
        # obliczenie dla nieparzystej liczby elementów
        return wart[int(length / 2)]

# parzysta liczba wartosci
wart_p = [53.9, 56.4, 54.6, 53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
# nieparzysta liczba wartosci
wart_n = [53.6, 56.4, 53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]

print("Parzysta liczba pomiarów    "+str(len(wart_p)))
print("Mediana wg numpy            "+str(numpy.median(wart_p)))
print("Mediana funkcja własna      "+str(fMediana(wart_p)))
print("Nieparzysta liczba pomiarów "+str(len(wart_n)))
print("Mediana wg numpy            "+str(numpy.median(wart_n)))
print("Mediana funkcja własna      "+str(fMediana(wart_n)))

#24. Utwórz fukcję, która jako argument będzie przyjmować 
#   listę liczb zmiennoprzecinkowych, a jej wynikiem będzie 
#   odchylenie standardowe średniej
import random as rnd
import numpy 

# Funkcja licząca rednią arytmetyczną podanej listy wartoci 
# funkcja otrzymuję 2 parametry, listę wartoci i liczbę elementów
def fSrednia(wart, liczba):
    srednia = 0
    for i in range(0, liczba):
        srednia = srednia + wart[i]
    srednia = srednia / liczba
    return srednia

# Funkcja licząca odchylenie standardowe podanej listy wartoci 
# funkcja otrzymuję 1 parametr listę wartoci
def fOdchylSt(wart):
    liczba = len(wart)
    srednia = fSrednia(wart, liczba)
    odchylst = 0
    for i in range(0, liczba):
        odchylst = odchylst + (srednia - wart[i]) * (srednia - wart[i])
    odchylst = math.sqrt(odchylst / liczba)
    return odchylst

# generowanie listy zawierających przypadkowe liczby rzeczywiste 
# z podanego zakresu
wart=[]
for i in range(100):
    wart.append(rnd.uniform(15,17))

print("Odchylenie st. wartosci sredniej numpy          : "+str(numpy.std(wart)))
print("Odchylenie st. wartosci sredniej funkcja własna : "+str(fOdchylSt(wart)))

# 25. Utwórz fukcję, która jako argument będzie przyjmować listę 
#   liczb zmiennoprzecinkowych, a jej wynikiem będzie drugi moment centralny 
#   (wariancja)
import random as rnd
import numpy 

# Funkcja licząca rednią arytmetyczną podanej listy wartoci 
# funkcja otrzymuję 2 parametry, listę wartoci i liczbę elementów
def fSrednia(wart, liczba):
    srednia = 0
    for i in range(0, liczba):
        srednia = srednia + wart[i]
    srednia = srednia / liczba
    return srednia

# Funkcja licząca wariancję podanej listy wartoci 
# funkcja otrzymuję 1 parametr listę wartoci
def fWariancja(wart):
    liczba = len(wart)
    wariancja = 0
    srednia = fSrednia(wart, liczba)
    for i in range(0, liczba):
        wariancja = wariancja + (srednia - wart[i]) * (srednia - wart[i])
    wariancja = wariancja / liczba
    return wariancja
# generowanie listy zawierających liczby rzeczywiste 
# z podanego zakresu
wart=[]
for i in range(100):
    wart.append(rnd.uniform(15,17))

print("wariancja numpy          : "+str(numpy.var(wart)))
print("Wariancja funkcja własna : "+str(fWariancja(wart)))

# 27. Utwórz funkcję, która jako argument będzie przyjmować listę 
#    liczb zmiennoprzecinkowych, a jej wynikiem będzie czwarty moment centralny 
#   (kurtoza)
from math import sqrt,pow
from random import uniform
from scipy.stats import kurtosis
import numpy 

# Funkcja licząca wartosć srednią podanej listy wartoci 
# funkcja otrzymuję 1 parametr listę wartoci
def fSrednia(wart):
    srednia = 0
    liczba = len(wart)
    for i in range(0, liczba):
        srednia = srednia + wart[i]
    srednia = srednia / liczba
    return srednia

# Funkcja licząca odchylenie standardowe podanej listy wartoci 
# funkcja otrzymuję 1 parametr listę wartoci
def fOdchylSt(wart):
    liczba = len(wart)
    srednia = fSrednia(wart)
    odchylst = 0
    for i in range(0, liczba):
        odchylst = odchylst + pow(srednia - wart[i], 2)
    odchylst = sqrt(odchylst / liczba)
    return odchylst

# Funkcja liczącaczwarty moment centralny podanej listy wartoci 
# funkcja otrzymuję 1 parametr listę wartoci
def fKurtoza(wart):
    liczba = len(wart)
    srednia = fSrednia(wart)
    odchylst = fOdchylSt(wart)
    kurtoza = 0
    for i in range(0, liczba):
        kurtoza = kurtoza + pow(srednia - wart[i], 4)
    odchylst = pow(odchylst, 4) * liczba
    kurtoza = kurtoza / odchylst - 3
    return kurtoza

# generowanie listy zawierających 1000 przypadkowych liczby rzeczywiste 
# z podanego zakresu
wart=[]
for i in range(1000):
    wart.append(uniform(21,25))

print("Kurtoza funkcja scipy  : "+str(kurtosis(wart)))
print("Kurtoza funkcja własna : "+str(fKurtoza(wart)))

#31. Korzystając z instrukcji np.random.choice oraz reshape z pakietu numpy 
#   stworzyć funkcję generują macierz kwadratową stopnia N wypełnioną 
#   wartościami 0 i 255 w losowy sposób

import random as rnd
import numpy as nmp

# Funkcja zwraca tablicę o podanym rozmiarze 
# wypełnioną przypadkowymi liczbami całkowitymiz zakresu 0-255
def fRndArray(rozmiar):
    # stworzenie pustej listy wartoci
    wart=[]
    # wypełnienie listy zerami
    for i in range(rozmiar * rozmiar):
        wart.append(0)
    # zamiana listy na tabelę jednowierszową
    tabela = nmp.array(wart)
    # zmiana tabeli jednowierszowej w podaną macierz kwadratową
    macierz = nmp.reshape(tabela, (rozmiar, rozmiar))
    # zerowanie listy wartoci
    wart=[]
    # Stworzenie listy wartoci zawierający liczby 0-255
    # wypełnienie listy wartoci 
    for i in range(256):
        wart.append(i)
    # wypełnienie macierzy przypadkowymi liczbami z podanej listy 
    for i in range(rozmiar):
        for j in range(rozmiar):
            macierz[i,j] = rnd.choice(wart)
    return macierz
# ustalenie rozmiaru macierzy wynikowej
rozmiar = 6
print(fRndArray(rozmiar))

#32. Utwórz funckję, która na zadanej macierzy zapisze wzór ustalonych struktur 
#   (blok, ul, bochenek, łódka, światła uliczne, żaba, latarnia)
import matplotlib.pyplot as plt
import numpy as np

# Funkcja zwraca macierz kwadratową N*N wypełnioną zerami
def whiteGrid(N):
    return np.random.choice([0,0], N*N).reshape(N, N)

# Funkcja dodale wzór "Szybowiec" na podanych współrzędnych
# zmienna line ustala kierunek poróży szybowca, wartoci SE, NE, NW, SW
def addGlider(i, j, image, line):
    glider = image[i:i+3, j:j+3]
    if (line == 'SE'):
        glider = np.array([[0, 255, 0],[0,0,255],[255,255,255]])
    elif (line == 'NE'):
        glider = np.array([[0, 255, 255],[255,0,255],[0,0,255]])
    elif (line == 'NW'):
        glider = np.array([[255, 255, 255],[255,0,0],[0,255,0]])
    elif (line == 'SW'):
        glider = np.array([[255, 0, 0],[255,0,255],[255,255,0]])
    image[i:i+3, j:j+3] = glider

# Funkcja dodale wzór "Blok" na podanych współrzędnych
def addBlock(i, j, image):
    block = np.array([[255, 255],[255,255]])
    image[i:i+2, j:j+2] = block
    
# Funkcja dodale wzór "Ul" na podanych współrzędnych
# zmienna line ustala kierunek początkowy, NS - pionowy, WE - poziomy
def addBeehive(i, j, image, line):
    if (line == 'NS'):
        beehive = np.array([[0,255,0],[255,0,255],[255,0,255],[0,255,0]])
        image[i:i+4, j:j+3] = beehive
    elif (line == 'WE'):
        beehive = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
        image[i:i+3, j:j+4] = beehive
    
# Funkcja dodale wzór "łódź" na podanych współrzędnych
# zmienna line ustala kierunek dziobu łodzi, wartoci SE, NE, NW, SW
def addBoat(i, j, image, line):
    boat = image[i:i+3, j:j+3]
    if (line == 'SE'):
        boat = np.array([[0,255,0],[255,0,255],[0,255,255]])
    elif (line == 'SW'):
        boat = np.array([[0,255,0],[255,0,255],[255,255,0]])
    elif (line == 'NW'):
        boat = np.array([[255,255,0],[255,0,255],[0,255,0]])
    elif (line == 'NE'):
        boat = np.array([[0,255,255],[255,0,255],[0,255,0]])
    image[i:i+3, j:j+3] = boat

# Funkcja dodale wzór "Bochenbek" na podanych współrzędnych
# zmienna line ustala kierunek rogu, wartoci SE, NE, NW, SW
def addLoaf(i, j, image, line):
    loaf = image[i:i+4, j:j+4]
    if (line == 'SE'):
        loaf = np.array([[0,0,255,0],[0,255,0,255],[255,0,0,255],[0,255,255,0]])    
    elif (line == 'SW'):
        loaf = np.array([[0,255,0,0],[255,0,255,0],[255,0,0,255],[0,255,255,0]])    
    elif (line == 'NW'):
        loaf = np.array([[0,255,255,0],[255,0,0,255],[255,0,255,0],[0,255,0,0]])    
    elif (line == 'NE'):
        loaf = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],[0,0,255,0]])    
    image[i:i+4, j:j+4] = loaf

# Funkcja dodale wzór "Żaba" na podanych współrzędnych
# zmienna line ustala kierunek początkowy, NS - pionowy, WE - poziomy
def addToad(i, j, image, line):
    if (line == 'NS'):
        toad = np.array([[255,0],[255,255],[255,255],[0,255]])
        image[i:i+4, j:j+2] = toad
    if (line == 'WE'):
        toad = np.array([[255,255,255,0],[0,255,255,255]])
        image[i:i+2, j:j+4] = toad

# Funkcja dodale wzór "Światła uliczbne" na podanych współrzędnych
# zmienna line ustala kierunek początkowy, NS - pionowy, WE - poziomy
def addBlinker(i, j, image, line):
    if (line == 'NS'):
        blinker = np.array([[0,255,0],[0,255,0],[0,255,0]])
    else:
        blinker = np.array([[0,0,0],[255,255,255],[0,0,0]])
    
# Funkcja dodale wzór "Latarnia" na podanych współrzędnych
# zmienna line ustala kierunek początkowy, L - lewy, R - prawy
def addBeacon(i, j, image, line):
    if (line == 'R'):
        beacon = np.array([[255,255,0,0],[255,0,0,0],[0,0,0,255],[0,0,255,255]])
        image[i:i+4, j:j+4] = beacon
    if (line == 'L'):
        beacon = np.array([[0,0,255,255],[0,0,0,255],[255,0,0,0],[255,255,0,0]])
        image[i:i+4, j:j+4] = beacon

# Wypełnienie macuirzy zerami - czyli pomalowanie kom órek na biało
image = whiteGrid(30)

# utworzenie figury
plt.figure()

# Wpisywanie poszczególnych kstałtów
addGlider(1, 1, image, 'SE')
addGlider(1, 6, image, 'NE')
addGlider(1, 14, image, 'NW')
addGlider(1, 21, image, 'SW')

addBlock(7,1, image)

addBeehive(6, 7, image, 'NS')
addBeehive(6, 14, image, 'WE')

addBoat(12, 1, image, 'SE')
addBoat(12, 7, image, 'NE')
addBoat(12, 14, image, 'NW')
addBoat(12, 21, image, 'SW')

addLoaf(18, 1, image, 'NE')
addLoaf(18, 7, image, 'NW')
addLoaf(18, 14, image, 'SW')
addLoaf(18, 21, image, 'SE')

addToad(24, 1, image, 'NS')
addToad(25, 7 , image, 'WE')

addBeacon(24,14, image, 'L')
addBeacon(24,21, image, 'R')

# Wywietlanie
plt.imshow(image, cmap = 'Greys')
plt.show()
