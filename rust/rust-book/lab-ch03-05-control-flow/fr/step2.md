# Expressions `if`

Une expression `if` vous permet de créer des branches dans votre code en fonction de conditions. Vous fournissez une condition et ensuite vous indiquez : "Si cette condition est remplie, exécutez ce bloc de code. Si la condition n'est pas remplie, n'exécutez pas ce bloc de code."

Créez un nouveau projet appelé `branches` dans votre répertoire `projet` pour explorer l'expression `if`. Dans le fichier `src/main.rs`, entrez le code suivant :

```bash
cd ~/projet
cargo new branches
```

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition était vraie");
    } else {
        println!("condition était fausse");
    }
}
```

Toutes les expressions `if` commencent par le mot-clé `if`, suivi d'une condition. Dans cet exemple, la condition vérifie si la variable `number` a une valeur inférieure à 5. Nous plaçons le bloc de code à exécuter si la condition est `vraie` immédiatement après la condition, à l'intérieur des accolades. Les blocs de code associés aux conditions dans les expressions `if` sont parfois appelés _bras_, tout comme les bras dans les expressions `match` que nous avons discutées dans "Comparer la proposition avec le nombre secret".

Facultativement, nous pouvons également inclure une expression `else`, comme nous l'avons fait ici, pour donner au programme un bloc de code alternatif à exécuter si la condition se révèle être `fausse`. Si vous ne fournissez pas d'expression `else` et que la condition est `fausse`, le programme saute simplement le bloc `if` et passe au reste du code.

Essayez d'exécuter ce code ; vous devriez voir la sortie suivante :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition était vraie
```

Essayons de modifier la valeur de `number` pour une valeur qui rend la condition `fausse` pour voir ce qui se passe :

```rust
    let number = 7;
```

Exécutez le programme à nouveau et regardez la sortie :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition était fausse
```

Il est également important de noter que la condition dans ce code _doit_ être un `bool`. Si la condition n'est pas un `bool`, nous obtiendrons une erreur. Par exemple, essayez d'exécuter le code suivant :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number était égal à trois");
    }
}
```

La condition `if` évalue à une valeur de `3` cette fois-ci, et Rust génère une erreur :

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projets/branches)
error[E0308]: types non compatibles
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ valeur attendue : `bool`, valeur trouvée : entier
```

L'erreur indique que Rust attendait un `bool` mais a reçu un entier. Contrairement à des langages tels que Ruby et JavaScript, Rust ne tentera pas automatiquement de convertir des types non booléens en booléen. Vous devez être explicite et fournir toujours à `if` une condition de type booléen. Si nous voulons que le bloc de code `if` s'exécute seulement lorsqu'un nombre est différent de `0`, par exemple, nous pouvons modifier l'expression `if` comme suit :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number!= 0 {
        println!("number était différent de zéro");
    }
}
```

En exécutant ce code, il affichera `number était différent de zéro`.
