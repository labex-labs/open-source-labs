# Paramètres

Nous pouvons définir des fonctions qui ont des _paramètres_, qui sont des variables spéciales qui font partie de la signature d'une fonction. Lorsqu'une fonction a des paramètres, vous pouvez lui fournir des valeurs concrètes pour ces paramètres. Technologiquement, les valeurs concrètes sont appelées _arguments_, mais dans la conversation ordinaire, les gens ont tendance à utiliser les mots _paramètre_ et _argument_ de manière interchangeable pour les variables dans la définition d'une fonction ou les valeurs concrètes passées lorsqu'on appelle une fonction.

Dans cette version de `another_function`, nous ajoutons un paramètre :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

Essayez d'exécuter ce programme ; vous devriez obtenir la sortie suivante :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

La déclaration de `another_function` a un paramètre nommé `x`. Le type de `x` est spécifié comme étant `i32`. Lorsque nous passons `5` à `another_function`, la macro `println!` met `5` à l'endroit où la paire d'accolades contenant `x` était dans la chaîne de formatage.

Dans les signatures de fonctions, vous _devez_ déclarer le type de chaque paramètre. Cette décision est délibérée dans la conception de Rust : exiger des annotations de type dans les définitions de fonctions signifie que le compilateur a presque jamais besoin que vous les utilisiez ailleurs dans le code pour comprendre quel type vous voulez dire. Le compilateur est également capable de donner des messages d'erreur plus utiles s'il connaît les types que la fonction attend.

Lorsque vous définissez plusieurs paramètres, séparez les déclarations de paramètres par des virgules, comme ceci :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

Cet exemple crée une fonction nommée `print_labeled_measurement` avec deux paramètres. Le premier paramètre est nommé `value` et est un `i32`. Le second est nommé `unit_label` et est de type `char`. La fonction imprime ensuite le texte contenant à la fois la `value` et le `unit_label`.

Essayons d'exécuter ce code. Remplacez le programme actuellement dans le fichier `src/main.rs` de votre projet _functions_ par l'exemple précédent et exécutez-le avec `cargo run` :

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

Parce que nous avons appelé la fonction avec `5` comme valeur pour `value` et `'h'` comme valeur pour `unit_label`, la sortie du programme contient ces valeurs.
