# Conditionnels

> Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.

Les conditionnels sont des structures de code utilisées pour tester si une expression renvoie `true` ou non. Une forme très courante de conditionnels est l'instruction `if...else`. Par exemple :

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

L'expression à l'intérieur de `if ()` est le test. Cela utilise l'opérateur d'égalité stricte (comme décrit ci-dessus) pour comparer la variable `iceCream` avec la chaîne de caractères `chocolate` pour voir si les deux sont égaux. Si cette comparaison renvoie `true`, le premier bloc de code s'exécute. Si la comparaison n'est pas vraie, le second bloc de code, après l'instruction `else`, s'exécute à la place.
