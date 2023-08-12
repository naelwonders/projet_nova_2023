import pandas as pd 

#lire le fichier csv 'clients', que je stock dans une variable (type : DATAFRAME sont en 2D avec lignes et colonnes)
clients = pd.read_csv("clients.csv") 

# afficher les 5 premières lignes
print(clients.head()) #display is for the jupyter notebook, here you use print

#afficher le nom et l'email
variables = clients[['nom','email']]
print(variables)

#le type de data d'une colonne est une SERIE (une dimention donc une colonne)
print(type(clients['email']))

print(type(clients))

#pour afficher les noms des colonnes
print(clients.columns)

print(clients.loc[clients['nom'] == 'Thomas', : ])