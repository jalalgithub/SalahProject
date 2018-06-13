import requests
import csv
import time

header=['timestamp','last','volume','bid','ask','high','low','vwap']
with open("Data1.csv", "w") as fd:
	w = csv.writer(fd,delimiter=',',lineterminator = '\n')
	#Creation du Header
	w.writerow(header)
	#Debut du processus de stockage de donnees
	while(1):
		#On emet une requete tout les 30 secondes
		time.sleep(30)
		req = requests.get('https://www.bitstamp.net/api/ticker/').json()
		val=[]
		for i in header:
			val.append(req[i])
		#Ajout de valeurs
		w.writerow(val)