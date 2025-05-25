# Gerar Dados

Neste passo, geraremos os dados para treinar e testar o classificador SVM. Geraremos 300 pontos de dados aleatórios com duas características. O alvo a prever é um XOR das entradas.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
