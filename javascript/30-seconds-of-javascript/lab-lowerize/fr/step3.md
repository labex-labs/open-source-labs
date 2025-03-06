# Création de la fonction de conversion en minuscules

Maintenant que nous savons comment accéder aux clés d'un objet et utiliser la méthode `reduce()`, créons une fonction qui convertit toutes les clés d'un objet en minuscules.

Dans votre shell interactif Node.js, définissez la fonction suivante :

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Analysons ce que fait cette fonction :

1. `Object.keys(obj)` récupère toutes les clés de l'objet d'entrée
2. `.reduce()` transforme ces clés en un nouvel objet
3. Pour chaque clé, nous créons une nouvelle entrée dans l'objet accumulateur (`acc`) avec :
   - La clé convertie en minuscules en utilisant `key.toLowerCase()`
   - La valeur originale de l'objet d'entrée (`obj[key]`)
4. Nous commençons avec un objet vide `{}` comme valeur initiale pour l'accumulateur
5. Enfin, nous renvoyons l'accumulateur, qui est notre nouvel objet avec des clés en minuscules

Maintenant, testons notre fonction avec l'objet `user` que nous avons créé précédemment :

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

Vous devriez voir la sortie suivante :

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

Parfait ! Toutes les clés sont maintenant en minuscules.

Essayons un autre exemple pour nous assurer que notre fonction fonctionne correctement :

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

La sortie devrait être :

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Notre fonction fonctionne correctement pour différents objets avec divers styles de casse de clés.
