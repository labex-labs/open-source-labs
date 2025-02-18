# Comment obtenir la taille en octets d'une chaîne de caractères en JavaScript

Pour obtenir la taille en octets d'une chaîne de caractères en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Convertissez la chaîne de caractères en un [objet `Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
3. Utilisez `Blob.size` pour obtenir la longueur de la chaîne de caractères en octets.

Voici le code JavaScript pour obtenir la taille en octets d'une chaîne de caractères :

```js
const byteSize = (str) => new Blob([str]).size;
```

Vous pouvez tester cette fonction avec les exemples suivants :

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
