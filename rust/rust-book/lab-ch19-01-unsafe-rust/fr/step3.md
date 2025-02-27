# Dereferencing a Raw Pointer

Dans "Dangling References", nous avons mentionné que le compilateur assure que les références sont toujours valides. Le Rust non sécurisé a deux nouveaux types appelés _pointeurs bruts_ qui sont similaires aux références. Comme pour les références, les pointeurs bruts peuvent être immuables ou mutables et sont écrits respectivement `*const T` et `*mut T`. L'astérisque n'est pas l'opérateur de déréférencement ; il fait partie du nom du type. Dans le contexte des pointeurs bruts, _immuable_ signifie que le pointeur ne peut pas être directement assigné après avoir été déréférencé.

Différents des références et des pointeurs intelligents, les pointeurs bruts :

- Sont autorisés à ignorer les règles d'emprunt en ayant à la fois des pointeurs immuables et mutables ou plusieurs pointeurs mutables vers la même emplacement
- Ne sont pas garantis pour pointer vers une mémoire valide
- Sont autorisés à être nuls
- N'implémentent pas de nettoyage automatique

En optant pour que Rust n'applique pas ces garanties, vous pouvez renoncer à la sécurité garantie en échange de meilleures performances ou de la capacité d'interagir avec un autre langage ou un matériel où les garanties de Rust ne s'appliquent pas.

Le Listing 19-1 montre comment créer un pointeur brut immuable et un pointeur brut mutable à partir de références.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;
```

Listing 19-1 : Création de pointeurs bruts à partir de références

Remarquez que nous n'incluons pas le mot clé `unsafe` dans ce code. Nous pouvons créer des pointeurs bruts dans du code sécurisé ; nous ne pouvons simplement pas déréférencer des pointeurs bruts en dehors d'un bloc `unsafe`, comme vous allez voir un peu plus loin.

Nous avons créé des pointeurs bruts en utilisant `as` pour convertir une référence immuable et une référence mutable dans leurs types de pointeurs bruts correspondants. Étant donné que nous les avons créés directement à partir de références garanties comme valides, nous savons que ces pointeurs bruts particuliers sont valides, mais nous ne pouvons pas faire cette hypothèse pour n'importe quel pointeur brut.

Pour le démontrer, ensuite, nous allons créer un pointeur brut dont la validité n'est pas aussi certaine. Le Listing 19-2 montre comment créer un pointeur brut vers un emplacement arbitraire en mémoire. Tenter d'utiliser une mémoire arbitraire est indéfini : il peut y avoir des données à cette adresse ou pas, le compilateur peut optimiser le code de sorte qu'il n'y ait pas d'accès mémoire, ou le programme peut se terminer avec une erreur de segmentation. En général, il n'y a pas de bonne raison d'écrire du code comme ça, mais il est possible.

```rust
let address = 0x012345usize;
let r = address as *const i32;
```

Listing 19-2 : Création d'un pointeur brut vers une adresse mémoire arbitraire

Rappelez-vous que nous pouvons créer des pointeurs bruts dans du code sécurisé, mais nous ne pouvons pas _déréférencer_ des pointeurs bruts et lire les données auxquelles ils pointent. Dans le Listing 19-3, nous utilisons l'opérateur de déréférencement `*` sur un pointeur brut qui nécessite un bloc `unsafe`.

```rust
let mut num = 5;

let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

Listing 19-3 : Déréférencement de pointeurs bruts à l'intérieur d'un bloc `unsafe`

Créer un pointeur ne fait aucun tort ; c'est seulement lorsque nous essayons d'accéder à la valeur à laquelle il pointe que nous risquons de finir par traiter une valeur invalide.

Notez également que dans les Listings 19-1 et 19-3, nous avons créé des pointeurs bruts `*const i32` et `*mut i32` qui ont tous deux pointé vers le même emplacement mémoire, où `num` est stocké. Si au lieu de cela, nous avions essayé de créer une référence immuable et une référence mutable à `num`, le code n'aurait pas compilé car les règles de propriété de Rust n'autorisent pas une référence mutable en même temps qu'aucune référence immuable. Avec des pointeurs bruts, nous pouvons créer un pointeur mutable et un pointeur immuable vers le même emplacement et modifier les données à travers le pointeur mutable, créant potentiellement une course de données. Faites attention!

Avec tous ces dangers, pourquoi utiliseriez-vous jamais des pointeurs bruts? Un cas d'utilisation majeur est lorsqu'on interface avec du code C, comme vous le verrez dans "Appeler une fonction ou une méthode non sécurisée". Un autre cas est lorsqu'on construit des abstractions sécurisées que le vérificateur d'emprunt ne comprend pas. Nous allons présenter les fonctions non sécurisées puis examiner un exemple d'abstraction sécurisée qui utilise du code non sécurisé.
