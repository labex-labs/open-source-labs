# Parcourir une collection avec `for`

Vous pouvez choisir d'utiliser la construction `while` pour parcourir les éléments d'une collection, comme un tableau. Par exemple, la boucle dans la liste 3-4 affiche chaque élément du tableau `a`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("la valeur est : {}", a[index]);

        index += 1;
    }
}
```

Liste 3-4 : Parcourir chaque élément d'une collection en utilisant une boucle `while`

Ici, le code compte les éléments du tableau. Il commence à l'index `0`, puis boucle jusqu'à ce qu'il atteigne le dernier index du tableau (c'est-à-dire lorsque `index < 5` n'est plus `vrai`). En exécutant ce code, tous les éléments du tableau seront affichés :

```bash
$ cargo run
   Compilant boucles v0.1.0 (file:///projets/boucles)
    Terminé en mode développement [non optimisé + débogage] cibles(s) en 0.32s
     Exécution `target/debug/boucles`
la valeur est : 10
la valeur est : 20
la valeur est : 30
la valeur est : 40
la valeur est : 50
```

Les cinq valeurs du tableau apparaissent dans le terminal, comme attendu. Même si `index` atteindra une valeur de `5` à un moment donné, la boucle s'arrête avant d'essayer de récupérer une sixième valeur dans le tableau.

Cependant, cette approche est propice à des erreurs ; nous pourrions faire planter le programme si la valeur de l'index ou la condition de test est incorrecte. Par exemple, si vous changez la définition du tableau `a` pour qu'il ait quatre éléments mais oubliez de mettre à jour la condition en `while index < 4`, le code plantera. Elle est également lente, car le compilateur ajoute du code exécuté pendant l'exécution pour effectuer la vérification conditionnelle de savoir si l'index est dans les limites du tableau à chaque itération de la boucle.

En guise d'alternative plus concise, vous pouvez utiliser une boucle `for` et exécuter un certain code pour chaque élément d'une collection. Une boucle `for` ressemble au code de la liste 3-5.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("la valeur est : {element}");
    }
}
```

Liste 3-5 : Parcourir chaque élément d'une collection en utilisant une boucle `for`

Lorsque nous exécutons ce code, nous verrons la même sortie que dans la liste 3-4. Plus important, nous avons maintenant augmenté la sécurité du code et éliminé la possibilité de bugs qui pourraient résulter de dépasser la fin du tableau ou de ne pas aller assez loin et manquer certains éléments.

En utilisant la boucle `for`, vous n'aurez pas besoin de vous souvenir de changer tout autre code si vous changez le nombre de valeurs dans le tableau, contrairement à la méthode utilisée dans la liste 3-4.

La sécurité et la concision des boucles `for` en font la construction de boucle la plus couramment utilisée en Rust. Même dans des situations où vous voulez exécuter un certain code un certain nombre de fois, comme dans l'exemple de décompte qui utilisait une boucle `while` dans la liste 3-3, la plupart des Rustaceens utiliseraient une boucle `for`. La façon de le faire serait d'utiliser un `Range`, fourni par la bibliothèque standard, qui génère tous les nombres séquentiellement, en commençant par un nombre et en terminant avant un autre nombre.

Voici à quoi ressemblerait le décompte en utilisant une boucle `for` et une autre méthode dont nous n'avons pas encore parlé, `rev`, pour inverser la plage :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("DÉCOLAGE!!!");
}
```

Ce code est un peu plus agréable, non?
