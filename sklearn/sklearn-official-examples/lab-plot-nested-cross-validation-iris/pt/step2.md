# Definir os Hiperparâmetros

Em seguida, definimos os hiperparâmetros a serem otimizados para o classificador de vetores de suporte. Neste caso, otimizamos o parâmetro de custo `C` e o coeficiente do kernel `gamma`.

```python
# Configurar possíveis valores dos parâmetros para otimização
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```
