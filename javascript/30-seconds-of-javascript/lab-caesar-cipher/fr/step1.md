# Chiffre de César

Pour utiliser le chiffre de César, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Appelez la fonction `caesarCipher` avec la chaîne à chiffrer ou à déchiffrer, la valeur de décalage et un booléen indiquant s'il faut déchiffrer ou non.
3. La fonction `caesarCipher` utilise l'opérateur modulo (`%`) et l'opérateur ternaire (`?`) pour calculer la clé de chiffrement ou de déchiffrement correcte.
4. Elle utilise l'opérateur de propagation (`...`) et `Array.prototype.map()` pour itérer sur les lettres de la chaîne donnée.
5. Elle utilise `String.prototype.charCodeAt()` et `String.fromCharCode()` pour convertir chaque lettre de manière appropriée, en ignorant les caractères spéciaux, les espaces, etc.
6. Elle utilise `Array.prototype.join()` pour combiner toutes les lettres en une chaîne.
7. Si vous voulez déchiffrer une chaîne chiffrée, passez `true` au dernier paramètre, `decrypt`, lors de l'appel de la fonction `caesarCipher`.

Voici le code de la fonction `caesarCipher` :

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

Voici quelques exemples d'utilisation de la fonction `caesarCipher` :

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
