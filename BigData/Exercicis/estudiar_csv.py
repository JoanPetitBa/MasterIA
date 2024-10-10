import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = ""

data = pd.read_csv(path)

# MOSTRA LES CINC PRIMERES FILES DE LES DADES
data.head()

# RESUM DE LES DADES
data.describe().T

# INFORMACIÓ DE LES DADES
data.info()

# MOSTRA EL TAMANY DE LES DADES (FILES,COLUMNES)
data.shape

# COMPROBAR SI HI HA VALORS NULS
data.isna().any()

# FER GRAFICS DE CADA COLUMNA
data.hist(figsize=(20,30))