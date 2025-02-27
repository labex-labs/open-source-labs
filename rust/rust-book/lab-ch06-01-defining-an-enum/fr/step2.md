# Valeurs d'énumération

Nous pouvons créer des instances de chacune des deux variantes de `IpAddrKind` comme ceci :

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

Remarquez que les variantes de l'énumération sont encadrées par son identifiant, et nous utilisons deux points pour les séparer. Cela est pratique car maintenant les deux valeurs `IpAddrKind::V4` et `IpAddrKind::V6` sont du même type : `IpAddrKind`. Nous pouvons ensuite, par exemple, définir une fonction qui prend n'importe quel `IpAddrKind` :

```rust
fn route(ip_kind: IpAddrKind) {}
```

Et nous pouvons appeler cette fonction avec n'importe laquelle des variantes :

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

L'utilisation d'énums présente encore plus d'avantages. En réfléchissant davantage à notre type d'adresse IP, pour le moment, nous n'avons pas de moyen de stocker les données de l'adresse IP réelle ; nous ne savons que de quel _type_ elle est. Étant donné que vous venez d'apprendre les structs au chapitre 5, vous pourriez être tenté de résoudre ce problème avec des structs comme dans la liste 6-1.

```rust
1 enum IpAddrKind {
    V4,
    V6,
}

2 struct IpAddr {
  3 kind: IpAddrKind,
  4 address: String,
}

5 let home = IpAddr {
    kind: IpAddrKind::V4,
    address: String::from("127.0.0.1"),
};

6 let loopback = IpAddr {
    kind: IpAddrKind::V6,
    address: String::from("::1"),
};
```

Liste 6-1 : Stockage des données et de la variante `IpAddrKind` d'une adresse IP à l'aide d'un `struct`

Ici, nous avons défini un struct `IpAddr` \[2\] qui a deux champs : un champ `kind` \[3\] qui est de type `IpAddrKind` (l'énumération que nous avons définie précédemment \[1\]) et un champ `address` \[4\] de type `String`. Nous avons deux instances de ce struct. La première est `home` \[5\], et elle a la valeur `IpAddrKind::V4` comme `kind` avec des données d'adresse associées de `127.0.0.1`. La deuxième instance est `loopback` \[6\]. Elle a l'autre variante de `IpAddrKind` comme valeur de `kind`, `V6`, et a l'adresse `::1` associée. Nous avons utilisé un struct pour regrouper les valeurs `kind` et `address` ensemble, de sorte que maintenant la variante est associée à la valeur.

Cependant, représenter le même concept en utilisant seulement un enum est plus concise : au lieu d'avoir un enum à l'intérieur d'un struct, nous pouvons directement insérer des données dans chaque variante d'énumération. Cette nouvelle définition de l'énumération `IpAddr` indique que les deux variantes `V4` et `V6` auront des valeurs `String` associées :

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

Nous attachons directement des données à chaque variante de l'énumération, il n'est donc pas nécessaire d'avoir un struct supplémentaire. Ici, il est également plus facile de voir un autre détail sur la façon dont les enums fonctionnent : le nom de chaque variante d'énumération que nous définissons devient également une fonction qui construit une instance de l'énumération. C'est-à-dire que `IpAddr::V4()` est un appel de fonction qui prend un argument `String` et renvoie une instance du type `IpAddr`. Nous obtenons automatiquement cette fonction constructeur définie en définissant l'énumération.

Il y a un autre avantage à utiliser un enum plutôt qu'un struct : chaque variante peut avoir différents types et quantités de données associées. Les adresses IP de version quatre auront toujours quatre composants numériques qui auront des valeurs comprises entre 0 et 255. Si nous voulions stocker les adresses `V4` comme quatre valeurs `u8` mais toujours exprimer les adresses `V6` comme une seule valeur `String`, nous ne pourrions pas le faire avec un struct. Les enums gèrent ce cas avec aisance :

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

Nous avons montré plusieurs façons différentes de définir des structures de données pour stocker les adresses IP de version quatre et de version six. Cependant, il s'avère que le fait de vouloir stocker des adresses IP et d'encoder de quel type elles sont est si courant que la bibliothèque standard a une définition que nous pouvons utiliser! Voyons comment la bibliothèque standard définit `IpAddr` : elle a exactement l'énumération et les variantes que nous avons définies et utilisées, mais elle incorpore les données d'adresse à l'intérieur des variantes sous forme de deux structs différents, qui sont définis différemment pour chaque variante :

```rust
struct Ipv4Addr {
    --snip--
}

struct Ipv6Addr {
    --snip--
}

enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

Ce code illustre que vous pouvez insérer n'importe quel type de données dans une variante d'énumération : des chaînes, des types numériques ou des structs, par exemple. Vous pouvez même inclure un autre enum! De plus, les types de bibliothèque standard ne sont souvent pas beaucoup plus complexes que ceux que vous pourriez imaginer.

Remarquez que même si la bibliothèque standard contient une définition pour `IpAddr`, nous pouvons toujours créer et utiliser notre propre définition sans conflit car nous n'avons pas importé la définition de la bibliothèque standard dans notre portée. Nous en parlerons plus longuement au chapitre 7.

Regardons un autre exemple d'énumération dans la liste 6-2 : celle-ci a une grande variété de types incorporés dans ses variantes.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Liste 6-2 : Un `Message` enum dont les variantes stockent différentes quantités et types de valeurs

Cet enum a quatre variantes avec différents types :

- `Quit` n'a aucune donnée associée.
- `Move` a des champs nommés, comme un struct.
- `Write` inclut une seule `String`.
- `ChangeColor` inclut trois valeurs `i32`.

Définir un enum avec des variantes telles que celles de la liste 6-2 est similaire à définir différents types de définitions de structs, sauf que l'énumération n'utilise pas le mot clé `struct` et que toutes les variantes sont regroupées sous le type `Message`. Les structs suivants pourraient contenir les mêmes données que les variantes d'énumération précédentes :

```rust
struct QuitMessage; // struct unitaire
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // struct tuple
struct ChangeColorMessage(i32, i32, i32); // struct tuple
```

Mais si nous utilisions les différents structs, chacun ayant son propre type, nous ne pourrions pas aussi facilement définir une fonction pour prendre n'importe quel type de message que nous pourrions avec l'énumération `Message` définie dans la liste 6-2, qui est un seul type.

Il y a encore une autre similitude entre les enums et les structs : tout comme nous sommes capables de définir des méthodes sur les structs en utilisant `impl`, nous sommes également capables de définir des méthodes sur les enums. Voici une méthode nommée `call` que nous pourrions définir sur notre énumération `Message` :

```rust
impl Message {
    fn call(&self) {
      1 // le corps de la méthode serait défini ici
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

Le corps de la méthode utiliserait `self` pour obtenir la valeur sur laquelle nous avons appelé la méthode. Dans cet exemple, nous avons créé une variable `m` \[2\] qui a la valeur `Message::Write(String::from("hello"))`, et c'est ce que `self` sera dans le corps de la méthode `call` \[1\] lorsque `m.call()` est exécuté.

Regardons un autre enum dans la bibliothèque standard qui est très courant et utile : `Option`.
