# let Statements

Avant ce chapitre, nous avions seulement explicitement discuté de l'utilisation de motifs avec `match` et `if let`, mais en fait, nous les avons utilisés dans d'autres endroits également, y compris dans les instructions `let`. Par exemple, considérez cette affectation de variable simple avec `let` :

```rust
let x = 5;
```

Chaque fois que vous avez utilisé une instruction `let` comme celle-ci, vous avez utilisé des motifs, même si vous ne vous en étiez peut-être pas rendu compte! Plus formellement, une instruction `let` ressemble à ceci :

```rust
let MOTIF = EXPRESSION;
```

Dans des instructions comme `let x = 5;` avec un nom de variable dans la case MOTIF, le nom de variable n'est qu'une forme particulièrement simple d'un motif. Rust compare l'expression avec le motif et attribue tous les noms qu'il trouve. Ainsi, dans l'exemple `let x = 5;`, `x` est un motif qui signifie "lier ce qui correspond ici à la variable `x`". Comme le nom `x` est le motif complet, ce motif signifie effectivement "lier tout à la variable `x`, quelle que soit la valeur".

Pour voir plus clairement l'aspect de correspondance de motifs de `let`, considérez le listing 18-4, qui utilise un motif avec `let` pour déstructurer un tuple.

```rust
let (x, y, z) = (1, 2, 3);
```

Listing 18-4: Using a pattern to destructure a tuple and create three variables at once

Ici, nous comparons un tuple avec un motif. Rust compare la valeur `(1, 2, 3)` avec le motif `(x, y, z)` et constate que la valeur correspond au motif, en ce sens qu'il constate que le nombre d'éléments est le même dans les deux, donc Rust lie `1` à `x`, `2` à `y` et `3` à `z`. Vous pouvez considérer ce motif de tuple comme un emboîtement de trois motifs de variable individuels à l'intérieur.

Si le nombre d'éléments dans le motif ne correspond pas au nombre d'éléments dans le tuple, le type global ne correspondra pas et nous obtiendrons une erreur du compilateur. Par exemple, le listing 18-5 montre une tentative de déstructurer un tuple avec trois éléments en deux variables, ce qui ne fonctionnera pas.

```rust
let (x, y) = (1, 2, 3);
```

Listing 18-5: Incorrectly constructing a pattern whose variables don't match the number of elements in the tuple

Tenter de compiler ce code résulte dans cette erreur de type :

```bash
error[E0308]: mismatched types
 --> src/main.rs:2:9
  |
2 |     let (x, y) = (1, 2, 3);
  |         ^^^^^^   --------- this expression has type `({integer}, {integer},
{integer})`
  |         |
  |         expected a tuple with 3 elements, found one with 2 elements
  |
  = note: expected tuple `({integer}, {integer}, {integer})`
             found tuple `(_, _)`
```

Pour corriger l'erreur, nous pourrions ignorer une ou plusieurs des valeurs dans le tuple en utilisant `_` ou `..`, comme vous le verrez dans "Ignoring Values in a Pattern". Si le problème est qu'il y a trop de variables dans le motif, la solution est de faire correspondre les types en supprimant des variables de sorte que le nombre de variables soit égal au nombre d'éléments dans le tuple.
