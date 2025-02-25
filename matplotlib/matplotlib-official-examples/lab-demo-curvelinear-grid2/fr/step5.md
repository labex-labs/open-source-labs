# Création de la figure

La dernière étape consiste à créer la figure à l'aide de la fonction `plt.figure`. Nous définirons la taille de la figure sur (7, 4) et appellerons la fonction `curvelinear_test1` créée dans les étapes 2 - 4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
