# Pointeurs de fonction

Nous avons parlé de la manière de passer des closures à des fonctions ; vous pouvez également passer des fonctions ordinaires à des fonctions! Cette technique est utile lorsque vous voulez passer une fonction que vous avez déjà définie plutôt que de définir une nouvelle closure. Les fonctions se coercitent en le type `fn` (avec une _f_ en minuscules), ne pas confondre avec le trait de closure `Fn`. Le type `fn` est appelé un _pointeur de fonction_. Passer des fonctions avec des pointeurs de fonction vous permettra d'utiliser des fonctions comme arguments pour d'autres fonctions.

La syntaxe pour spécifier qu'un paramètre est un pointeur de fonction est similaire à celle des closures, comme montré dans la Liste 19-27, où nous avons défini une fonction `add_one` qui ajoute 1 à son paramètre. La fonction `do_twice` prend deux paramètres : un pointeur de fonction vers n'importe quelle fonction qui prend un paramètre de type `i32` et renvoie un `i32`, et une valeur `i32`. La fonction `do_twice` appelle la fonction `f` deux fois, en lui passant la valeur `arg`, puis ajoute les deux résultats d'appel de fonction ensemble. La fonction `main` appelle `do_twice` avec les arguments `add_one` et `5`.

Nom de fichier : `src/main.rs`

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

Liste 19-27 : Utilisation du type `fn` pour accepter un pointeur de fonction en tant qu'argument

Ce code affiche `The answer is: 12`. Nous spécifions que le paramètre `f` dans `do_twice` est un `fn` qui prend un paramètre de type `i32` et renvoie un `i32`. Nous pouvons ensuite appeler `f` dans le corps de `do_twice`. Dans `main`, nous pouvons passer le nom de la fonction `add_one` comme premier argument à `do_twice`.

Contrairement aux closures, `fn` est un type plutôt qu'un trait, donc nous spécifions `fn` comme type de paramètre directement plutôt que de déclarer un paramètre de type générique avec l'un des traits `Fn` comme limite de trait.

Les pointeurs de fonction implémentent les trois traits de closure (`Fn`, `FnMut` et `FnOnce`), ce qui signifie que vous pouvez toujours passer un pointeur de fonction en tant qu'argument pour une fonction qui attend une closure. Il est préférable d'écrire des fonctions en utilisant un type générique et l'un des traits de closure de sorte que vos fonctions puissent accepter à la fois des fonctions et des closures.

Cela étant dit, un exemple de cas où vous voudriez seulement accepter `fn` et non des closures est lorsqu'il s'agit d'interagir avec du code externe qui n'a pas de closures : les fonctions C peuvent accepter des fonctions en tant qu'arguments, mais C n'a pas de closures.

En tant qu'exemple de cas où vous pourriez utiliser soit une closure définie en ligne soit une fonction nommée, regardons une utilisation de la méthode `map` fournie par le trait `Iterator` dans la bibliothèque standard. Pour utiliser la fonction `map` pour transformer un vecteur de nombres en un vecteur de chaînes de caractères, nous pourrions utiliser une closure, comme ceci :

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(|i| i.to_string())
 .collect();
```

Ou nous pourrions nommer une fonction comme argument de `map` au lieu de la closure, comme ceci :

```rust
let list_of_numbers = vec![1, 2, 3];
let list_of_strings: Vec<String> = list_of_numbers
 .iter()
 .map(ToString::to_string)
 .collect();
```

Notez que nous devons utiliser la syntaxe qualifiée en entier dont nous avons parlé dans "Traits avancés" car il existe plusieurs fonctions disponibles nommées `to_string`.

Ici, nous utilisons la fonction `to_string` définie dans le trait `ToString`, que la bibliothèque standard a implémenté pour tout type qui implémente `Display`.

Rappelez-vous de "Valeurs d'enumération" que le nom de chaque variant d'enumération que nous définissons devient également une fonction d'initialisation. Nous pouvons utiliser ces fonctions d'initialisation comme pointeurs de fonction qui implémentent les traits de closure, ce qui signifie que nous pouvons spécifier les fonctions d'initialisation comme arguments pour des méthodes qui prennent des closures, comme ceci :

```rust
enum Status {
    Value(u32),
    Stop,
}

let list_of_statuses: Vec<Status> = (0u32..20)
 .map(Status::Value)
 .collect();
```

Ici, nous créons des instances `Status::Value` en utilisant chaque valeur `u32` dans la plage sur laquelle `map` est appelé en utilisant la fonction d'initialisation de `Status::Value`. Certaines personnes préfèrent ce style et certaines personnes préfèrent utiliser des closures. Elles se compilent en même code, donc utilisez le style qui est le plus clair pour vous.
