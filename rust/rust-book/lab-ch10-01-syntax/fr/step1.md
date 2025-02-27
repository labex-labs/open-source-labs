# Removing Duplication by Extracting a Function

Les génériques nous permettent de remplacer des types spécifiques par un placeholder qui représente plusieurs types pour éliminer la duplication de code. Avant d'approfondir la syntaxe des génériques, regardons tout d'abord comment éliminer la duplication d'une manière qui ne concerne pas les types génériques en extrayant une fonction qui remplace des valeurs spécifiques par un placeholder qui représente plusieurs valeurs. Ensuite, nous appliquerons la même technique pour extraire une fonction générique! En étudiant comment reconnaître le code dupliqué que vous pouvez extraire dans une fonction, vous commencerez à reconnaître le code dupliqué qui peut utiliser des génériques.

Nous commencerons par le programme court de la Liste 10-1 qui trouve le plus grand nombre dans une liste.

Nom de fichier : `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Liste 10-1 : Trouver le plus grand nombre dans une liste de nombres

Nous stockons une liste d'entiers dans la variable `number_list` \[1\] et plaçons une référence au premier nombre de la liste dans une variable appelée `largest` \[2\]. Nous parcourons ensuite tous les nombres de la liste \[3\], et si le nombre actuel est supérieur au nombre stocké dans `largest` \[4\], nous remplaçons la référence dans cette variable \[5\]. Cependant, si le nombre actuel est inférieur ou égal au plus grand nombre vu jusqu'à présent, la variable ne change pas et le code passe au nombre suivant de la liste. Après avoir considéré tous les nombres de la liste, `largest` devrait faire référence au plus grand nombre, qui est dans ce cas 100.

Nous avons maintenant la tâche de trouver le plus grand nombre dans deux listes différentes de nombres. Pour ce faire, nous pouvons choisir de dupliquer le code de la Liste 10-1 et d'utiliser la même logique à deux endroits différents du programme, comme montré dans la Liste 10-2.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

Liste 10-2 : Code pour trouver le plus grand nombre dans _deux_ listes de nombres

Bien que ce code fonctionne, dupliquer le code est fastidieux et propice aux erreurs. Nous devons également nous souvenir de mettre à jour le code en plusieurs endroits lorsque nous voulons le modifier.

Pour éliminer cette duplication, nous allons créer une abstraction en définissant une fonction qui opère sur toute liste d'entiers passée en paramètre. Cette solution rend notre code plus clair et nous permet d'exprimer de manière abstraite le concept de trouver le plus grand nombre dans une liste.

Dans la Liste 10-3, nous extrayons le code qui trouve le plus grand nombre dans une fonction appelée `largest`. Ensuite, nous appelons la fonction pour trouver le plus grand nombre dans les deux listes de la Liste 10-2. Nous pourrions également utiliser la fonction sur toute autre liste de valeurs `i32` que nous pourrions avoir à l'avenir.

Nom de fichier : `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

Liste 10-3 : Code abstrait pour trouver le plus grand nombre dans deux listes

La fonction `largest` a un paramètre appelé `list`, qui représente toute tranche concrète de valeurs `i32` que nous pourrions passer à la fonction. En conséquence, lorsque nous appelons la fonction, le code s'exécute sur les valeurs spécifiques que nous passons.

En résumé, voici les étapes que nous avons suivies pour changer le code de la Liste 10-2 à la Liste 10-3 :

1.  Identifier le code dupliqué.
2.  Extraire le code dupliqué dans le corps de la fonction et spécifier les entrées et les valeurs de retour de ce code dans la signature de la fonction.
3.  Mettre à jour les deux instances de code dupliqué pour appeler la fonction à la place.

Ensuite, nous utiliserons les mêmes étapes avec des génériques pour réduire la duplication de code. De la même manière que le corps de la fonction peut opérer sur une `list` abstraite au lieu de valeurs spécifiques, les génériques permettent au code d'opérer sur des types abstraits.

Par exemple, disons que nous ayons deux fonctions : l'une qui trouve l'élément le plus grand dans une tranche de valeurs `i32` et l'autre qui trouve l'élément le plus grand dans une tranche de valeurs `char`. Comment éliminer cette duplication? Découvrons-le!
