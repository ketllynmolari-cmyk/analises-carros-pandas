import pandas as pd

df = pd.read_csv("carros.csv")

media = df["price"].mean()
print("Preço médio geral:", media)

caros = df[df["price"] > media]
print(caros)

print("Tem", len(caros), "carros acima da média")