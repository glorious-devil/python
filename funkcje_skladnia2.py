#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py

def mnoz(a, b):
    print(a * b)

def mnoz2(*args):
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)
    
    def wylicz(imie1='adam', imie2='ewa', **kwargs):    #słownik zmiennej długości, kwargs - keyword arguments
        print(imie1)
        print(imie2)
        for k, v in kwargs.items():
            print('{} {}'.format(k, v))
    
def main(args):
    mnoz(4, 6)
    mnoz2(4, 6, 8, 9, 3)
    wylicz(imie2='ola', imie3='piotr', imie4='lilith')
    for k, v in kwargs.items():
        print('{} {}'.format(k, v))
        
        #typy argumentów w funkcjach
        #pozycyjne wymagane
        #nazwane wymagane
        #argumenty domyślne
        #argumenty zmiennej długości: listy i słowniki
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
