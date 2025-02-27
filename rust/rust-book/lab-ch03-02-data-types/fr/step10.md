# Le type tableau

Une autre manière d'avoir une collection de plusieurs valeurs est avec un _tableau_. Contrairement à un tuple, chaque élément d'un tableau doit avoir le même type. Contrairement aux tableaux dans certains autres langages, les tableaux en Rust ont une longueur fixe.

Nous écrivons les valeurs dans un tableau comme une liste séparée par des virgules à l'intérieur de crochets :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```

Les tableaux sont utiles lorsque vous voulez que vos données soient allouées sur la pile plutôt que sur la pile (nous en parlerons plus en détail dans le chapitre 4) ou lorsque vous voulez vous assurer d'avoir toujours un nombre fixe d'éléments. Cependant, un tableau n'est pas aussi flexible que le type vecteur. Un _vecteur_ est un type de collection similaire fourni par la bibliothèque standard qui _peut_ grandir ou rétrécir en taille. Si vous n'êtes pas sûr de devoir utiliser un tableau ou un vecteur, il est probable que vous devriez utiliser un vecteur. Le chapitre 8 traite des vecteurs en détail.

Cependant, les tableaux sont plus utiles lorsque vous savez que le nombre d'éléments ne devra pas changer. Par exemple, si vous utilisez les noms des mois dans un programme, vous utiliseriez probablement un tableau plutôt qu'un vecteur car vous savez qu'il contiendra toujours 12 éléments :

```rust
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

Vous écrivez le type d'un tableau en utilisant des crochets avec le type de chaque élément, un point-virgule, puis le nombre d'éléments dans le tableau, comme ceci :

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Ici, `i32` est le type de chaque élément. Après le point-virgule, le nombre `5` indique que le tableau contient cinq éléments.

Vous pouvez également initialiser un tableau pour qu'il contienne la même valeur pour chaque élément en spécifiant la valeur initiale, suivie d'un point-virgule, puis la longueur du tableau entre crochets, comme montré ici :

```rust
let a = [3; 5];
```

Le tableau nommé `a` contiendra `5` éléments qui seront tous initialisés à la valeur `3`. Cela équivaut à écrire `let a = [3, 3, 3, 3, 3];` mais de manière plus concise.
