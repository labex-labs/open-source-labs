# Reformateando Dados

Às vezes, os dados podem não estar inicialmente no formato necessário pelo scikit-learn. Nesses casos, precisamos pré-processar os dados para transformá-los na forma `(n_amostras, n_características)`. Um exemplo de reformatear dados é o conjunto de dados dígitos, que consiste em 1797 imagens 8x8 de dígitos manuscritos:

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Saída:

```
(1797, 8, 8)
```

Para usar este conjunto de dados com o scikit-learn, precisamos reformatear cada imagem 8x8 em um vetor de características de comprimento 64:

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
