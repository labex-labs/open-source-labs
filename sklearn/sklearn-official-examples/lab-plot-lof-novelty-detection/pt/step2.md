# Gerar Dados

Vamos gerar alguns dados para treino, teste e outliers usando numpy. Vamos gerar 100 observações normais de treino, 20 observações normais de teste e 20 observações anormais novas.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
