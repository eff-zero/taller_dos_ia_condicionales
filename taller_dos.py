#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 02:25:48 2021

@author: jesus
"""
# TALLER #2 - EJERICICIOS CONDICIONALES

# 1.
cantidad_camisas = int(input('Ingrese el número de camisas: '))
acumulador = 0
if (cantidad_camisas > 0):
    for x in range(cantidad_camisas):
        x = float(input(f'Valor de camisa #{x + 1}: '))
        acumulador = acumulador + x
    if (cantidad_camisas >= 3):
        descuento = 1 - 0.30
        total = acumulador * descuento
        print(f'Su total a pagar es ${total:,}')
    elif (cantidad_camisas > 0):
        descuento = 1 - 0.10
        total = acumulador * descuento
        print(f'Su total a pagar es ${total:,}')
else:
    print(f'La cantidad {cantidad_camisas} de camisas es invalida')
