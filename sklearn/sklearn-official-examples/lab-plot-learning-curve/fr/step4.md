# Analyser les courbes d'apprentissage

```python
# Interpréter les courbes d'apprentissage
```

Nous pouvons analyser la courbe d'apprentissage du classifieur Naïf Bayes. Sa forme peut être trouvée très souvent dans des ensembles de données plus complexes : le score d'entraînement est très élevé lorsqu'on utilise peu d'échantillons pour l'entraînement et diminue lorsque le nombre d'échantillons augmente, tandis que le score de test est très bas au début et augmente ensuite lorsqu'on ajoute des échantillons. Les scores d'entraînement et de test deviennent plus réalistes lorsqu'on utilise tous les échantillons pour l'entraînement.

Nous voyons une autre courbe d'apprentissage typique pour le classifieur SVM avec noyau RBF. Le score d'entraînement reste élevé indépendamment de la taille de l'ensemble d'entraînement. D'un autre côté, le score de test augmente avec la taille de l'ensemble de données d'entraînement. En effet, il augmente jusqu'à un certain point où il atteint un plateau. L'observation d'un tel plateau est une indication qu'il peut ne pas être utile d'acquérir de nouvelles données pour entraîner le modèle puisque la performance de généralisation du modèle ne va plus augmenter.
