# Extraire des sous-chaînes

Vous pouvez extraire des sous-chaînes à l'aide d'expressions régulières. La méthode `extract` accepte une expression régulière avec au moins un groupe de capture.

```python
# extraire le premier chiffre de chaque chaîne
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
