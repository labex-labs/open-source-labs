# Une valeur entière avec \_

Nous avons utilisé le tiret bas comme motif joker qui correspondra à n'importe quelle valeur mais ne se lira pas à la valeur. Cela est particulièrement utile comme dernier bras dans une expression `match`, mais nous pouvons également l'utiliser dans n'importe quel motif, y compris les paramètres de fonction, comme montré dans la Liste 18-17.

Nom de fichier : `src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("This code only uses the y parameter: {y}");
}

fn main() {
    foo(3, 4);
}
```

Liste 18-17 : Utilisation de `_` dans une signature de fonction

Ce code ignorera complètement la valeur `3` passée en tant que premier argument et imprimera `This code only uses the y parameter: 4`.

Dans la plupart des cas, lorsque vous n'avez plus besoin d'un paramètre de fonction particulier, vous modifieriez la signature pour qu'elle n'inclue pas le paramètre non utilisé. Ignorer un paramètre de fonction peut être particulièrement utile dans des cas où, par exemple, vous implémentez un trait et que vous avez besoin d'un certain type de signature, mais que le corps de la fonction dans votre implémentation n'a pas besoin d'un des paramètres. Vous évitez ainsi de recevoir un avertissement du compilateur concernant les paramètres de fonction non utilisés, comme vous le feriez si vous utilisiez un nom à la place.
