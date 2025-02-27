# énumérations

Une `enum` est décomposée de manière similaire :

```rust
// `allow` est requis pour supprimer les avertissements car seul
// une variante est utilisée.
#[allow(dead_code)]
enum Couleur {
    // Ces 3 sont spécifiées uniquement par leur nom.
    Rouge,
    Bleu,
    Vert,
    // Elles lient également des tuples `u32` à différents noms : modèles de couleur.
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let couleur = Couleur::RGB(122, 17, 40);
    // TODO ^ Essayez différentes variantes pour `couleur`

    println!("Quelle est la couleur?");
    // Une `enum` peut être décomposée à l'aide d'un `match`.
    match couleur {
        Couleur::Rouge   => println!("La couleur est Rouge!"),
        Couleur::Bleu  => println!("La couleur est Bleu!"),
        Couleur::Vert => println!("La couleur est Verte!"),
        Couleur::RGB(r, g, b) =>
            println!("Rouge : {}, vert : {}, et bleu : {}!", r, g, b),
        Couleur::HSV(h, s, v) =>
            println!("Teinte : {}, saturation : {}, valeur : {}!", h, s, v),
        Couleur::HSL(h, s, l) =>
            println!("Teinte : {}, saturation : {}, luminosité : {}!", h, s, l),
        Couleur::CMY(c, m, y) =>
            println!("Cyan : {}, magenta : {}, jaune : {}!", c, m, y),
        Couleur::CMYK(c, m, y, k) =>
            println!("Cyan : {}, magenta : {}, jaune : {}, clé (noir) : {}!",
                c, m, y, k),
        // Pas besoin d'un autre bras car toutes les variantes ont été examinées
    }
}
```
