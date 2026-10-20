import pandas as pd

df = pd.read_csv("carros.csv")

print("=== RESUMO FINAL ===")
print("Total de carros:", len(df))
print("Marca que mais aparece:", df["company"].mode()[0])
print("Preço médio:", df["price"].mean())
print("Carro mais caro:", df["price"].max())
print("Carro mais barato:", df["price"].min())