

# Creamos lista de cervecerías o nodos de oferta
cervecerias = ["Cervecería A", "Cervercería B"]

# diccionario con la capacidad de oferta de cada cerveceria
oferta = {"Cervecería A": 1000,
          "Cervercería B": 4000}

# Creamos la lista de los bares o nodos de demanda
bares = ["Bar 1", "Bar 2", "Bar 3", "Bar 4", "Bar 5"]

# diccionario con la capacidad de demanda de cada bar
demanda = {"Bar 1":500,
           "Bar 2":900,
           "Bar 3":1800,
           "Bar 4":200,
           "Bar 5":700,}

# Lista con los costos de transporte de cada nodo
costos = [   #Bares
         #1 2 3 4 5
         [2,4,5,2,1],#A   Cervecerías
         [3,1,3,2,3] #B
         ]

p