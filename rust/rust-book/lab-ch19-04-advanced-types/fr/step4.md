# Le type `!` qui ne renvoie jamais

Rust a un type spécial nommé `!` qui est connu en termes de théorie des types comme le _type vide_ car il n'a pas de valeurs. Nous préférons l'appeler _type jamais_ car il prend la place du type de retour lorsqu'une fonction ne retournera jamais. Voici un exemple :

```rust
fn bar() ->! {
    --snip--
}
```

Ce code est lu comme "la fonction `bar` renvoie jamais". Les fonctions qui renvoient jamais sont appelées _fonctions divergentes_. Nous ne pouvons pas créer de valeurs du type `!`, donc `bar` ne peut jamais renvoyer.

Mais à quoi sert un type pour lequel vous ne pouvez jamais créer de valeurs? Rappelez-vous le code de la liste 2-5, partie du jeu de devinette de nombre ; nous en reproduisons un peu ici dans la liste 19-26.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Liste 19-26 : Un `match` avec un bras qui se termine par `continue`

À l'époque, nous avons sauté certains détails de ce code. Dans "La construction de flux de contrôle `match`", nous avons discuté que les bras d'un `match` doivent tous renvoyer le même type. Ainsi, par exemple, le code suivant ne fonctionne pas :

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

Le type de `guess` dans ce code devrait être à la fois un entier _et_ une chaîne de caractères, et Rust exige que `guess` ait seulement un type. Alors, que renvoie `continue`? Comment avons-nous été autorisés à renvoyer un `u32` à partir d'un bras et à avoir un autre bras qui se termine par `continue` dans la liste 19-26?

Comme vous avez peut-être deviné, `continue` a une valeur de type `!`. C'est-à-dire que lorsque Rust calcule le type de `guess`, il examine les deux bras du `match`, le premier avec une valeur de type `u32` et le second avec une valeur de type `!`. Comme `!` ne peut jamais avoir de valeur, Rust décide que le type de `guess` est `u32`.

La manière formelle de décrire ce comportement est que les expressions de type `!` peuvent être contraintes à n'importe quel autre type. Nous sommes autorisés à terminer ce bras de `match` par `continue` car `continue` ne renvoie pas de valeur ; au lieu de cela, elle renvoie le contrôle au début de la boucle, donc dans le cas `Err`, nous n'assignons jamais de valeur à `guess`.

Le type jamais est également utile avec la macro `panic!`. Rappelez-vous la fonction `unwrap` que nous appelons sur des valeurs de type `Option<T>` pour produire une valeur ou déclencher une panique avec cette définition :

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "appelé `Option::unwrap()` sur une valeur `None`"
            ),
        }
    }
}
```

Dans ce code, la même chose se passe que dans le `match` de la liste 19-26 : Rust voit que `val` a le type `T` et que `panic!` a le type `!`, donc le résultat de l'expression `match` globale est `T`. Ce code fonctionne car `panic!` ne produit pas de valeur ; elle termine le programme. Dans le cas `None`, nous ne renverrons pas de valeur à partir de `unwrap`, donc ce code est valide.

Une dernière expression qui a le type `!` est une boucle `loop` :

    print!("pour toujours ");

    loop {
        print!("et toujours ");
    }

Ici, la boucle ne se termine jamais, donc `!` est la valeur de l'expression. Cependant, ce ne serait pas vrai si nous avions inclus un `break`, car la boucle se terminerait lorsqu'elle arriverait au `break`.
