# Criar Pontos de Dados

Nesta etapa, criaremos alguns pontos de dados usando a classe de unidade personalizada - `Foo`.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
