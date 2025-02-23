# Conversion de radians en degrés

Pour convertir un angle de radians en degrés, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la formule suivante : `degrees = radians * (180 / Math.PI)`
3. Remplacez `radians` dans la formule par la valeur que vous voulez convertir.
4. Le résultat sera en degrés.

Voici un exemple :

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

Cela convertira `π/2` radians en `90` degrés.
