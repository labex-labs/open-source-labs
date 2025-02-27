# La construction de flux de contrôle match

Rust possède une construction de flux de contrôle extrêmement puissante appelée `match` qui vous permet de comparer une valeur avec une série de modèles et d'exécuter ensuite du code en fonction du modèle qui correspond. Les modèles peuvent être composés de valeurs littérales, de noms de variables, de jokers et de nombreuses autres choses ; le chapitre 18 couvre tous les différents types de modèles et ce qu'ils font. Le pouvoir de `match` vient de l'expressivité des modèles et du fait que le compilateur confirme que tous les cas possibles sont traités.

Imaginez une expression `match` comme une machine de tri de pièces : les pièces glissent le long d'une piste avec des trous de tailles différentes, et chaque pièce tombe dans le premier trou qu'elle rencontre et dans lequel elle rentre. De la même manière, les valeurs passent par chaque modèle dans une `match`, et au premier modèle auquel la valeur "convient", la valeur tombe dans le bloc de code associé pour être utilisé pendant l'exécution.

Parlant de pièces, utilisons-les comme exemple avec `match`! Nous pouvons écrire une fonction qui prend une pièce américaine inconnue et, de manière similaire à la machine de comptage, détermine laquelle elle est et renvoie sa valeur en cents, comme montré dans la liste 6-3.

```rust
1 enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
  2 match coin {
      3 Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

Liste 6-3 : Un enum et une expression `match` qui a les variantes de l'enum comme modèles

Analysons la `match` dans la fonction `value_in_cents`. Tout d'abord, nous listons le mot clé `match` suivi d'une expression, qui dans ce cas est la valeur `coin` \[2\]. Cela semble très similaire à une expression utilisée avec `if`, mais il y a une grande différence : avec `if`, l'expression doit renvoyer une valeur booléenne, mais ici elle peut renvoyer n'importe quel type. Le type de `coin` dans cet exemple est l'enum `Coin` que nous avons défini à \[1\].

Ensuite, viennent les branches de la `match`. Une branche a deux parties : un modèle et du code. La première branche ici a un modèle qui est la valeur `Coin::Penny` puis l'opérateur `=>` qui sépare le modèle et le code à exécuter \[3\]. Le code dans ce cas est juste la valeur `1`. Chaque branche est séparée de la suivante par une virgule.

Lorsque l'expression `match` s'exécute, elle compare la valeur résultante avec le modèle de chaque branche, dans l'ordre. Si un modèle correspond à la valeur, le code associé à ce modèle est exécuté. Si ce modèle ne correspond pas à la valeur, l'exécution continue avec la branche suivante, tout comme dans une machine de tri de pièces. Nous pouvons avoir autant de branches que nécessaire : dans la liste 6-3, notre `match` a quatre branches.

Le code associé à chaque branche est une expression, et la valeur résultante de l'expression dans la branche correspondante est la valeur qui est renvoyée pour l'expression `match` entière.

Nous n'utilisons généralement pas les accolades si le code de la branche de la `match` est court, comme c'est le cas dans la liste 6-3 où chaque branche ne renvoie qu'une valeur. Si vous voulez exécuter plusieurs lignes de code dans une branche de la `match`, vous devez utiliser les accolades, et la virgule suivant la branche est alors facultative. Par exemple, le code suivant affiche "Pièce de centime porte-bonheur!" chaque fois que la méthode est appelée avec une `Coin::Penny`, mais renvoie toujours la dernière valeur du bloc, `1` :

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
