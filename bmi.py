#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    wzrost = input('Podaj swój wzrost w cm: ')
    mase = input('Podaj swoją masę w kg: ')
    bmi = masa / (wzrost * 0.01)**2
        print('BMI = {:.2f}'.format(bmi))
    if bmi < 18,5: 
        print('niedowaga')
    elif bmi <= 24,9:
        print('norma')
    elif bmi < 30:
        print('nadwaga')
    else:
        print('otyłość')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
