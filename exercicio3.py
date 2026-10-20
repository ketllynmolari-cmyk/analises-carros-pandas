import pandas as pd

df = pd.read_csv("carros.csv")

print ("quantas linhas e colunas:")
print(df.shape)

print("\nMédia de preço: ")
print(df["price"].mean())

print("\nCarro mais caro: ")
print(df["price"].max())

print("\mQuantas mascas tem: ")
print(df["company"].value_counts())