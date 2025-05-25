# Gerar o Conjunto de Dados Swiss-Hole

Geramos o conjunto de dados Swiss-Hole adicionando um buraco ao conjunto de dados Swiss Roll usando o parâmetro `hole=True` na função `make_swiss_roll()`.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
