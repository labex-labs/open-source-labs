# Converter Formato Largo para Longo

Agora, vamos converter os dados em formato largo de 𝑁𝑂2 para formato longo usando a função `melt`.

```python
# Resetar o índice para no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Meltar os dados
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
