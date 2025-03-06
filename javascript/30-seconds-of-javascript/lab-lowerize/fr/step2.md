# Accéder aux clés d'un objet

Avant de pouvoir transformer les clés d'un objet, nous devons comprendre comment y accéder. JavaScript propose la méthode `Object.keys()`, qui renvoie un tableau contenant toutes les clés d'un objet.

Dans votre shell interactif Node.js, essayez ce qui suit :

```javascript
Object.keys(user);
```

Vous devriez voir une sortie comme celle-ci :

```
[ 'Name', 'AGE', 'Email' ]
```

Maintenant, essayons de convertir chaque clé en minuscules en utilisant la méthode `toLowerCase()`. Nous pouvons utiliser la méthode `map()` pour transformer chaque clé :

```javascript
Object.keys(user).map((key) => key.toLowerCase());
```

La sortie devrait être :

```
[ 'name', 'age', 'email' ]
```

Parfait ! Nous avons maintenant un tableau avec toutes les clés converties en minuscules. Cependant, nous devons encore créer un nouvel objet avec ces clés en minuscules et les valeurs originales. Pour cela, nous utiliserons la méthode `reduce()` dans l'étape suivante.

Comprenons la méthode `reduce()` avant de continuer. Cette méthode exécute une fonction de réduction sur chaque élément du tableau, ce qui donne une seule valeur de sortie.

Voici un exemple simple de `reduce()` :

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);

sum;
```

La sortie sera `10`, qui est la somme de tous les nombres du tableau. Le `0` dans la méthode `reduce()` est la valeur initiale de l'accumulateur.
