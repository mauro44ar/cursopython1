edad = int(input('Escriba su edad: '))

if edad > 0 and edad <= 10:
    
    print(f'Tiene {edad} es un niño')

elif edad > 10 and edad <= 18:
    
    print (f'Tiene {edad} es un adolescente')
    
elif edad >18 and edad <=64:
    
    print(f'Tiene {edad} es un adulto ')

else:
    
    print(f'Tiene {edad} es un abuelo ')