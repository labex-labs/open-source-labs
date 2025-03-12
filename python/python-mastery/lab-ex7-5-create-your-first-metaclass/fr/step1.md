# Comprendre les métaclasses

Les métaclasses sont une fonctionnalité avancée mais puissante en Python. En tant que débutant, vous vous demandez peut - être ce que sont les métaclasses et pourquoi elles sont importantes. Avant de commencer à créer notre première métaclasse, prenons un moment pour comprendre ces concepts.

## Qu'est - ce qu'une métaclasse ?

En Python, tout est un objet, y compris les classes. Tout comme une classe normale est utilisée pour créer des instances, une métaclasse est utilisée pour créer des classes. Par défaut, Python utilise la métaclasse intégrée `type` pour créer toutes les classes.

Découpons le processus de création de classe étape par étape :

1. Tout d'abord, Python lit la définition de classe que vous avez écrite dans votre code. C'est là que vous définissez le nom de la classe, ses attributs et ses méthodes.
2. Ensuite, Python collecte des informations importantes sur la classe, telles que le nom de la classe, les classes de base dont elle hérite et tous ses attributs.
3. Après cela, Python transmet ces informations collectées à la métaclasse. La métaclasse est chargée de prendre ces informations et de créer l'objet de classe réel.
4. Enfin, la métaclasse crée et retourne la nouvelle classe.

Une métaclasse vous donne le pouvoir de personnaliser ce processus de création de classe. Vous pouvez modifier ou inspecter les classes pendant leur création, ce qui peut être très utile dans certains scénarios.

Visualisons cette relation pour faciliter la compréhension :

```
Metaclass → creates → Class → creates → Instance
```

Dans ce laboratoire (lab), nous allons créer notre propre métaclasse. En faisant cela, vous pourrez voir ce processus de création de classe en action et mieux comprendre le fonctionnement des métaclasses.
