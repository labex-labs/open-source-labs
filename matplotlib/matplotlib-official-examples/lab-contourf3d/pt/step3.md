# Gerar os Dados

Agora geraremos os dados a serem usados no gráfico de contorno 3D. Usaremos o método `axes3d.get_test_data()` para gerar os dados. Este método gera dados de teste para um gráfico 3D.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
