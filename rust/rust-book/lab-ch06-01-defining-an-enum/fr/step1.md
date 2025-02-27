# Définition d'un Enum

Alors que les structs vous donnent un moyen de regrouper des champs et des données liés, comme un `Rectangle` avec sa `largeur` et sa `hauteur`, les enums vous donnent un moyen de dire qu'une valeur est l'une d'un ensemble possible de valeurs. Par exemple, nous pouvons vouloir dire que `Rectangle` est l'un d'un ensemble de formes possibles qui inclut également `Circle` et `Triangle`. Pour ce faire, Rust nous permet d'encoder ces possibilités sous forme d'un enum.

Regardons une situation que nous pourrions vouloir exprimer dans le code et voyons pourquoi les enums sont utiles et plus appropriés que les structs dans ce cas. Disons que nous devons travailler avec des adresses IP. Actuellement, deux normes majeures sont utilisées pour les adresses IP : la version quatre et la version six. Parce que ce sont les seules possibilités pour une adresse IP que notre programme rencontrera, nous pouvons _énumérer_ toutes les variantes possibles, d'où le nom d'énumération.

Toute adresse IP peut être soit une adresse de version quatre soit une adresse de version six, mais pas les deux en même temps. Cette propriété des adresses IP rend la structure de données enum appropriée car une valeur enum ne peut être qu'une de ses variantes. Les adresses de version quatre et de version six sont toujours fondamentalement des adresses IP, donc elles devraient être traitées comme le même type lorsque le code gère des situations qui s'appliquent à n'importe quel type d'adresse IP.

Nous pouvons exprimer ce concept dans le code en définissant une énumération `IpAddrKind` et en listant les types possibles qu'une adresse IP peut avoir, `V4` et `V6`. Ce sont les variantes de l'enum :

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

`IpAddrKind` est désormais un type de données personnalisé que nous pouvons utiliser ailleurs dans notre code.
