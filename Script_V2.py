import numpy as np
import pandas as pd
import requests
import json
import time
import datetime


def generate_btc_dataset(nb_points):
    df = pd.DataFrame(columns=["timestamp", "last", "volume", "bid", "ask", "high", "low", "vwap", "open"])
    count = 0

    while count<nb_points:
        time.sleep(2)
        response = requests.get("https://www.bitstamp.net/api/ticker/")
        data = response.json()
        new_df = pd.DataFrame.from_dict(data, orient="index").T
        df = df.append(new_df, ignore_index=True)
        count += 1
    
    return df


if __name__ == "__main__":
	print("Dataset generation started")
	btc_dataset = generate_btc_dataset(nb_points=2500)
	btc_dataset.to_csv("btc_dataset.csv", index=False)
	print("Dataset generation finished")
