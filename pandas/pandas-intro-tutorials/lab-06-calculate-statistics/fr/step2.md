# Calcul des statistiques résumées

Dans cette étape, nous allons calculer des statistiques résumées pour l'ensemble de données Titanic.

```python
# Calcul de l'âge moyen des passagers du Titanic
average_age = titanic["Age"].mean()
# Affichage du résultat
print(f"L'âge moyen des passagers du Titanic est {average_age}")

# Calcul de l'âge médian et du prix du billet de voyage des passagers du Titanic
median_age_fare = titanic[["Age", "Fare"]].median()
# Affichage du résultat
print(f"L'âge médian et le prix du billet de voyage des passagers du Titanic sont {median_age_fare}")
```
