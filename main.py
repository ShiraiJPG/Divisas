print("Hola Mundo")

"""
FÓRMULA PARA CONVERSIÓN DE DIVISA:
Para convertir de una moneda a otra, se utiliza la siguiente fórmula:

    cantidad_en_moneda_destino = presupuesto / tasa_de_cambio

Donde:
- presupuesto: es la cantidad de dinero que tienes en la moneda original.
- tasa_de_cambio: es el valor de 1 unidad de la moneda destino expresada en la moneda original.

Por ejemplo, si 1 JPY = 0.0075 USD, entonces:
    300 USD / 0.0075 USD/JPY = 40000 JPY
"""

# Función de conversión
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


## Edita el codigo segun la cantidad que gustes.
print("Convertir USD a Yenes Japoneses (JPY):")
print(exchange_money(300, 0.0075))

print("Convertir USD a Pesos Mexicanos (MXN):")
print(exchange_money(300, 0.0581))

print("Convertir USD a Euros (EUR):")
print(exchange_money(300, 1.075))

print("Convertir USD a Pesos Colombianos (COP):")
print(exchange_money(300, 0.000259))
