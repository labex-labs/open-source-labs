# Prise en main des objets Date en JavaScript

JavaScript propose un objet `Date` intégré qui nous permet de manipuler les dates et les heures. Avant de calculer la différence entre des dates, comprenons d'abord comment créer et manipuler des objets `Date` en JavaScript.

## Démarrage de l'environnement Node.js

Commençons par ouvrir l'environnement interactif de Node.js :

1. Ouvrez le Terminal en cliquant sur le menu Terminal en haut de l'IDE Web.
2. Tapez la commande suivante et appuyez sur Entrée :

```bash
node
```

Vous devriez maintenant voir l'invite Node.js (`>`), ce qui indique que vous êtes dans l'environnement interactif JavaScript. Cela vous permet d'exécuter du code JavaScript directement dans le terminal.

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## Création d'objets Date

En JavaScript, nous pouvons créer un nouvel objet `Date` de plusieurs manières :

```javascript
// Date et heure actuelles
let now = new Date();
console.log(now);

// Date et heure spécifiques (année, mois [0-11], jour, heure, minute, seconde)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 15 janvier 2023, 10:30:45
console.log(specificDate);

// Date à partir d'une chaîne de caractères
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

Essayez de taper chacun de ces exemples dans l'environnement Node.js et observez la sortie.

Notez qu'en JavaScript, les mois sont indexés à partir de zéro, ce qui signifie que janvier est 0, février est 1, et ainsi de suite.

## Obtention d'un horodatage (timestamp) à partir d'objets Date

Chaque objet `Date` en JavaScript stocke en interne l'heure sous forme du nombre de millisecondes écoulées depuis le 1er janvier 1970 (UTC). Cela est connu sous le nom d'horodatage (timestamp).

```javascript
let now = new Date();
console.log(now.getTime()); // Obtenir l'horodatage en millisecondes
```

Cet horodatage sera utile pour calculer la différence entre des dates.
