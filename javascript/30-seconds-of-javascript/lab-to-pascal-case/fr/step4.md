# Création de la fonction complète toPascalCase

Maintenant que nous comprenons tous les éléments nécessaires, créons une fonction complète `toPascalCase` qui peut gérer n'importe quelle chaîne de caractères en entrée.

1. Créons un fichier JavaScript pour enregistrer notre fonction. Quittez votre session Node.js en appuyant deux fois sur Ctrl+C ou en tapant `.exit`.

2. Dans l'éditeur WebIDE, créez un nouveau fichier en cliquant sur "File" > "New File" dans le menu supérieur.

3. Enregistrez le fichier sous le nom `pascalCase.js` dans le répertoire `/home/labex/project`.

4. Copiez et collez le code suivant dans l'éditeur :

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Enregistrez le fichier en appuyant sur Ctrl+S ou en sélectionnant "File" > "Save" dans le menu.

6. Exécutez le fichier en utilisant Node.js en ouvrant le terminal et en tapant :

```bash
node pascalCase.js
```

Vous devriez voir la sortie suivante :

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Notre fonction `toPascalCase` fonctionne maintenant correctement. Revoyons comment elle fonctionne :

1. Nous utilisons une expression régulière pour trouver les mots dans la chaîne de caractères en entrée, quelle que soit le délimiteur utilisé.
2. Nous vérifions si des mots ont été trouvés. Sinon, nous renvoyons une chaîne de caractères vide.
3. Nous utilisons `map()` pour mettre en majuscule chaque mot et `join('')` pour les combiner sans séparateurs.
4. Le résultat est une chaîne de caractères en casse Pascal (Pascal case) où chaque mot commence par une lettre majuscule et le reste est en minuscules.
