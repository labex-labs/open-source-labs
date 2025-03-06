# Comprendre les objets en JavaScript

Avant de commencer à convertir les clés d'un objet en minuscules, comprenons ce que sont les objets JavaScript et comment nous pouvons les manipuler.

En JavaScript, un objet est une collection de paires clé-valeur. Les clés sont des chaînes de caractères (ou des Symboles), et les valeurs peuvent être de n'importe quel type de données, y compris d'autres objets.

Commençons par ouvrir le shell interactif Node.js :

1. Ouvrez le terminal dans votre WebIDE
2. Tapez `node` puis appuyez sur Entrée

Vous devriez maintenant voir l'invite Node.js (`>`), qui vous permet de taper directement du code JavaScript.

Créons un objet simple avec des clés en casse mixte :

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

Tapez ce code dans l'invite Node.js puis appuyez sur Entrée. Pour voir l'objet, tapez simplement `user` puis appuyez sur Entrée :

```javascript
user;
```

Vous devriez voir la sortie suivante :

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

Comme vous pouvez le voir, cet objet a des clés avec différents styles de casse. Dans l'étape suivante, nous allons apprendre à accéder à ces clés et à les convertir en minuscules.
