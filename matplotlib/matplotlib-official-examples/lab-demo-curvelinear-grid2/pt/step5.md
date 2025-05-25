# Criar a Figura

O passo final é criar a figura usando a função `plt.figure`. Definiremos o tamanho da figura como (7, 4) e chamaremos a função `curvelinear_test1` criada nos Passos 2-4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
