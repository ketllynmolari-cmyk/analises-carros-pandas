import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("carros.csv")

# Calcula a média de preço por marca
media = df.groupby("company")["price"].mean().sort_values()

print(media)

media.plot(kind="barh", color="green")
plt.title("Preço médio por marca")
plt.xlabel("Preço médio")
plt.show()