# Pivoteamento com Agregações Únicas

Pivot é um dos métodos-chave para _reshaping_ de dados no Pandas. Ele oferece uma maneira de transformar seus dados para que você possa visualizá-los de diferentes ângulos.

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
