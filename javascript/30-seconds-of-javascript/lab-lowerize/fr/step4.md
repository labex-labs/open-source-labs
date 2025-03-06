# Gestion des cas limites

Notre fonction fonctionne bien pour les objets simples, mais qu'en est-il des cas plus complexes ? Explorons certains cas limites et voyons comment notre fonction les gère.

## Objets vides

Tout d'abord, testons avec un objet vide :

```javascript
lowerizeKeys({});
```

La sortie devrait être un objet vide :

```
{}
```

## Objets avec des objets imbriqués

Et si l'objet contient des objets imbriqués ? Essayons cela :

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

La sortie sera :

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

Notez que seule la clé de premier niveau `User` est convertie en minuscules. Les clés à l'intérieur des objets imbriqués restent inchangées.

Pour gérer les objets imbriqués, nous devrons modifier notre fonction pour traiter récursivement tous les objets. Créons une version améliorée :

```javascript
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
```

Cette fonction améliorée :

1. Vérifie si chaque valeur est également un objet (et non un tableau ou null)
2. Si c'est le cas, elle s'appelle elle-même de manière récursive sur cet objet imbriqué
3. Sinon, elle utilise la valeur originale

Testons-la avec notre objet imbriqué :

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

Maintenant, vous devriez voir toutes les clés converties en minuscules, même dans les objets imbriqués :

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

Bravo ! Vous avez créé une fonction avancée capable de gérer les objets imbriqués.
