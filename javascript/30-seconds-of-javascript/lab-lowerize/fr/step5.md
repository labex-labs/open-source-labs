# Création d'un module réutilisable

Maintenant que nous avons des fonctions opérationnelles, créons un fichier de module JavaScript réutilisable que nous pouvons importer dans d'autres projets.

Tout d'abord, quittons le shell interactif Node.js en appuyant deux fois sur Ctrl+C ou en tapant `.exit` puis en appuyant sur Entrée.

Maintenant, créons un nouveau fichier nommé `object-utils.js` dans le répertoire du projet :

1. Dans l'éditeur WebIDE, accédez au panneau de l'explorateur de fichiers à gauche
2. Cliquez avec le bouton droit dans le répertoire du projet et sélectionnez "Nouveau fichier"
3. Nommez le fichier `object-utils.js`
4. Ajoutez le code suivant au fichier :

```javascript
/**
 * Convertit toutes les clés d'un objet en minuscules
 * @param {Object} obj - L'objet d'entrée
 * @returns {Object} Un nouvel objet avec toutes les clés en minuscules
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Convertit récursivement toutes les clés d'un objet et de ses objets imbriqués en minuscules
 * @param {Object} obj - L'objet d'entrée
 * @returns {Object} Un nouvel objet avec toutes les clés en minuscules (y compris les objets imbriqués)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Vérifie si la valeur est un objet et non null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Exporte les fonctions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Maintenant, créons un fichier de test pour vérifier que notre module fonctionne correctement. Créez un nouveau fichier nommé `test.js` :

1. Dans l'éditeur WebIDE, accédez au panneau de l'explorateur de fichiers à gauche
2. Cliquez avec le bouton droit dans le répertoire du projet et sélectionnez "Nouveau fichier"
3. Nommez le fichier `test.js`
4. Ajoutez le code suivant au fichier :

```javascript
// Importe les fonctions de notre module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test avec un objet simple
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Objet original :");
console.log(user);

console.log("\nObjet avec des clés en minuscules :");
console.log(lowerizeKeys(user));

// Test avec un objet imbriqué
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nObjet imbriqué :");
console.log(nestedObject);

console.log("\nObjet imbriqué avec des clés en minuscules (superficiel) :");
console.log(lowerizeKeys(nestedObject));

console.log("\nObjet imbriqué avec des clés en minuscules (profonde) :");
console.log(deepLowerizeKeys(nestedObject));
```

Maintenant, exécutons le fichier de test :

```bash
node test.js
```

Vous devriez voir une sortie similaire à :

```
Objet original :
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Objet avec des clés en minuscules :
{ name: 'John', age: 30, email: 'john@example.com' }

Objet imbriqué :
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Objet imbriqué avec des clés en minuscules (superficiel) :
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Objet imbriqué avec des clés en minuscules (profonde) :
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

Félicitations ! Vous avez créé avec succès un module JavaScript réutilisable avec des fonctions pour convertir les clés d'objets en minuscules. Ce module peut maintenant être importé dans n'importe lequel de vos projets JavaScript.
