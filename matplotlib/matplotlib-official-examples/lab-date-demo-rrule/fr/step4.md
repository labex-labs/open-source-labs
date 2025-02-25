# Définissez le localisateur et le formateur de repères

Vous utiliserez la fonction RRuleLocator pour définir le localisateur de repères sur la base de la règle de récurrence que vous avez définie dans l'étape précédente. Vous utiliserez également la fonction DateFormatter pour définir le formateur de repères.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```
