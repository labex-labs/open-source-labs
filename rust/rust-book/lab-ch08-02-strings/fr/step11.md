# Methods for Iterating Over Strings

La meilleure façon de travailler sur des parties de chaînes de caractères est d'être explicite sur le fait que vous voulez des caractères ou des octets. Pour les valeurs scalaires Unicode individuelles, utilisez la méthode `chars`. Appeler `chars` sur "Зд" sépare et renvoie deux valeurs de type `char`, et vous pouvez itérer sur le résultat pour accéder à chaque élément :

    for c in "Зд".chars() {
        println!("{c}");
    }

Ce code affichera ce qui suit :

```rust
З
д
```

Alternativement, la méthode `bytes` renvoie chaque octet brut, ce qui peut être approprié pour votre domaine :

    for b in "Зд".bytes() {
        println!("{b}");
    }

Ce code affichera les quatre octets qui composent cette chaîne :

    208
    151
    208
    180

Mais n'oubliez pas que les valeurs scalaires Unicode valides peuvent être composées de plus d'un octet.

Obtenir des grappes de caractères à partir de chaînes de caractères, comme avec le script dévanagari, est complexe, donc cette fonctionnalité n'est pas fournie par la bibliothèque standard. Des crates sont disponibles sur *https://crates.io* si c'est la fonctionnalité dont vous avez besoin.
