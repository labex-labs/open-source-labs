# Instructions et expressions

Les corps de fonctions sont composés d'une série d'instructions éventuellement terminées par une expression. Jusqu'à présent, les fonctions que nous avons abordées n'ont pas inclus une expression de fin, mais vous avez vu une expression comme partie d'une instruction. Étant donné que Rust est un langage basé sur les expressions, cette distinction est importante à comprendre. D'autres langages n'ont pas les mêmes distinctions, donc examinons ce qu'est une instruction et une expression et comment leurs différences affectent les corps de fonctions.

- **Instructions** : sont des instructions qui effectuent une action et ne renvoient pas de valeur.
- **Expressions** : évaluent à une valeur résultante. Examnons quelques exemples.

Nous avons déjà utilisé des instructions et des expressions. Créer une variable et lui assigner une valeur avec le mot clé `let` est une instruction. Dans la liste 3-1, `let y = 6;` est une instruction.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

Liste 3-1 : Une déclaration de fonction `main` contenant une instruction

Les définitions de fonctions sont également des instructions ; l'exemple précédent dans son ensemble est une instruction en elle-même.

Les instructions ne renvoient pas de valeurs. Par conséquent, vous ne pouvez pas assigner une instruction `let` à une autre variable, comme le tente de le faire le code suivant ; vous obtiendrez une erreur :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

Lorsque vous exécutez ce programme, l'erreur que vous obtiendrez ressemble à ceci :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

L'instruction `let y = 6` ne renvoie pas de valeur, donc il n'y a rien à quoi `x` puisse être lié. Cela est différent de ce qui se passe dans d'autres langages, tels que C et Ruby, où l'affectation renvoie la valeur de l'affectation. Dans ces langages, vous pouvez écrire `x = y = 6` et que `x` et `y` aient tous les deux la valeur `6` ; ce n'est pas le cas en Rust.

Les expressions évaluent à une valeur et constituent la majeure partie du reste du code que vous écrirez en Rust. Considérez une opération mathématique, telle que `5 + 6`, qui est une expression qui évalue à la valeur `11`. Les expressions peuvent faire partie d'instructions : dans la liste 3-1, le `6` dans l'instruction `let y = 6;` est une expression qui évalue à la valeur `6`. Appeler une fonction est une expression. Appeler une macro est une expression. Un nouveau bloc de portée créé avec des accolades est une expression, par exemple :

Nom de fichier : `src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

L'expression \[2\] est un bloc qui, dans ce cas, évalue à `4`. Cette valeur est liée à `y` comme partie de l'instruction `let` \[1\]. Notez la ligne sans point-virgule à la fin \[3\], qui est différente de la plupart des lignes que vous avez vu jusqu'à présent. Les expressions ne comportent pas de point-virgule de fin. Si vous ajoutez un point-virgule à la fin d'une expression, vous la transformez en une instruction, et elle ne renverra alors pas de valeur. Gardez cela à l'esprit lorsque vous explorerez les valeurs de retour de fonctions et les expressions dans la suite.
