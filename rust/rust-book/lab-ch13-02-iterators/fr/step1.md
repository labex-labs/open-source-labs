# Processing a Series of Items with Iterators

Le patron d'itérateur vous permet d'effectuer une tâche sur une séquence d'éléments tour à tour. Un itérateur est responsable de la logique d'itération sur chaque élément et de la détermination du moment où la séquence est terminée. Lorsque vous utilisez des itérateurs, vous n'avez pas à réimplémenter cette logique vous-même.

En Rust, les itérateurs sont _paresseux_, ce qui signifie qu'ils n'ont aucun effet jusqu'à ce que vous appeliez des méthodes qui consomment l'itérateur pour l'épuiser. Par exemple, le code de la Liste 13-10 crée un itérateur sur les éléments du vecteur `v1` en appelant la méthode `iter` définie sur `Vec<T>`. Ce code seul ne fait rien de utile.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();
```

Liste 13-10: Création d'un itérateur

L'itérateur est stocké dans la variable `v1_iter`. Une fois que nous avons créé un itérateur, nous pouvons l'utiliser de diverses manières. Dans la Liste 3-5, nous avons itéré sur un tableau en utilisant une boucle `for` pour exécuter du code sur chacun de ses éléments. Sous le capot, cela a implicitement créé puis consommé un itérateur, mais nous avons passé sous silence jusqu'à présent la manière exacte dont cela fonctionne.

Dans l'exemple de la Liste 13-11, nous séparons la création de l'itérateur de son utilisation dans la boucle `for`. Lorsque la boucle `for` est appelée en utilisant l'itérateur dans `v1_iter`, chaque élément de l'itérateur est utilisé dans une itération de la boucle, ce qui imprime chaque valeur.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();

for val in v1_iter {
    println!("Got: {val}");
}
```

Liste 13-11: Utilisation d'un itérateur dans une boucle `for`

Dans les langages qui n'ont pas d'itérateurs fournis par leur bibliothèque standard, vous écririez probablement la même fonctionnalité en commençant une variable à l'index 0, en utilisant cette variable pour indexer dans le vecteur pour obtenir une valeur, et en incrémentant la valeur de la variable dans une boucle jusqu'à ce qu'elle atteigne le nombre total d'éléments dans le vecteur.

Les itérateurs gèrent toute cette logique pour vous, réduisant le code répétitif que vous pourriez potentiellement bousiller. Les itérateurs vous donnent plus de flexibilité pour utiliser la même logique avec de nombreux types différents de séquences, pas seulement les structures de données dans lesquelles vous pouvez indexer, comme les vecteurs. Examnons comment les itérateurs le font.
