# Créer la fonction génératrice de données

Ensuite, nous devons créer une fonction pour générer les données de l'animation. La fonction produira une onde sinusoïdale qui décroît au fil du temps. Nous utiliserons la fonction `itertools.count()` pour générer une séquence infinie de nombres. Nous utiliserons ces nombres pour calculer les valeurs de l'onde sinusoïdale.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
