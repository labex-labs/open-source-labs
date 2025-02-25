# Règles générales de diffusion (broadcasting)

NumPy compare les formes de deux tableaux élément par élément pour déterminer s'ils sont compatibles pour la diffusion (broadcasting). Les règles suivantes s'appliquent :

1. Deux dimensions sont compatibles si elles ont la même taille.
2. Deux dimensions sont compatibles si l'une d'entre elles a une taille de 1.

Si ces conditions ne sont pas remplies, une `ValueError` est levée, indiquant que les tableaux ont des formes incompatibles.
