# Comprendre le problème et configurer l'environnement

Avant de commencer à coder, comprenons ce que notre fonction `replaceLast` devrait faire :

1. Accepter trois paramètres :

   - `str` : La chaîne de caractères d'entrée à modifier
   - `pattern` : La sous-chaîne ou l'expression régulière (regular expression) à rechercher
   - `replacement` : La chaîne de caractères à utiliser pour remplacer la dernière occurrence

2. Retourner une nouvelle chaîne de caractères avec la dernière occurrence du motif remplacée.

Créons un fichier JavaScript pour implémenter notre fonction :

1. Naviguez jusqu'au répertoire du projet dans l'explorateur de fichiers de WebIDE.
2. Créez un nouveau fichier nommé `replaceLast.js` dans le répertoire `replace-last`.
3. Ajoutez la structure de base suivante au fichier :

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

Pour vérifier que tout est configuré correctement, ajoutons un test simple :

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Maintenant, exécutons notre code pour voir la sortie actuelle :

1. Ouvrez le terminal dans WebIDE.
2. Naviguez jusqu'au répertoire `replace-last` :
   ```bash
   cd ~/project/replace-last
   ```
3. Exécutez le fichier JavaScript en utilisant Node.js :
   ```bash
   node replaceLast.js
   ```

Vous devriez voir `Hello world world` dans la sortie car notre fonction retourne actuellement simplement la chaîne de caractères originale sans apporter de modifications.
