# Criando o Gráfico

Em seguida, criaremos o gráfico definindo o eixo principal (host axis) e o eixo secundário (parasite axis). O eixo principal será usado para os dados primários e o eixo secundário será usado para os dados secundários.

```python
host = host_subplot(111)
par = host.twinx()
```
