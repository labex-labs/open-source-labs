# Comprendre le format de date ISO et les objets Date en JavaScript

Avant de commencer à coder, comprenons ce que représente le format de date ISO 8601 et comment JavaScript gère les dates.

## Le format de date ISO 8601

Le format ISO 8601 est une norme internationale pour représenter les dates et les heures. Le format ISO simplifié étendu ressemble à ceci :

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

Où :

- `YYYY` représente l'année (quatre chiffres)
- `MM` représente le mois (deux chiffres)
- `DD` représente le jour (deux chiffres)
- `T` est un caractère littéral séparant la date et l'heure
- `HH` représente les heures (deux chiffres)
- `mm` représente les minutes (deux chiffres)
- `ss` représente les secondes (deux chiffres)
- `sss` représente les millisecondes (trois chiffres)
- `Z` indique le fuseau horaire UTC (heure Zulu)

Par exemple, `2023-05-12T14:30:15.123Z` représente le 12 mai 2023, à 14 h 30 min 15 s et 123 millisecondes UTC.

## L'objet Date en JavaScript

JavaScript fournit un objet `Date` intégré pour travailler avec les dates et les heures. Lorsque vous créez un nouvel objet `Date`, vous pouvez lui passer une chaîne de caractères formatée selon le standard ISO :

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

Ouvrons le terminal et pratiquons le travail avec les objets Date :

1. Ouvrez le Terminal en cliquant sur le menu Terminal en haut de l'IDE Web.
2. Tapez `node` et appuyez sur Entrée pour démarrer le shell interactif Node.js.
3. Créez un nouvel objet Date pour l'heure actuelle :

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. Convertissez cet objet Date en une chaîne de caractères au format ISO :

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

Vous devriez voir une sortie similaire à :

```
2023-05-12T14:30:15.123Z
```

5. Créez un objet Date à partir d'une chaîne de caractères au format ISO :

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

Cela démontre comment JavaScript peut analyser et créer des objets Date à partir de chaînes de caractères formatées selon le standard ISO.
