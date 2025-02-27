# Déballez les options et utilisez les valeurs par défaut

Il existe plusieurs façons de déballer une `Option` et de recourir à une valeur par défaut si elle est `None`. Pour choisir celle qui répond à nos besoins, nous devons prendre en compte les points suivants :

- avons-nous besoin d'une évaluation eager ou lazy?
- avons-nous besoin de conserver la valeur vide d'origine intacte ou de la modifier in situ?

## `or()` est chaînable, évalue de manière eager, conserve la valeur vide intacte

`or()` est chaînable et évalue son argument de manière eager, comme le montre l'exemple suivant. Notez que parce que les arguments de `or` sont évalués de manière eager, la variable passée à `or` est déplacée.

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let orange = Some(Fruit::Orange);
    let no_fruit: Option<Fruit> = None;

    let first_available_fruit = no_fruit.or(orange).or(apple);
    println!("first_available_fruit: {:?}", first_available_fruit);
    // first_available_fruit: Some(Orange)

    // `or` déplace son argument.
    // Dans l'exemple ci-dessus, `or(orange)` a retourné un `Some`, donc `or(apple)` n'a pas été invoqué.
    // Mais la variable nommée `apple` a été déplacée malgré tout et ne peut plus être utilisée.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: décommentez la ligne ci-dessus pour voir l'erreur du compilateur
 }
```

## `or_else()` est chaînable, évalue de manière lazy, conserve la valeur vide intacte

Une autre alternative est d'utiliser `or_else`, qui est également chaînable et évalue de manière lazy, comme le montre l'exemple suivant :

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let no_fruit: Option<Fruit> = None;
    let get_kiwi_as_fallback = || {
        println!("Providing kiwi as fallback");
        Some(Fruit::Kiwi)
    };
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Some(Fruit::Lemon)
    };

    let first_available_fruit = no_fruit
     .or_else(get_kiwi_as_fallback)
     .or_else(get_lemon_as_fallback);
    println!("first_available_fruit: {:?}", first_available_fruit);
    // Providing kiwi as fallback
    // first_available_fruit: Some(Kiwi)
}
```

## `get_or_insert()` évalue de manière eager, modifie la valeur vide in situ

Pour vous assurer qu'une `Option` contient une valeur, vous pouvez utiliser `get_or_insert` pour la modifier in situ avec une valeur de repli, comme le montre l'exemple suivant. Notez que `get_or_insert` évalue son paramètre de manière eager, donc la variable `apple` est déplacée :

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let mut my_fruit: Option<Fruit> = None;
    let apple = Fruit::Apple;
    let first_available_fruit = my_fruit.get_or_insert(apple);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    println!("my_fruit is: {:?}", my_fruit);
    // first_available_fruit is: Apple
    // my_fruit is: Some(Apple)
    //println!("Variable named `apple` is moved: {:?}", apple);
    // TODO: décommentez la ligne ci-dessus pour voir l'erreur du compilateur
}
```

## `get_or_insert_with()` évalue de manière lazy, modifie la valeur vide in situ

Au lieu de fournir explicitement une valeur de repli, nous pouvons passer une closure à `get_or_insert_with`, comme suit :

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let mut my_fruit: Option<Fruit> = None;
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Fruit::Lemon
    };
    let first_available_fruit = my_fruit
     .get_or_insert_with(get_lemon_as_fallback);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    println!("my_fruit is: {:?}", my_fruit);
    // Providing lemon as fallback
    // first_available_fruit is: Lemon
    // my_fruit is: Some(Lemon)

    // Si l'Option a une valeur, elle est laissée inchangée et la closure n'est pas invoquée
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // La sortie est la suivante. Notez que la closure `get_lemon_as_fallback` n'est pas invoquée
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```
