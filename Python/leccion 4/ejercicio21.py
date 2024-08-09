""" 
tienda del libro
proporcionar el nombre:<string>
proporcionar id:<int>
proporcionar el precio:<float>
indicar si el envio es gratuito(true/false)
"""

ids = int(input('ingrese el id:  '))

nombre= input('ingrese el nombre del libro: ')

precio = float(input('ingrese precio del libro:  '))

envio =  input('el envio es gratuito ( True or False):  ')

if envio =='True':
    envio=True
elif envio == 'False':
    envio=False 
else:
    envio =' valor incorrecto, debe escribir True o False'
    
print (f''' 
       id {ids} 
       nombre del libro {nombre} 
       precio {precio} 
       envio es gratuito {envio}''')