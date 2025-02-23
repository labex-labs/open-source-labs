# Comment trouver les facteurs premiers d'un nombre en utilisant l'algorithme de division par tâtonnement

Pour trouver les facteurs premiers d'un nombre donné en utilisant l'algorithme de division par tâtonnement, suivez ces étapes :

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- Utilisez une boucle `while` pour itérer sur tous les facteurs premiers possibles, en commençant par `2`.
- Si le facteur actuel, `f`, divise exactement `n`, ajoutez `f` au tableau de facteurs et divisez `n` par `f`. Sinon, incrémentez `f` de un.
- La fonction `primeFactors` prend un nombre `n` en entrée et renvoie un tableau de ses facteurs premiers.
- Pour tester la fonction, appelez `primeFactors(147)` et elle renverra `[3, 7, 7]`.

Voici le code JavaScript :

```js
const primeFactors = (n) => {
  let a = [],
    f = 2;
  while (n > 1) {
    if (n % f === 0) {
      a.push(f);
      n /= f;
    } else {
      f++;
    }
  }
  return a;
};
```

N'oubliez pas de remplacer `147` par le nombre pour lequel vous voulez trouver les facteurs premiers.
