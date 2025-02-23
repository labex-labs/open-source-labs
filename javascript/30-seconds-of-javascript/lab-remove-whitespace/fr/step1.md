# Fonction pour supprimer les espaces blancs

Pour supprimer les espaces blancs d'une chaîne de caractères, utilisez la fonction suivante.

- Utilisez `String.prototype.replace()` avec une expression régulière pour remplacer toutes les occurrences de caractères d'espace blanc par une chaîne de caractères vide.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## Explication de l'expression régulière

- `/\s+/g` se décompose comme suit :
  - `\s` : Correspond à tout caractère d'espace blanc (espaces, tabulations, retours à la ligne)
  - `+` : Correspond à une ou plusieurs occurrences du caractère précédent
  - `/g` : Drapeau global - correspond à toutes les occurrences dans la chaîne, pas seulement à la première

## Référence rapide d'expressions régulières

Les motifs d'espace blanc communs :

- `\s` - correspond à tout espace blanc (espace, tabulation, nouvelle ligne)
- `\t` - correspond aux caractères de tabulation
- `\n` - correspond aux caractères de nouvelle ligne
- `\r` - correspond aux retours chariots
- (espace) - ne correspond qu'aux caractères d'espace

Par exemple,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// Plus d'exemples :
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
