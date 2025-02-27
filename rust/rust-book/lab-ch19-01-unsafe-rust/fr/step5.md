# Créer une abstraction sécurisée sur du code non sécurisé

Le simple fait qu'une fonction contienne du code non sécurisé ne signifie pas que nous devons marquer toute la fonction comme non sécurisée. En fait, envelopper du code non sécurisé dans une fonction sécurisée est une abstraction courante. Par exemple, étudions la fonction `split_at_mut` de la bibliothèque standard, qui nécessite du code non sécurisé. Nous explorerons comment nous pourrions l'implémenter. Cette méthode sécurisée est définie sur des slices mutables : elle prend une slice et la divise en deux en la coupant à l'index donné en argument. Le Listing 19-4 montre comment utiliser `split_at_mut`.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

Listing 19-4 : Utilisation de la fonction sécurisée `split_at_mut`

Nous ne pouvons pas implémenter cette fonction en utilisant seulement le Rust sécurisé. Une tentative pourrait ressembler au Listing 19-5, qui ne compilera pas. Pour simplifier, nous implémenterons `split_at_mut` comme une fonction plutôt qu'une méthode et seulement pour des slices de valeurs `i32` plutôt que pour un type générique `T`.

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

Listing 19-5 : Tentative d'implémentation de `split_at_mut` en utilisant seulement le Rust sécurisé

Cette fonction obtient d'abord la longueur totale de la slice. Ensuite, elle vérifie que l'index donné en paramètre est dans la slice en vérifiant s'il est inférieur ou égal à la longueur. L'assertion signifie que si nous passons un index supérieur à la longueur pour diviser la slice, la fonction va planter avant d'essayer d'utiliser cet index.

Ensuite, nous retournons deux slices mutables dans un tuple : l'une du début de la slice d'origine jusqu'à l'index `mid` et l'autre de `mid` jusqu'à la fin de la slice.

Lorsque nous essayons de compiler le code du Listing 19-5, nous obtiendrons une erreur :

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

Le vérificateur d'emprunt de Rust ne peut pas comprendre que nous empruntons des parties différentes de la slice ; il ne sait que nous empruntons deux fois à la même slice. Emprunter des parties différentes d'une slice est fondamentalement correct car les deux slices ne se chevauchent pas, mais Rust n'est pas assez intelligent pour le savoir. Lorsque nous savons que le code est correct, mais que Rust ne le sait pas, il est temps d'utiliser du code non sécurisé.

Le Listing 19-6 montre comment utiliser un bloc `unsafe`, un pointeur brut et quelques appels à des fonctions non sécurisées pour que l'implémentation de `split_at_mut` fonctionne.

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

Listing 19-6 : Utilisation de code non sécurisé dans l'implémentation de la fonction `split_at_mut`

Rappelez-vous de "Le type slice" qu'un slice est un pointeur vers des données et la longueur de la slice. Nous utilisons la méthode `len` pour obtenir la longueur d'une slice \[1\] et la méthode `as_mut_ptr` pour accéder au pointeur brut d'une slice \[2\]. Dans ce cas, puisque nous avons une slice mutable de valeurs `i32`, `as_mut_ptr` renvoie un pointeur brut avec le type `*mut i32`, que nous avons stocké dans la variable `ptr`.

Nous conservons l'assertion que l'index `mid` est dans la slice \[3\]. Ensuite, nous arrivons au code non sécurisé \[4\] : la fonction `slice::from_raw_parts_mut` prend un pointeur brut et une longueur, et elle crée une slice. Nous l'utilisons pour créer une slice qui commence à `ptr` et qui est longue de `mid` éléments \[5\]. Ensuite, nous appelons la méthode `add` sur `ptr` avec `mid` comme argument pour obtenir un pointeur brut qui commence à `mid`, et nous créons une slice en utilisant ce pointeur et le nombre restant d'éléments après `mid` comme longueur \[6\].

La fonction `slice::from_raw_parts_mut` est non sécurisée car elle prend un pointeur brut et doit faire confiance que ce pointeur est valide. La méthode `add` sur les pointeurs bruts est également non sécurisée car elle doit faire confiance que l'emplacement d'offset est également un pointeur valide. Par conséquent, nous avons dû mettre un bloc `unsafe` autour de nos appels à `slice::from_raw_parts_mut` et `add` pour pouvoir les appeler. En examinant le code et en ajoutant l'assertion que `mid` doit être inférieur ou égal à `len`, nous pouvons dire que tous les pointeurs bruts utilisés à l'intérieur du bloc `unsafe` seront des pointeurs valides vers des données à l'intérieur de la slice. Ceci est une utilisation acceptable et appropriée de `unsafe`.

Notez que nous n'avons pas besoin de marquer la fonction résultante `split_at_mut` comme `unsafe`, et nous pouvons appeler cette fonction à partir du Rust sécurisé. Nous avons créé une abstraction sécurisée pour le code non sécurisé avec une implémentation de la fonction qui utilise du code non sécurisé de manière sécurisée, car elle ne crée que des pointeurs valides à partir des données dont cette fonction a accès.

En revanche, l'utilisation de `slice::from_raw_parts_mut` dans le Listing 19-7 risque probablement de planter lorsque la slice est utilisée. Ce code prend un emplacement mémoire arbitraire et crée une slice de 10 000 éléments de long.

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

Listing 19-7 : Création d'une slice à partir d'un emplacement mémoire arbitraire

Nous ne possédons pas la mémoire à cet emplacement arbitraire, et il n'est pas garanti que la slice créée par ce code contienne des valeurs `i32` valides. Tenter d'utiliser `values` comme si c'était une slice valide entraîne un comportement indéfini.
