# Générer un UUID dans un navigateur

Pour générer un UUID conforme à [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) version 4 dans un navigateur, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez la méthode `Crypto.getRandomValues()` pour générer un UUID.
3. Convertissez l'UUID en une chaîne hexadécimale à l'aide de la méthode `Number.prototype.toString()`.
4. Implémentez le code suivant :

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Appelez la fonction `UUIDGeneratorBrowser()` pour générer un UUID. Par exemple, `UUIDGeneratorBrowser()` retournerait `'7982fcfe-5721-4632-bede-6000885be57d'`.
