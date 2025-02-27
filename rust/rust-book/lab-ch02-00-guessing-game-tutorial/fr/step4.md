# Storing Values with Variables

Ensuite, nous allons créer une _variable_ pour stocker l'entrée de l'utilisateur, comme ceci :

```rust
let mut guess = String::new();
```

Maintenant, le programme devient intéressant! Il y a beaucoup de choses qui se passent dans cette petite ligne. Nous utilisons l'instruction `let` pour créer la variable. Voici un autre exemple :

```rust
let apples = 5;
```

Cette ligne crée une nouvelle variable nommée `apples` et l'associe à la valeur 5. En Rust, les variables sont immuables par défaut, ce qui signifie qu'une fois que nous avons donné une valeur à la variable, la valeur ne changera pas. Nous aborderons ce concept en détail dans "Variables and Mutability". Pour rendre une variable mutable, nous ajoutons `mut` avant le nom de la variable :

```rust
let apples = 5; // immutable
let mut bananas = 5; // mutable
```

> Note : La syntaxe `//` démarre un commentaire qui continue jusqu'à la fin de la ligne. Rust ignore tout ce qui se trouve dans les commentaires. Nous aborderons les commentaires en détail au chapitre 3.

Revenons au programme du jeu de devinette. Maintenant, vous savez que `let mut guess` introduira une variable mutable nommée `guess`. Le signe égal (`=`) indique à Rust que nous voulons lier quelque chose à la variable maintenant. À droite du signe égal se trouve la valeur à laquelle `guess` est lié, qui est le résultat de l'appel à `String::new`, une fonction qui renvoie une nouvelle instance d'un `String`. `String` est un type de chaîne de caractères fourni par la bibliothèque standard qui est un texte encodé en UTF-8 et pouvant grandir.

La syntaxe `::` dans la ligne `::new` indique que `new` est une fonction associée du type `String`. Une _fonction associée_ est une fonction qui est implémentée sur un type, dans ce cas `String`. Cette fonction `new` crée une nouvelle chaîne de caractères vide. Vous trouverez une fonction `new` sur de nombreux types car c'est un nom commun pour une fonction qui crée une nouvelle valeur d'un certain type.

En résumé, la ligne `let mut guess = String::new();` a créé une variable mutable qui est actuellement liée à une nouvelle instance vide d'un `String`. Phew!
