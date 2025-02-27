# Formatage

Nous avons vu que la mise en forme est spécifiée via une _chaîne de formatage_ :

- `format!("{}", foo)` -> `"3735928559"`
- `format!("0x{:X}", foo)` -> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -> `"0o33653337357"`

La même variable (`foo`) peut être formatée différemment selon le _type d'argument_ utilisé : `X` vs `o` vs _non spécifié_.

Cette fonctionnalité de formatage est implémentée via des traits, et il existe un trait pour chaque type d'argument. Le trait de formatage le plus courant est `Display`, qui gère les cas où le type d'argument n'est pas spécifié : `{}` par exemple.

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitude
    lat: f32,
    // Longitude
    lon: f32,
}

impl Display for City {
    // `f` est un tampon, et cette méthode doit écrire la chaîne formatée dedans.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` est comme `format!`, mais il écrira la chaîne formatée
        // dans un tampon (le premier argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // Changez ceci pour utiliser {} une fois que vous avez ajouté une implémentation
        // pour fmt::Display.
        println!("{:?}", color);
    }
}
```

Vous pouvez consulter la liste complète des traits de formatage et de leurs types d'arguments dans la documentation de `std::fmt`.

## Activité

Ajoutez une implémentation du trait `fmt::Display` pour la structure `Color` ci-dessus de sorte que la sortie s'affiche comme suit :

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

Trois conseils si vous êtes bloqué :

- La formule pour calculer une couleur dans l'espace de couleur RGB est : `RGB = (R*65536)+(G*256)+B, (lorsque R est ROUGE, G est VERT et B est BLEU)`. Pour en savoir plus, consultez le format et le calcul de la couleur RGB.
- Vous pouvez avoir besoin de lister chaque couleur plus d'une fois.
- Vous pouvez compléter avec des zéros jusqu'à une largeur de 2 avec `:0>2`.
