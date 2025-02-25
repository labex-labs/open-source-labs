# Générer des données aléatoires

Dans cette étape, vous allez générer des données aléatoires pour la compétence du lanceur, l'angle de décollage, la poussée, le succès et la position. Plus précisément, vous allez générer 25 points de données pour chaque variable, sauf pour la position, qui aura 2 coordonnées pour chaque point de données.

```python
N = 25
np.random.seed(42)
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)
```
