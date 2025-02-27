# Types de données

Toute valeur en Rust est d'un certain **type de données**, qui indique à Rust quel type de données est spécifié afin qu'il sache comment travailler avec ces données. Nous examinerons deux sous-ensembles de types de données : scalaires et composites.

Gardez à l'esprit que Rust est un langage **statiquement typé**, ce qui signifie qu'il doit connaître les types de toutes les variables à la compilation. Le compilateur peut généralement déduire quel type nous souhaitons utiliser en fonction de la valeur et de la manière dont nous l'utilisons. Dans les cas où plusieurs types sont possibles, par exemple lorsque nous avons converti une `String` en un type numérique en utilisant `parse` dans "Comparer la supposition au nombre secret", nous devons ajouter une annotation de type, comme ceci :

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

Si nous n'ajoutons pas l'annotation de type `: u32` montrée dans le code précédent, Rust affichera l'erreur suivante, ce qui signifie que le compilateur a besoin de plus d'informations de notre part pour savoir quel type nous souhaitons utiliser :

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

Vous verrez différentes annotations de type pour d'autres types de données.
