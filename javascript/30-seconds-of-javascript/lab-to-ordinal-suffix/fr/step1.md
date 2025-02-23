# Fonction pour convertir des nombres en suffixe ordinal

Pour convertir un nombre en suffixe ordinal, utilisez la fonction `toOrdinalSuffix`.

- Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
- La fonction prend un nombre en entrée et le renvoie sous forme de chaîne de caractères avec le suffixe d'indicateur ordinal correct.
- Utilisez l'opérateur modulo (`%`) pour trouver les valeurs des chiffres unitaires et des dizaines.
- Trouvez les motifs ordinaux auxquels les chiffres correspondent.
- Si le chiffre se trouve dans le motif des ados, utilisez l'ordinal des ados.

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["er", "ème", "ème", "ème"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

Voici un exemple d'utilisation de la fonction `toOrdinalSuffix`:

```js
toOrdinalSuffix("123"); // '123ème'
```
