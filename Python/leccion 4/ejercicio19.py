edad = int(input('ingrese su edad: '))

"""
if edad >=20 and edad<30:    
    print(f'su edad es {edad} y esta dentro del rango')

else:
    
    print (f'au edad es {edad} no esta dentro del rango')
    
if edad >= 30 and edad < 40:
    
    print(f'su edad es {edad} y esta dentro del rango')

else:
    
    print (f'au edad es {edad} no esta dentro del rango')
"""

veinte= edad >=20 and edad < 30
treinta= edad >=30 and edad < 40

if veinte or treinta:
    print (f"esta demtrp de rango 20`s y 30's su edad es {edad} ")
else:
    print (f"su edad esta fuera del rango de los 20's a 30's su edad es: {edad}")