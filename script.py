import requests
import time

#Ouverture du fichier ou on stockera les donnees
fd = open('Data.csv','w')

#Creation du Header
keys=['timestamp','last','volume','bid','ask','high','low','vwap']
header=",".join(keys)+'\n'
fd.write(header)

#Debut du processus de stockage de donnees
while(1):
	#On emet une requete tout les 30 secondes
	time.sleep(30)
	#Appel a l'API bitstamp
	req = requests.get('https://www.bitstamp.net/api/ticker/').json()
	val=''
	for i in keys:
		val+=str(req[i])+','
	val=val[:-1]
	val+='\n'
	fd.write(val)
