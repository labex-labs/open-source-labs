# Types de taille dynamique et le trait `Sized`

Rust doit connaître certains détails sur ses types, par exemple combien d'espace allouer pour une valeur d'un type particulier. Cela laisse un coin de son système de types un peu confus au départ : le concept de _types de taille dynamique_. Parfois appelés _DST_ ou _types non dimensionnés_, ces types nous permettent d'écrire du code utilisant des valeurs dont la taille ne peut être connue que pendant l'exécution.

Plongeons dans les détails d'un type de taille dynamique appelé `str`, que nous avons utilisé tout au long du livre. C'est vrai, pas `&str`, mais `str` tout seul, est un DST. Nous ne pouvons pas savoir combien de caractères la chaîne contient jusqu'à l'exécution, ce qui signifie que nous ne pouvons pas créer une variable de type `str`, ni prendre un argument de type `str`. Considérez le code suivant, qui ne fonctionne pas :

```rust
let s1: str = "Hello there!";
let s2: str = "How's it going?";
```

Rust doit savoir combien de mémoire allouer pour toute valeur d'un type particulier, et toutes les valeurs d'un type doivent utiliser la même quantité de mémoire. Si Rust nous autorisait à écrire ce code, ces deux valeurs de type `str` devraient occuper la même quantité d'espace. Mais elles ont des longueurs différentes : `s1` nécessite 12 octets de stockage et `s2` nécessite 15. C'est pourquoi il n'est pas possible de créer une variable contenant un type de taille dynamique.

Alors, que faisons-nous? Dans ce cas, vous savez déjà la réponse : nous donnons à `s1` et `s2` le type `&str` plutôt que `str`. Rappelez-vous de "Tranche de chaîne" que la structure de données de tranche stocke juste la position de départ et la longueur de la tranche. Ainsi, bien qu'un `&T` soit une seule valeur qui stocke l'adresse mémoire où se trouve le `T`, un `&str` est _deux_ valeurs : l'adresse du `str` et sa longueur. En conséquence, nous pouvons connaître la taille d'une valeur de type `&str` à la compilation : elle est le double de la longueur d'un `usize`. C'est-à-dire que nous connaissons toujours la taille d'un `&str`, quelle que soit la longueur de la chaîne qu'il référence. En général, c'est ainsi que les types de taille dynamique sont utilisés en Rust : ils ont un supplément d'informations métadonnées qui stockent la taille des informations dynamiques. La règle d'or des types de taille dynamique est que nous devons toujours placer les valeurs de types de taille dynamique derrière un pointeur de quelque type que ce soit.

Nous pouvons combiner `str` avec tous types de pointeurs : par exemple, `Box<str>` ou `Rc<str>`. En fait, vous l'avez déjà vu auparavant mais avec un type de taille dynamique différent : les traits. Chaque trait est un type de taille dynamique que nous pouvons référencer en utilisant le nom du trait. Dans "Utilisation d'objets de trait qui autorisent des valeurs de différents types", nous avons mentionné que pour utiliser les traits en tant qu'objets de trait, nous devons les placer derrière un pointeur, tel que `&dyn Trait` ou `Box<dyn Trait>` (`Rc<dyn Trait>` fonctionnerait également).

Pour travailler avec les DST, Rust fournit le trait `Sized` pour déterminer si la taille d'un type est connue à la compilation ou non. Ce trait est automatiquement implémenté pour tout ce dont la taille est connue à la compilation. De plus, Rust ajoute implicitement une contrainte sur `Sized` à chaque fonction générique. C'est-à-dire qu'une définition de fonction générique comme celle-ci :

```rust
fn generic<T>(t: T) {
    --snip--
}
```

est en fait traitée comme si nous avions écrit ceci :

```rust
fn generic<T: Sized>(t: T) {
    --snip--
}
```

Par défaut, les fonctions génériques ne fonctionneront que sur des types dont la taille est connue à la compilation. Cependant, vous pouvez utiliser la syntaxe spéciale suivante pour relâcher cette restriction :

```rust
fn generic<T:?Sized>(t: &T) {
    --snip--
}
```

Une contrainte de trait sur `?Sized` signifie "`T` peut ou non être `Sized`" et cette notation remplace la valeur par défaut selon laquelle les types génériques doivent avoir une taille connue à la compilation. La syntaxe `?Trait` avec ce sens n'est disponible que pour `Sized`, pas pour aucun autre trait.

Notez également que nous avons changé le type du paramètre `t` de `T` à `&T`. Parce que le type peut ne pas être `Sized`, nous devons l'utiliser derrière un pointeur de quelque type que ce soit. Dans ce cas, nous avons choisi une référence.

Ensuite, nous parlerons des fonctions et des closures!
