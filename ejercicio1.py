
def LeerDocument(archivo):
    '''Esta funcion leera la informacion de un fichero 
        y la guardara en una variable del tipo lista.
        Parametros:
            -archivo: Ruta de acceso al fichero a leer
        Salida:
            -lista: Lista con los datos del fichero'''


    import os

    if os.path.isfile(archivo):                       
        with open(archivo, 'r') as file:               
            documento = file.read()
        print(documento)

def IdentificarPagado(pagado):
    '''Esta funcion creera un fichero con todas las lineas del 
    documento en las que pone Pagado
        Parametros:
            -Pagado: Ruta de acceso al fichero a leer
        Salida:
            -no duvuelve nada'''
    file = open('LibroCuentas.txt', 'w')
    documento = file.readlines()
    pago = 'PAGAD0'
    for linea in documento:
        if pagado in linea:
            pago = linea.split(',')[2]
    if pago == 'PAGADO':
        print(pago)
    else:
        return pago
    

    
    
    

archivo = 'LibroCuentas.txt'
LeerDocument(archivo)
IdentificarPagado('PAGADO')    
    

        
