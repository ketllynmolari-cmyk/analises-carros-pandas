import pandas as pd

df = pd.read_csv("carros.csv")

# Acha a linha do carro mais caro
mais_caro = df[df["price"] == df["price"].max()]

print("O carro mais caro é:")
print(mais_caro)