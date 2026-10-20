import pandas as pd

df = pd.read_csv("carros.csv")

#limpar
df = df.dropna()
df = df.drop_duplicates()

# SALVA LIMPO POR CIMA 
df.to_csv("carros.csv", index=False)

print("limpo e salvo!")
print(df.head())