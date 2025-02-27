# Générer des données

Ensuite, nous allons générer quelques données à utiliser pour notre régression. Nous allons créer une tendance monotone non linéaire avec un bruit uniforme homoscédaque.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
