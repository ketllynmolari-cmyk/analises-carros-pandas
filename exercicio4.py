import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("carros.csv")

# Conta quantos carros de cada marca
df["company"].value_counts().plot(kind="bar")

plt.title("Quantos carros de cada marca")
plt.xlabel("Marca")
plt.ylabel("Quantidade")
plt.show()