# Comment convertir une chaîne de caractères en un tableau de caractères en JavaScript

Pour convertir une chaîne de caractères en un tableau de caractères en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez l'opérateur de propagation (`...`) pour convertir la chaîne de caractères en un tableau de caractères.
3. Définissez une fonction appelée `toCharArray` qui prend une chaîne de caractères en argument et renvoie un tableau de ses caractères.
4. Appelez la fonction `toCharArray` avec la chaîne de caractères que vous voulez convertir en argument.
5. La fonction renverra un tableau de caractères.

Voici le code :

```js
const toCharArray = (s) => [...s];

toCharArray("hello"); // ['h', 'e', 'l', 'l', 'o']
```
