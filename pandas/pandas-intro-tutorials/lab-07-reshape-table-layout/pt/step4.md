# Criar uma Tabela Pivot

Crie uma tabela pivot para encontrar as concentrações médias de 𝑁𝑂2 e 𝑃𝑀25 em cada uma das estações.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
