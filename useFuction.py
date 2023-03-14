"""Funcion que clasifica tamaños de huevos y devuleve el resultado en un diccionario"""

def clasificacion_huevos(mi_lista):

    #variables locales
    huevos_AAA = 0
    huevos_AA = 0
    huevos_A = 0
    huevos_BC = 0

    for huevo in mi_lista:
        if huevo >= 55 and huevo <60:
            huevos_A += 1
        elif huevo >= 60 and huevo <69:
            huevos_AA += 1
        elif huevo >= 69:
            huevos_AAA += 1
        elif huevo < 53:
            huevos_BC +=1

    # se crea una variable tipo lista que va contener los valores dados en el ciclo anterior                
    cajas = [huevos_A, huevos_AA, huevos_AAA, huevos_BC]


    # crea el diccionario de resultados con los valores recibidos en la funcion
    result = [{'tipo_huevo': 'A', 'numero_huevos': huevos_A, 'numero_bandejas': cajas[0]},
               {'tipo_huevo':'AA', 'numero_huevos': huevos_AA, 'numero_bandejas': cajas[1]},
               {'tipo_huevo': 'AAA', 'numero_huevos': huevos_AAA, 'numero_bandejas': cajas[2]},
               {'tipo_huevo': 'BC', 'numeros_huevos': huevos_BC, 'numero_bandejas':cajas[3]}
               ]
    return result
 
clasificacion_huevos([55,80,3,1])