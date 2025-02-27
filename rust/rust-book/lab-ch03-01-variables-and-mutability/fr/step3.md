# Ombre (Shadowing)

Comme vous l'avez vu dans le tutoriel du jeu de devinette au chapitre 2, vous pouvez déclarer une nouvelle variable avec le même nom qu'une variable précédente. Les Rustaceans disent que la première variable est **ombragée** par la seconde, ce qui signifie que la seconde variable est celle que le compilateur verra lorsque vous utiliserez le nom de la variable. En effet, la seconde variable obscurcit la première, prenant toutes les utilisations du nom de variable pour elle-même jusqu'à ce qu'elle soit elle-même ombragée ou que la portée se termine. Nous pouvons ombrager une variable en utilisant le même nom de variable et en répétant l'utilisation du mot clé `let` comme suit :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

Ce programme lie d'abord `x` à une valeur de `5`. Ensuite, il crée une nouvelle variable `x` en répétant `let x =`, prenant la valeur initiale et ajoutant `1` de sorte que la valeur de `x` soit alors `6`. Ensuite, à l'intérieur d'une portée interne créée avec les accolades, la troisième instruction `let` ombre également `x` et crée une nouvelle variable, multipliant la valeur précédente par `2` pour donner à `x` une valeur de `12`. Lorsque cette portée est terminée, l'ombre interne se termine et `x` revient à être `6`. Lorsque nous exécutons ce programme, il affichera ceci :

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

L'ombre est différente de la marque d'une variable comme `mut` car nous obtiendrons une erreur de compilation si nous essayons accidentellement de réaffecter cette variable sans utiliser le mot clé `let`. En utilisant `let`, nous pouvons effectuer quelques transformations sur une valeur mais laisser la variable être immuable après que ces transformations ont été effectuées.

L'autre différence entre `mut` et l'ombre est que parce que nous créons effectivement une nouvelle variable lorsque nous utilisons à nouveau le mot clé `let`, nous pouvons changer le type de la valeur mais réutiliser le même nom. Par exemple, disons que notre programme demande à un utilisateur de montrer combien d'espaces ils veulent entre certains textes en saisissant des caractères d'espace, puis que nous voulons stocker cette entrée comme un nombre :

```rust
let spaces = "   ";
let spaces = spaces.len();
```

La première variable `spaces` est de type chaîne de caractères et la seconde variable `spaces` est de type nombre. L'ombre nous épargne donc de devoir trouver des noms différents, tels que `spaces_str` et `spaces_num` ; au lieu de cela, nous pouvons réutiliser le nom plus simple `spaces`. Cependant, si nous essayons d'utiliser `mut` pour cela, comme montré ici, nous obtiendrons une erreur de compilation :

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

L'erreur indique que nous ne sommes pas autorisés à modifier le type d'une variable :

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

Maintenant que nous avons exploré la façon dont les variables fonctionnent, regardons les différents types de données qu'elles peuvent avoir.
