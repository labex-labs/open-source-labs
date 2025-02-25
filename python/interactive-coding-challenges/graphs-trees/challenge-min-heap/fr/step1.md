# Tas min

## Problème

Implémentez un tas min avec les méthodes suivantes :

- `extract_min()` : supprime et renvoie la valeur minimale dans le tas
- `insert(value)` : insère une nouvelle valeur dans le tas tout en maintenant la propriété du tas

## Exigences

L'implémentation doit répondre aux exigences suivantes :

- Les entrées sont des entiers
- L'implémentation doit tenir dans la mémoire

## Utilisation exemple

Considérez le tas min suivant :

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
```

- `extract_min()` : supprime et renvoie la valeur minimale dans le tas, qui est 5. Le tas résultant est :

```txt
          _15_
        /      \
       20      25
      / \     /  \
     22  40
```

- `insert(2)` : insère la valeur 2 dans le tas tout en maintenant la propriété du tas. Le tas résultant est :

```txt
          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
```
