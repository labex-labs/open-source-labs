# Interprétation des hyperparamètres du noyau

Maintenant, nous pouvons examiner les hyperparamètres du noyau.

```python
gaussian_process.kernel_
```

Ainsi, la majeure partie du signal cible, avec la moyenne soustraite, est expliquée par une tendance à la hausse à long terme d'environ 45 ppm et une échelle de longueur d'environ 52 ans. La composante périodique a une amplitude d'environ 2,6 ppm, un temps de décroissance d'environ 90 ans et une échelle de longueur d'environ 1,5. Le long temps de décroissance indique qu'il existe une composante très proche d'une périodicité saisonnière. Le bruit corrélé a une amplitude d'environ 0,2 ppm avec une échelle de longueur d'environ 0,12 ans et une contribution de bruit blanc d'environ 0,04 ppm. Ainsi, le niveau global de bruit est très faible, ce qui indique que les données peuvent être très bien expliquées par le modèle.
