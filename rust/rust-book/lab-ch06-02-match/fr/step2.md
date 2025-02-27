# Modèles qui se lient à des valeurs

Une autre fonctionnalité pratique des branches de `match` est qu'elles peuvent se lier aux parties des valeurs qui correspondent au modèle. C'est ainsi que nous pouvons extraire des valeurs des variantes d'enumération.

En guise d'exemple, modifions l'une de nos variantes d'enumération pour qu'elle contienne des données à l'intérieur. De 1999 à 2008, la monnaie américaine a frappé des quarters avec des dessins différents pour chacune des 50 états américains sur un côté. Aucune autre pièce n'a reçu des dessins d'états, donc seul le quarter a cette valeur supplémentaire. Nous pouvons ajouter cette information à notre `enum` en changeant la variante `Quarter` pour inclure une valeur `UsState` stockée à l'intérieur, ce que nous avons fait dans la liste 6-4.

```rust
#[derive(Debug)] // afin que nous puissions examiner l'état dans un instant
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

Liste 6-4 : Un enum `Coin` dans lequel la variante `Quarter` contient également une valeur `UsState`

Imaginons qu'un ami essaye de collecter les 50 quarters d'états. Pendant que nous trions notre monnaie de poche par type de pièce, nous allons également annoncer le nom de l'état associé à chaque quarter afin que si c'est un état que notre ami n'a pas, il puisse l'ajouter à sa collection.

Dans l'expression `match` de ce code, nous ajoutons une variable appelée `state` au modèle qui correspond aux valeurs de la variante `Coin::Quarter`. Lorsqu'un `Coin::Quarter` correspond, la variable `state` se lira à la valeur de l'état de ce quarter. Ensuite, nous pouvons utiliser `state` dans le code de cette branche, comme ceci :

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

Si nous appelions `value_in_cents(Coin::Quarter(UsState::Alaska))`, `coin` serait `Coin::Quarter(UsState::Alaska)`. Lorsque nous comparons cette valeur avec chacune des branches de `match`, aucune d'entre elles ne correspond jusqu'à ce que nous arrivions à `Coin::Quarter(state)`. A ce moment-là, la liaison pour `state` sera la valeur `UsState::Alaska`. Nous pouvons ensuite utiliser cette liaison dans l'expression `println!`, permettant ainsi d'obtenir la valeur d'état interne de la variante `Coin` pour `Quarter`.
