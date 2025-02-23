# Génération de nombres aléatoires gaussiens à l'aide de la transformation Box-Muller

Pour générer des nombres aléatoires gaussiens (distribués normalement) à l'aide de la transformation Box-Muller, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le extrait de code fourni qui utilise la transformation Box-Muller pour générer des nombres aléatoires avec une distribution gaussienne.
3. La fonction `randomGauss()` fournie dans l'extrait de code génère un nombre aléatoire avec une distribution gaussienne.
4. La sortie de la fonction `randomGauss()` est un nombre compris entre 0 et 1.
5. La sortie peut être utilisée pour diverses applications, telles que des simulations statistiques, l'analyse de données et l'apprentissage automatique.

```js
const randomGauss = () => {
  const theta = 2 * Math.PI * Math.random();
  const rho = Math.sqrt(-2 * Math.log(1 - Math.random()));
  return (rho * Math.cos(theta)) / 10.0 + 0.5;
};
```

Utilisation de l'exemple :

```js
randomGauss(); // 0,5
```
