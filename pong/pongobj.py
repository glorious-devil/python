#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        self.szer, self.wys = szer, wys
        pygame.display.set_caption('Pong')
    
    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((200, 255, 255))
        for obGraf in args:
            self.pow.blit(obGraf.pow, obGraf.prost)
        pygame.display.update()

class PongGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        pygame.key.set_repeat(50, 25) #po 50 sek wykryj czułość klawisza i odczytaj po 25 s
        self.plansza = Plansza(szer, wys)
        self.pal1 = Paletka(szer=100, wys=20, x=350, y=360, kolor=(0, 0, 255)) #lub Paletka(szer=100, wys=20, x=350, y=360) - bardziej czytelne
        self.pal2 = Paletka(szer=100, wys=20, x=350, y=20, kolor=(255, 0, 0))
        self.pilka = Pilka(szer=20, wys=20, x=390, y=190, kolor=(0, 255, 0))
        self.al = Al(self.pal2, self.pilka, 5)
        # zegar
        self.fpsClock = pygame.time.Clock()
        
    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == MOUSEMOTION:
                    mX, mY = event.pos
                    self.pal1.przesun(mX, self.plansza.szer)
                    
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.pal1.przesun2(self.plansza.szer, -10)
                    elif event.key == K_RIGHT:
                        self.pal1.przesun2(self.plansza.szer, 10)
                    elif event.key == K_UP:
                        self.pal1.przesun3(self.plansza.szer, -10)
                    elif event.key == K_DOWN:
                        self.pal1.przesun3(self.plansza.szer, 10)
                        
                        
            self.pilka.ruszaj(self.plansza.szer, self.plansza.wys, self.pal1, self.pal2)
            self.al.ruszaj()
            self.plansza.rysuj(
                self.pal1,
                self.pal2,
                self.pilka,         
            )
            self.fpsClock.tick(120)
            
class ObiektGraf():
    """Klasa bazowa dla rysowanych obiektów"""
    
    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0)): #szerokość, wysokość, rogi i kolor (red, green, yellow)
        self.szer = szer
        self.wys = wys
        self.pow = pygame.Surface([szer, wys], pygame.SRCALPHA).convert_alpha()
        self.prost = self.pow.get_rect(x=x, y=y) #zwraca obiekt typu rect z ustawionymi zmiennymi
        self.kolor = kolor
        
class Paletka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0), maks_v=10): #szerokość, wysokość, rogi, kolor (red, green, yellow), prędkość
        super().__init__(szer, wys, x, y, kolor) #dziedziczenie cech rodzica elementu, wywołanie konstruktora z klasy bazowej
        self.pow.fill(kolor)
        self.maks_v = maks_v
        
    def przesun(self, mX, o_szer):
        """przesuniecie = mX
        :param:
        mX = składowa X pozycji paletki
        o_szer = szerokość okna gry
        """
        
        przesuniecie = mX - self.maks_v
        if przesuniecie > o_szer - self.szer:
            przesuniecie = o_szer - self.szer
        if przesuniecie < 0:
            przesuniecie = 0
        self.prost.x = przesuniecie
        
    def przesun2(self, o_szer, krok)
        if przesuniecie = self.prost.x > krok:
            przesuniecie = o_szer - self.szer
        if przesuniecie
        
class Pilka(ObiektGraf):
    
    def __init__(self, szer, wys, x, y, kolor=(0, 0, 255), px_v=3, py_v=3):
        super().__init__(szer, wys, x, y, kolor)
        pygame.draw.ellipse(self.pow, self.kolor, [0, 0, self.szer, self.wys])
        self.px_v = px_v
        self.py_v = py_v
        self.start_x = x
        self.start_y = y
        
    def ruszaj(self, o_szer, o_wys, *args):
        self.prost.move_ip(self.px_v, self.py_v)
        if self.prost.right > o_szer or self.prost.left <= 0:
            self.px_v *= -1
        if self.prost.top <= 0 or self.prost.bottom >= o_wys:
            self.prost.x = o_szer / 2
            self.prost.y = o_wys / 2
            
        for pal in args: 
            if self.prost.colliderect(pal.prost):
                self.py_v *= -1

class Al():
    
    def __init__(self, pal, pilka, pal_v=20):
        self.pal = pal
        self.pilka = pilka
        self.pal_v = pal_v
    
    def ruszaj(self):
        if self.pilka.prost.centerx > self.pal.prost.centerx: #śledzenie zaczyna się i kiedy środek piłki nie pokrywa się ze środkiem paletki położenie się zmienia
            self.pal.prost.x += self.pal_v
        elif self.pilka.prost.centerx < self.pal.prost.centerx:
            self.pal.prost.x -= self.pal_v
            
if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
