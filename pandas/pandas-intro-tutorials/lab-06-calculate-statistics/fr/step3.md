# Agrégation de statistiques par catégorie

Ensuite, nous allons apprendre à aggréger des statistiques groupées par catégorie.

```python
# Calcul de l'âge moyen des passagers masculins et féminins du Titanic
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# Affichage du résultat
print(f"L'âge moyen des passagers masculins et féminins du Titanic est {average_age_sex}")

# Calcul de la moyenne du prix du billet de voyage pour chaque combinaison de sexe et de classe de cabine
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# Affichage du résultat
print(f"La moyenne du prix du billet de voyage pour chaque combinaison de sexe et de classe de cabine est {mean_fare_sex_class}")
```
