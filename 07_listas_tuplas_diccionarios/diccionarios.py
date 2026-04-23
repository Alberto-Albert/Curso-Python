midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "Espana":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)


mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(midiccionario["Francia"])


midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario["Anillos"])

print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))