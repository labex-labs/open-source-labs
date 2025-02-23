# Fonction pour copier une chaîne de caractères dans le presse-papiers

Pour copier une chaîne de caractères dans le presse-papiers, utilisez la fonction `copyToClipboardAsync`. La fonction renvoie une promesse qui est résolue lorsque le contenu du presse-papiers a été mis à jour. Voici les étapes :

1. Vérifiez si l'API du presse-papiers est disponible en vérifiant si `Navigator`, `Navigator.clipboard` et `Navigator.clipboard.writeText` sont véridiques à l'aide d'une instruction `if`.
2. Si l'API du presse-papiers est disponible, utilisez `Clipboard.writeText()` pour écrire la valeur donnée, `str`, dans le presse-papiers.
3. Retournez le résultat de `Clipboard.writeText()`, qui est une promesse qui est résolue lorsque le contenu du presse-papiers a été mis à jour.
4. Si l'API du presse-papiers n'est pas disponible, rejetez la promesse avec un message d'erreur approprié à l'aide de `Promise.reject()`.
5. Si vous devez prendre en charge les anciens navigateurs, utilisez `Document.execCommand()` au lieu de `Clipboard.writeText()`. Vous pouvez en savoir plus sur cela dans le fragment de code `copyToClipboard`.

Voici la fonction `copyToClipboardAsync` :

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("L'API du presse-papiers n'est pas disponible.");
};
```

Pour utiliser la fonction, appelez `copyToClipboardAsync` avec la chaîne de caractères que vous voulez copier en tant qu'argument, comme ceci :

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' copié dans le presse-papiers.
```
