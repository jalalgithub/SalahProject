import pandas as pd
import requests
import time

with open('data.csv', 'a') as __f__:
	__i__=0
	while 1:
		time.sleep(10)
		__req__= requests.get('https://www.bitstamp.net/api/ticker/').json()
		__df__=pd.DataFrame(__req__, columns = ['timestamp','last','volume','bid','ask','high','low','vwap'],index=[__i__])
		#add the header for the first iteration
		if __i__==0:
			__df__.to_csv(__f__, header=True)
		#Otherwise, only add the last row received
		else:
			__df__.to_csv(__f__, header=False)
		__i__+=1
		print("Iteration number:",__i__)