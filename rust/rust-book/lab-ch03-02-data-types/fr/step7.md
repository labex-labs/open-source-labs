# Le type caractère

Le type `char` de Rust est le type alphabétique le plus primitif du langage. Voici quelques exemples de déclaration de valeurs `char` :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // avec annotation de type explicite
    let heart_eyed_cat = '😻';
}
```

Notez que nous spécifions les littéraux `char` avec des apostrophes simples, contrairement aux littéraux de chaîne, qui utilisent des guillemets doubles. Le type `char` de Rust a une taille de quatre octets et représente une Valeur scalaire Unicode, ce qui signifie qu'il peut représenter bien plus que simplement le code ASCII. Les lettres accentuées ; les caractères chinois, japonais et coréens ; les émojis ; et les espaces de largeur nulle sont tous des valeurs `char` valides en Rust. Les Valeurs scalaires Unicode vont de `U+0000` à `U+D7FF` et de `U+E000` à `U+10FFFF` inclusivement. Cependant, un "caractère" n'est pas vraiment un concept dans Unicode, donc votre intuition humaine de ce qu'est un "caractère" peut ne pas correspondre à ce qu'est un `char` en Rust. Nous aborderons ce sujet en détail dans "Stockage de texte encodé en UTF-8 avec les chaînes".
