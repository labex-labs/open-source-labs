# Générer un code couleur hexadécimal aléatoire dans le Terminal/SSH

Pour générer un code couleur hexadécimal aléatoire dans le Terminal/SSH, suivez les étapes ci-dessous :

1. Ouvrez le Terminal/SSH.
2. Tapez `node`.
3. Utilisez le code suivant pour générer un nombre hexadécimal aléatoire de 24 bits (6 \* 4 bits) :

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. Pour générer un code couleur hexadécimal aléatoire, appelez la fonction `randomHexColorCode()`.

Exemple :

```js
randomHexColorCode(); // '#e34155'
```

Cela générera un code couleur hexadécimal aléatoire que vous pouvez utiliser dans vos projets de codage.
