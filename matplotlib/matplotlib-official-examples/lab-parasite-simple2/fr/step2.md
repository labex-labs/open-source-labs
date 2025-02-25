# Définir les données

Ensuite, nous devons définir les données qui seront tracées. Dans cet exemple, nous avons un ensemble d'observations avec quatre variables : nom, mouvement propre angulaire, erreur de mouvement propre angulaire et distance. Nous allons convertir le mouvement propre angulaire en vitesse linéaire et le tracer en fonction de la FWHM (largeur totale à mi-hauteur) des observations.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Facteur de conversion du mouvement propre angulaire en vitesse linéaire
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```
