import pandas as pd

df = pd.read_csv("carros.csv")

# Salva a versão final limpa
df.to_csv("carros_limpo_final.csv", index=False)

print("Salvo com sucesso!")
print("Total de carros salvos:", len(df))
print("Preço médio final:", df["price"].mean())