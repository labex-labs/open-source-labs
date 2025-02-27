# Bytes and Scalar Values and Grapheme Clusters! Oh My!

Un autre point concernant UTF-8 est qu'il existe en fait trois façons pertinentes de considérer les chaînes de caractères du point de vue de Rust : en tant que bytes, en tant que valeurs scalaires et en tant que grappes de caractères (ce qui est le plus proche de ce que nous appellerions des _lettres_).

Si nous considérons le mot hindi "नमस्ते" écrit en script dévanagari, il est stocké sous forme d'un vecteur de valeurs `u8` qui ressemble à ceci :

```rust
[224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224,
164, 164, 224, 165, 135]
```

Ce sont 18 octets et c'est ainsi que les ordinateurs stockent finalement ces données. Si nous les considérons comme des valeurs scalaires Unicode, qui sont le type `char` de Rust, ces octets ressemblent à ceci :

```rust
['न', 'म', 'स', '्', 'त', 'े']
```

Il y a six valeurs `char` ici, mais la quatrième et la sixième ne sont pas des lettres : ce sont des diacritiques qui n'ont pas de sens isolés. Enfin, si nous les considérons comme des grappes de caractères, nous obtiendrons ce qu'une personne appellerait les quatre lettres qui composent le mot hindi :

```rust
["न", "म", "स्", "ते"]
```

Rust fournit différentes façons d'interpréter les données brutes de chaîne de caractères stockées par les ordinateurs de sorte que chaque programme puisse choisir l'interprétation dont il a besoin, quelle que soit la langue humaine des données.

Une dernière raison pour laquelle Rust ne nous permet pas d'indexer une `String` pour obtenir un caractère est que les opérations d'indexation sont censées prendre toujours un temps constant (O(1)). Mais il n'est pas possible de garantir cette performance avec une `String`, car Rust devrait parcourir le contenu depuis le début jusqu'à l'index pour déterminer combien de caractères valides il y avait.
