# Accéder à ou modifier une variable statique mutable

Dans ce livre, nous n'avons pas encore parlé des variables globales, que Rust prend en charge mais qui peuvent poser des problèmes avec les règles de propriété de Rust. Si deux threads accèdent à la même variable globale mutable, cela peut entraîner une course de données.

En Rust, les variables globales sont appelées _variables statiques_. Le Listing 19-9 montre un exemple de déclaration et d'utilisation d'une variable statique avec une slice de chaîne de caractères comme valeur.

Nom du fichier : `src/main.rs`

```rust
static HELLO_WORLD: &str = "Hello, world!";

fn main() {
    println!("value is: {HELLO_WORLD}");
}
```

Listing 19-9 : Définition et utilisation d'une variable statique immuable

Les variables statiques sont similaires aux constantes, que nous avons discutées dans "Constantes". Les noms des variables statiques sont en `SCREAMING_SNAKE_CASE` par convention. Les variables statiques ne peuvent stocker que des références avec la durée de vie `'static`, ce qui signifie que le compilateur Rust peut déterminer la durée de vie et que nous n'avons pas besoin d'y annoter explicitement. Accéder à une variable statique immuable est sécurisé.

Une différence subtile entre les constantes et les variables statiques immuables est que les valeurs dans une variable statique ont une adresse fixe en mémoire. Utiliser la valeur accédera toujours aux mêmes données. Les constantes, en revanche, sont autorisées à dupliquer leurs données chaque fois qu'elles sont utilisées. Une autre différence est que les variables statiques peuvent être mutables. Accéder et modifier les variables statiques mutables est _non sécurisé_. Le Listing 19-10 montre comment déclarer, accéder et modifier une variable statique mutable nommée `COUNTER`.

Nom du fichier : `src/main.rs`

```rust
static mut COUNTER: u32 = 0;

fn add_to_count(inc: u32) {
    unsafe {
        COUNTER += inc;
    }
}

fn main() {
    add_to_count(3);

    unsafe {
        println!("COUNTER: {COUNTER}");
    }
}
```

Listing 19-10 : Lire ou écrire dans une variable statique mutable est non sécurisé.

Comme pour les variables régulières, nous spécifions la mutabilité en utilisant le mot clé `mut`. Tout code qui lit ou écrit dans `COUNTER` doit être à l'intérieur d'un bloc `unsafe`. Ce code compile et affiche `COUNTER: 3` comme prévu car c'est un code mono-threadé. Avoir plusieurs threads accéder à `COUNTER` entraînerait probablement des courses de données.

Avec des données mutables accessibles globalement, il est difficile de s'assurer qu'il n'y a pas de courses de données, c'est pourquoi Rust considère les variables statiques mutables comme non sécurisées. Lorsque cela est possible, il est préférable d'utiliser les techniques de concurrence et les pointeurs intelligents sécurisés par threads que nous avons discutés au Chapitre 16 afin que le compilateur vérifie que l'accès aux données à partir de différents threads est effectué de manière sécurisée.
