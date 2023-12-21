

final=input('¿Acabo la carrera?, contesta con si o no')
'''for i in diccionario:
    final=input('¿Acabo la carrera?, contesta con si o no')
    if final == 'si':
        print('El corredor a las',diccionario['tiempo'], 'estaba en el km',diccionario['km'])
    else:
        print('no')'''
while final == 'no':
    tiempo=str(input('introduce la hora del corredor'))
    km=str(input('introduce el kilomentro del corredor'))
    diccionario={'tiempo':tiempo,'km':km}
    break
while final == 'si':
     print('El corredor a las',diccionario['tiempo'], 'estaba en el km',diccionario['km'])
