# Ajouter la description et le nom complet des paramètres

Enfin, nous ajouterons la description et le nom complet des paramètres au tableau de mesures. Nous effectuons une jointure gauche sur les colonnes `parameter` et `id`.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
