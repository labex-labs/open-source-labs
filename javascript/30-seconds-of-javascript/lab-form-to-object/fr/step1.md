# Conversion d'un formulaire en objet

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Vous pouvez encoder un ensemble d'éléments de formulaire sous forme d'un objet en utilisant les étapes suivantes :

1. Utilisez le constructeur `FormData` pour convertir le formulaire HTML en `FormData`.
2. Convertissez le `FormData` en tableau à l'aide de `Array.from()`.
3. Collectez l'objet à partir du tableau à l'aide de `Array.prototype.reduce()`.

Voici un extrait de code d'exemple :

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

Pour convertir un formulaire spécifique, vous pouvez appeler la fonction `formToObject` et passer l'élément de formulaire en tant qu'argument :

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
