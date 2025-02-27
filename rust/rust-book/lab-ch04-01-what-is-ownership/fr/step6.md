# Variables et données interagissant avec le concept de "move"

Plusieurs variables peuvent interagir avec les mêmes données de différentes manières en Rust. Regardons un exemple utilisant un entier dans la liste 4-2.

```rust
let x = 5;
let y = x;
```

Liste 4-2 : Attribution de la valeur entière de la variable `x` à `y`

On peut probablement deviner ce qui se passe : "lier la valeur `5` à `x` ; puis faire une copie de la valeur dans `x` et la lier à `y`." Maintenant, nous avons deux variables, `x` et `y`, et les deux valent `5`. C'est effectivement ce qui se passe, car les entiers sont des valeurs simples de taille connue et fixe, et ces deux valeurs `5` sont empilées.

Maintenant, regardons la version avec `String` :

```rust
let s1 = String::from("hello");
let s2 = s1;
```

Cela semble très similaire, donc on pourrait supposer que le fonctionnement serait le même : c'est-à-dire que la deuxième ligne ferait une copie de la valeur dans `s1` et la lierait à `s2`. Mais ce n'est pas exactement ce qui se passe.

Regardez la figure 4-1 pour voir ce qui se passe avec `String` en coulisse. Un `String` est composé de trois parties, montrées à gauche : un pointeur vers la mémoire qui contient le contenu de la chaîne, une longueur et une capacité. Ce groupe de données est stocké sur la pile. À droite se trouve la mémoire sur le tas qui contient le contenu.

Figure 4-1 : Représentation en mémoire d'un `String` contenant la valeur `"hello"` lié à `s1`

La longueur est la quantité de mémoire, en octets, que le contenu du `String` utilise actuellement. La capacité est la quantité totale de mémoire, en octets, que le `String` a reçue de l'allocateur. La différence entre la longueur et la capacité est importante, mais pas dans ce contexte, donc pour l'instant, il est bon d'ignorer la capacité.

Lorsque nous assignons `s1` à `s2`, les données du `String` sont copiées, ce qui signifie que nous copions le pointeur, la longueur et la capacité qui sont sur la pile. Nous ne copions pas les données sur le tas que le pointeur référence. En d'autres termes, la représentation des données en mémoire ressemble à la figure 4-2.

Figure 4-2 : Représentation en mémoire de la variable `s2` qui a une copie du pointeur, de la longueur et de la capacité de `s1`

La représentation ne ressemble _pas_ à la figure 4-3, qui est ce que la mémoire serait si Rust copiait également les données du tas. Si Rust faisait cela, l'opération `s2 = s1` pourrait être très coûteuse en termes de performance d'exécution si les données sur le tas étaient volumineuses.

Figure 4-3 : Une autre possibilité de ce que `s2 = s1` pourrait faire si Rust copiait également les données du tas

Plus tôt, nous avons dit que lorsque une variable sort de portée, Rust appelle automatiquement la fonction `drop` et nettoie la mémoire du tas pour cette variable. Mais la figure 4-2 montre les deux pointeurs de données pointant vers le même emplacement. C'est un problème : lorsque `s2` et `s1` sortent de portée, elles essaieront toutes les deux de libérer la même mémoire. Ceci est connu sous le nom d'erreur de _double free_ et est l'un des bugs de sécurité mémoire dont nous avons parlé précédemment. Libérer la mémoire deux fois peut entraîner une corruption de la mémoire, ce qui peut potentiellement entraîner des vulnérabilités de sécurité.

Pour assurer la sécurité mémoire, après la ligne `let s2 = s1;`, Rust considère `s1` comme plus valide. Par conséquent, Rust n'a pas besoin de libérer quoi que ce soit lorsque `s1` sort de portée. Vérifions ce qui se passe lorsque vous essayez d'utiliser `s1` après la création de `s2` ; cela ne fonctionnera pas :

```rust
let s1 = String::from("hello");
let s2 = s1;

println!("{s1}, world!");
```

Vous obtiendrez une erreur comme celle-ci car Rust vous empêche d'utiliser la référence invalidée :

```bash
error[E0382]: borrow of moved value: `s1`
 --> src/main.rs:5:28
  |
2 |     let s1 = String::from("hello");
  |         -- move occurs because `s1` has type `String`, which
 does not implement the `Copy` trait
3 |     let s2 = s1;
  |              -- value moved here
4 |
5 |     println!("{s1}, world!");
  |                ^^ value borrowed here after move
```

Si vous avez entendu les termes de _copie superficielle_ et _copie profonde_ dans d'autres langages, le concept de copier le pointeur, la longueur et la capacité sans copier les données semble probablement comme faire une copie superficielle. Mais parce que Rust invalide également la première variable, au lieu d'être appelé une copie superficielle, cela est connu sous le nom de _move_. Dans cet exemple, nous dirions que `s1` a été _déplacé_ dans `s2`. Donc, ce qui se passe effectivement est montré dans la figure 4-4.

Figure 4-4 : Représentation en mémoire après que `s1` a été invalidé

Cela résout notre problème! Avec seulement `s2` valide, lorsqu'elle sort de portée, elle seule libérera la mémoire, et nous avons fini.

En outre, il y a un choix de conception implicite dans tout cela : Rust ne créera jamais automatiquement de "copies profondes" de vos données. Par conséquent, toute copie _automatique_ peut être considérée comme peu coûteuse en termes de performance d'exécution.
