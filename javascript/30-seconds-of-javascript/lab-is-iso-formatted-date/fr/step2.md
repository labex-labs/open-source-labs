# Création d'une fonction pour valider les chaînes de caractères de date au format ISO

Dans cette étape, nous allons créer une fonction JavaScript qui vérifie si une chaîne de caractères donnée est au format ISO 8601 valide.

## Création de la fonction de validation

Créons un nouveau fichier JavaScript pour notre validateur de date ISO :

1. Dans l'IDE Web, cliquez sur l'icône de l'Explorateur dans la barre latérale gauche.
2. Cliquez avec le bouton droit dans l'explorateur de fichiers et sélectionnez "Nouveau fichier".
3. Nommez le fichier `isISODate.js` et appuyez sur Entrée.
4. Ajoutez le code suivant au fichier :

```javascript
/**
 * Vérifie si une chaîne de caractères est une chaîne de caractères de date formatée selon le standard ISO 8601 valide
 * @param {string} val - La chaîne de caractères à vérifier
 * @return {boolean} - Retourne true si la chaîne de caractères est au format ISO, false sinon
 */
const isISOString = (val) => {
  // Crée un objet Date à partir de la chaîne de caractères d'entrée
  const d = new Date(val);

  // Vérifie si la date est valide (pas NaN) et si la chaîne de caractères ISO correspond à l'original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Exporte la fonction pour pouvoir l'utiliser ailleurs
module.exports = isISOString;
```

Examinons comment cette fonction fonctionne :

1. `new Date(val)` crée un objet Date à partir de la chaîne de caractères d'entrée.
2. `d.valueOf()` retourne la valeur numérique du timestamp (en millisecondes depuis le 1er janvier 1970).
3. `Number.isNaN(d.valueOf())` vérifie si la date est invalide (NaN signifie "Not a Number").
4. `d.toISOString() === val` vérifie que la conversion de l'objet Date en une chaîne de caractères ISO correspond à l'entrée originale.

## Test de notre fonction

Maintenant, créons un fichier de test simple pour tester notre fonction :

1. Créez un autre fichier nommé `testISO.js`.
2. Ajoutez le code suivant :

```javascript
// Importe notre fonction isISOString
const isISOString = require("./isISODate");

// Teste avec une date formatée selon le standard ISO valide
console.log("Test d'une date ISO valide :");
console.log("2020-10-12T10:10:10.000Z");
console.log("Résultat :", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Teste avec un format invalide
console.log("Test d'une date non ISO :");
console.log("2020-10-12");
console.log("Résultat :", isISOString("2020-10-12"));
```

3. Exécutez le fichier de test en utilisant Node.js :

```bash
node testISO.js
```

Vous devriez voir une sortie similaire à :

```
Test d'une date ISO valide :
2020-10-12T10:10:10.000Z
Résultat : true

Test d'une date non ISO :
2020-10-12
Résultat : false
```

Cela montre que notre fonction identifie correctement que "2020-10-12T10:10:10.000Z" est une date formatée selon le standard ISO valide, tandis que "2020-10-12" ne l'est pas.
