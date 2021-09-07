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

# 2.
numero = int(input('Ingrese un número entre [1-100]: '))
monto_a_pagar = float(input('Ingrese el valor de su compra: '))
if (numero > 0 and numero <= 100):
    if (numero < 74):
        descuento = 0.15
        total = monto_a_pagar * descuento
        print(f'Su descuento es de ${total:,}')
    elif (numero >= 74):
        descuento = 0.20
        total = monto_a_pagar * descuento
        print(f'Su descuento es de ${total:,}')
else:
    print('Número no valido')

# 3.
fianza = float(input('Ingrese el valor de su fianza: '))
cuotas = int(input('Ingrese el número de cuotas: '))
total_fianza = fianza * cuotas
if (fianza > 0 and cuotas > 0):
    if (fianza >= 50000):
        cuota = 2/100
        monto = total_fianza * cuota
        total = total_fianza + monto
        print(f'La cuota a pagar es por la afianzadora es de ${total:,}')
    else:
        cuota = 3/100
        monto = total_fianza * cuota
        total = total_fianza + monto
        print(f'La cuota a pagar es por la afianzadora es de ${total:,}')
else:
    print('Valor invalido de fianza o de cuotas')

# 4.
promedio = int(input('Ingrese su promedio de contaminación: '))
if (promedio > 0):
    if (promedio > 170):
        multa = 50/100
        ganancia_diaria = float(input('Ingrese su ganancia diaria promedio: '))
        dias = 5
        total_sin_descuento = ganancia_diaria * dias
        descuento_dia = ganancia_diaria * multa
        descuento_total = total_sin_descuento * multa
        print(f'Usted se le descontará ${descuento_dia:,} diariamente'
              f' y su descuento final a la semana es de ${descuento_total:,}')
    else:
        print('Usted no aplica para multa')
else:
    print('Promedio invalido')

# 5.
print('» Al cabo de tres años ingrese «')
decremento_carro = float(input('Valor de devaluación del carro: '))
incremento_terreno = float(input('Valor del incremento del terreno: '))
if (decremento_carro > 0 and incremento_terreno > 0):
    if (decremento_carro < incremento_terreno/2):
        print('Usted debería comprar el carro')
    else:
        print('Usted debería comprar el terreno')
else:
    print('Algún valor no es valido')

# 6.
precio_compu = 11000
cantidad_compu = int(input('Ingrese la cantidad de computadoras a comprar: '))
if (cantidad_compu > 0):
    total_sin_descuento = cantidad_compu * precio_compu
    if (cantidad_compu < 5):
        descuento = 10/100
        valor_descuento = total_sin_descuento * descuento
        valor_final = total_sin_descuento - valor_descuento
        print(f'Descuento: ${valor_descuento:,}, debe pagar: ${valor_final:,}')
    elif (cantidad_compu > 4 and cantidad_compu < 10):
        descuento = 20/100
        valor_descuento = total_sin_descuento * descuento
        valor_final = total_sin_descuento - valor_descuento
        print(f'Descuento: ${valor_descuento:,}, debe pagar: ${valor_final:,}')
    else:
        descuento = 40/100
        valor_descuento = total_sin_descuento * descuento
        valor_final = total_sin_descuento - valor_descuento
        print(f'Descuento: ${valor_descuento:,}, debe pagar: ${valor_final:,}')
else:
    print('Cantidad de computadoras no valido')

# 7.
iva = 1 + (16/100)
precio_producto = float(input('Ingrese el precio de su producto: '))
es_nosy = int(input('Ingrese [0 ó 1] si\n 1 » Sí\n 0 » No\n »» '))
if (precio_producto > 0):
    if (precio_producto > 2000 and es_nosy):
        descuento = 15/100
        valor_descuento = precio_producto * descuento
        valor_final = (precio_producto - valor_descuento) * iva
        print(f'El valor final del producto es ${valor_final:,}')
    elif (precio_producto > 2000):
        descuento = 10/100
        valor_descuento = precio_producto * descuento
        valor_final = (precio_producto - valor_descuento) * iva
        valor_final = round(valor_final, 2)
        print(f'El valor final del producto es ${valor_final:,}')
    elif (es_nosy):
        descuento = 5/100
        valor_descuento = precio_producto * descuento
        valor_final = (precio_producto - valor_descuento) * iva
        print(f'El valor final del producto es ${valor_final:,}')
    else:
        descuento = 0
        valor_descuento = precio_producto * descuento
        valor_final = (precio_producto - valor_descuento) * iva
        print(f'El valor final del producto es ${valor_final:,}')
else:
    print('Precio no valido')

# 8.
monto_compra = float(input('Ingrese el monto total de la compra: '))
pago_mayor_a_500 = {'Propio': 0.55, 'Banco': 0.30, 'Crédito': 0.15}  # > 500K
pago_menor_a_500 = {'Propio': 0.70, 'Banco': 0, 'Crédito': 0.30}  # < 500K
interes_fabricante = 0.20
if (monto_compra > 0):
    if (monto_compra > 500000):
        inversión_propia = monto_compra * pago_mayor_a_500['Propio']
        prestamo = monto_compra * pago_mayor_a_500['Banco']
        credito = monto_compra * pago_mayor_a_500['Crédito']
        valor_interes = interes_fabricante * credito
        print(f'Cantidad a invertir por la empresa » ${inversión_propia:,}\n'
              f'Valor del préstamo del banco » ${prestamo:,}\n'
              f'Valor del crédito con el fabricante » ${credito:,}\n'
              f'Valor del interés del fabricante » ${valor_interes:,}\n'
              )
    else:
        inversión_propia = monto_compra * pago_menor_a_500['Propio']
        prestamo = monto_compra * pago_menor_a_500['Banco']
        credito = monto_compra * pago_menor_a_500['Crédito']
        valor_interes = interes_fabricante * credito
        print(f'Cantidad a invertir por la empresa » ${inversión_propia:,}\n'
              f'Valor del préstamo del banco » ${prestamo:,}\n'
              f'Valor del crédito con el fabricante » ${credito:,}\n'
              f'Valor del interés del fabricante » ${valor_interes:,}\n'
              )
else:
    print('Monto invalido')

# 9.
numero_1 = float(input('Ingrese su primer número: '))
numero_2 = float(input('Ingrese su segundo número: '))
if (numero_1 > numero_2):
    resultado = numero_1 - numero_2
elif (numero_1 < numero_2):
    resultado = numero_1 + numero_2
else:
    resultado = numero_1 * numero_2
print(f'El resultado de su operacion según la comparación es » {resultado}')

# 10.
numero_1 = float(input('Ingrese su primer número: '))
numero_2 = float(input('Ingrese su segundo número: '))
numero_3 = float(input('Ingrese su tercer número: '))
numeros = [numero_1, numero_2, numero_3]
mayor = numero_1
for n in numeros:
    if (n > mayor):
        mayor = n
print(f'El número mayor es » {mayor}')
