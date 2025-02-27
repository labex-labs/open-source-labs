# Extraire les valeurs capturées des closures et les traits `Fn`

Une fois qu'une closure a capturé une référence ou a pris la propriété d'une valeur de l'environnement dans lequel elle est définie (ce qui affecte donc ce qui, le cas échéant, est déplacé _vers l'intérieur_ de la closure), le code dans le corps de la closure définit ce qui se passe avec les références ou les valeurs lorsque la closure est évaluée plus tard (ce qui affecte donc ce qui, le cas échéant, est déplacé _vers l'extérieur_ de la closure).

Le corps d'une closure peut faire l'une des choses suivantes : déplacer une valeur capturée hors de la closure, muter la valeur capturée, ni déplacer ni muter la valeur, ou ne rien capturer de l'environnement au départ.

La manière dont une closure capture et gère les valeurs de l'environnement affecte les traits que la closure implémente, et les traits sont la manière dont les fonctions et les structs peuvent spécifier quels types de closures ils peuvent utiliser. Les closures implémenteront automatiquement un, deux ou les trois traits `Fn` suivants, de manière additive, selon la façon dont le corps de la closure gère les valeurs :

- `FnOnce` s'applique aux closures qui peuvent être appelées une seule fois. Toutes les closures implémentent au moins ce trait car toutes les closures peuvent être appelées. Une closure qui déplace les valeurs capturées hors de son corps n'implémentera que `FnOnce` et aucun des autres traits `Fn` car elle ne peut être appelée qu'une seule fois.
- `FnMut` s'applique aux closures qui ne déplacent pas les valeurs capturées hors de leur corps, mais qui peuvent muter les valeurs capturées. Ces closures peuvent être appelées plusieurs fois.
- `Fn` s'applique aux closures qui ne déplacent pas les valeurs capturées hors de leur corps et qui ne mutent pas les valeurs capturées, ainsi qu'aux closures qui ne capturent rien de leur environnement. Ces closures peuvent être appelées plusieurs fois sans muter leur environnement, ce qui est important dans des cas tels que l'appel d'une closure plusieurs fois simultanément.

Regardons la définition de la méthode `unwrap_or_else` sur `Option<T>` que nous avons utilisée dans la Liste 13-1 :

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

Rappelez-vous que `T` est le type générique représentant le type de la valeur dans la variante `Some` d'un `Option`. Ce type `T` est également le type de retour de la fonction `unwrap_or_else` : le code qui appelle `unwrap_or_else` sur un `Option<String>`, par exemple, obtiendra une `String`.

Ensuite, remarquez que la fonction `unwrap_or_else` a le paramètre de type générique supplémentaire `F`. Le type `F` est le type du paramètre nommé `f`, qui est la closure que nous fournissons lorsqu'on appelle `unwrap_or_else`.

La contrainte de trait spécifiée sur le type générique `F` est `FnOnce() -> T`, ce qui signifie que `F` doit être apellable une fois, ne prendre aucun argument et renvoyer un `T`. En utilisant `FnOnce` dans la contrainte de trait, on exprime la contrainte selon laquelle `unwrap_or_else` ne va appeler `f` qu'une seule fois, au maximum. Dans le corps de `unwrap_or_else`, on peut voir que si l'`Option` est `Some`, `f` ne sera pas appelé. Si l'`Option` est `None`, `f` sera appelé une fois. Parce que toutes les closures implémentent `FnOnce`, `unwrap_or_else` accepte la plus grande variété de closures et est aussi flexible que possible.

> Note : Les fonctions peuvent également implémenter les trois traits `Fn`. Si ce que nous voulons faire ne nécessite pas capturer de valeur de l'environnement, nous pouvons utiliser le nom d'une fonction plutôt qu'une closure là où nous avons besoin de quelque chose qui implémente l'un des traits `Fn`. Par exemple, sur une valeur `Option<Vec<T>>`, nous pourrions appeler `unwrap_or_else(Vec::new)` pour obtenir un nouveau vecteur vide si la valeur est `None`.

Maintenant, regardons la méthode de la bibliothèque standard `sort_by_key`, définie sur les slices, pour voir en quoi elle diffère de `unwrap_or_else` et pourquoi `sort_by_key` utilise `FnMut` au lieu de `FnOnce` pour la contrainte de trait. La closure reçoit un argument sous forme d'une référence à l'élément actuel de la slice considérée et renvoie une valeur de type `K` qui peut être ordonnée. Cette fonction est utile lorsque vous voulez trier une slice selon un attribut particulier de chaque élément. Dans la Liste 13-7, nous avons une liste d'instances de `Rectangle` et nous utilisons `sort_by_key` pour les ordonner par leur attribut `width` du plus petit au plus grand.

Nom du fichier : `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Liste 13-7 : Utilisation de `sort_by_key` pour ordonner des rectangles par largeur

Ce code imprime :

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

La raison pour laquelle `sort_by_key` est défini pour prendre une closure `FnMut` est qu'elle appelle la closure plusieurs fois : une fois pour chaque élément de la slice. La closure `|r| r.width` ne capture, ne muter ni ne déplace rien de son environnement, donc elle répond aux exigences de la contrainte de trait.

En revanche, la Liste 13-8 montre un exemple d'une closure qui implémente seulement le trait `FnOnce`, car elle déplace une valeur de l'environnement. Le compilateur ne nous laissera pas utiliser cette closure avec `sort_by_key`.

Nom du fichier : `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

Liste 13-8 : Tentative d'utilisation d'une closure `FnOnce` avec `sort_by_key`

C'est une manière artificielle et compliquée (qui ne fonctionne pas) d'essayer de compter le nombre de fois que `sort_by_key` est appelé lors du tri de `list`. Ce code tente de faire ce comptage en ajoutant `value` --- une `String` de l'environnement de la closure --- dans le vecteur `sort_operations`. La closure capture `value` puis déplace `value` hors de la closure en transférant la propriété de `value` au vecteur `sort_operations`. Cette closure peut être appelée une fois ; essayer de l'appeler une deuxième fois ne fonctionnerait pas car `value` ne serait plus dans l'environnement pour être ajouté à nouveau dans `sort_operations`! Par conséquent, cette closure n'implémente que `FnOnce`. Lorsque nous essayons de compiler ce code, nous obtenons cette erreur selon laquelle `value` ne peut pas être déplacé hors de la closure car la closure doit implémenter `FnMut` :

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

L'erreur pointe vers la ligne dans le corps de la closure qui déplace `value` hors de l'environnement. Pour corriger ceci, nous devons modifier le corps de la closure de sorte qu'elle ne déplace pas les valeurs hors de l'environnement. Conserver un compteur dans l'environnement et incrémenter sa valeur dans le corps de la closure est une manière plus directe de compter le nombre de fois que `sort_by_key` est appelé. La closure dans la Liste 13-9 fonctionne avec `sort_by_key` car elle capture seulement une référence mutable au compteur `num_sort_operations` et peut donc être appelée plusieurs fois.

Nom du fichier : `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

Liste 13-9 : Utilisation d'une closure `FnMut` avec `sort_by_key` est autorisée.

Les traits `Fn` sont importants lorsqu'on définit ou utilise des fonctions ou des types qui utilisent des closures. Dans la section suivante, nous parlerons d'itérateurs. De nombreuses méthodes d'itérateur prennent des arguments de closure, donc gardez ces détails sur les closures à l'esprit lorsque nous continuerons!
