# Comprendre la casse Pascal (Pascal case) et configurer l'environnement

La casse Pascal est une convention de nommage où :

- La première lettre de chaque mot est en majuscule
- Aucun espace, tiret ou underscore n'est utilisé entre les mots
- Toutes les autres lettres sont en minuscules

Par exemple :

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

Commençons par configurer notre environnement de développement.

1. Ouvrez le terminal depuis l'interface WebIDE en cliquant sur "Terminal" dans la barre de menu supérieure.

2. Démarrez une session interactive Node.js en tapant la commande suivante dans le terminal et en appuyant sur Entrée :

```bash
node
```

Vous devriez voir l'invite Node.js (`>`) apparaître, ce qui indique que vous êtes maintenant dans l'environnement interactif Node.js.

3. Essayons une simple manipulation de chaîne de caractères pour nous échauffer. Tapez le code suivant à l'invite Node.js :

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

La sortie devrait être :

```
John doe
```

Cet exemple simple montre comment mettre en majuscule la première lettre d'une chaîne de caractères. Nous avons utilisé :

- `charAt(0)` pour obtenir le premier caractère
- `toUpperCase()` pour le convertir en majuscule
- `slice(1)` pour obtenir le reste de la chaîne
- La concaténation avec `+` pour les combiner

Ces méthodes de manipulation de chaînes de caractères seront utiles lors de la création de notre convertisseur en casse Pascal.
