# Conversion hexadécimal en RGB

Pour convertir un code couleur hexadécimal (avec ou sans préfixe `#`) en une chaîne RGB, suivez les étapes suivantes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur de décalage arithmétique vers la droite bit à bit et masquez les bits avec l'opérateur `&` (ET).
3. Si le code couleur est à 3 chiffres, convertissez-le d'abord en version à 6 chiffres.
4. Si une valeur alpha est fournie avec le code hexadécimal à 6 chiffres, renvoyez une chaîne `rgba()`.

Voici le code JavaScript pour la conversion :

```js
const hexToRGB = (hex) => {
  let alpha = false,
    h = hex.slice(hex.startsWith("#") ? 1 : 0);
  if (h.length === 3) h = [...h].map((x) => x + x).join("");
  else if (h.length === 8) alpha = true;
  h = parseInt(h, 16);
  return (
    "rgb" +
    (alpha ? "a" : "") +
    "(" +
    (h >>> (alpha ? 24 : 16)) +
    ", " +
    ((h & (alpha ? 0x00ff0000 : 0x00ff00)) >>> (alpha ? 16 : 8)) +
    ", " +
    ((h & (alpha ? 0x0000ff00 : 0x0000ff)) >>> (alpha ? 8 : 0)) +
    (alpha ? `, ${h & 0x000000ff}` : "") +
    ")"
  );
};
```

Vous pouvez utiliser la fonction `hexToRGB` avec les exemples suivants :

```js
hexToRGB("#27ae60ff"); // 'rgba(39, 174, 96, 255)'
hexToRGB("27ae60"); // 'rgb(39, 174, 96)'
hexToRGB("#fff"); // 'rgb(255, 255, 255)'
```
