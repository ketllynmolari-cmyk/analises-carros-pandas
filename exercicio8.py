import pandas as pd

df = pd.read_csv("carros.csv")

mais_barato = df[df["price"] == df["price"].min()]

print("O carro mais barato é:")
print(mais_barato)