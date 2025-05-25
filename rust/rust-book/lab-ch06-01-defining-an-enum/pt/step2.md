# Valores de Enum

Podemos criar instâncias de cada uma das duas variantes de `IpAddrKind` assim:

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

Observe que as variantes do enum são namespaced sob seu identificador, e usamos dois pontos duplos para separar os dois. Isso é útil porque agora ambos os valores `IpAddrKind::V4` e `IpAddrKind::V6` são do mesmo tipo: `IpAddrKind`. Podemos então, por exemplo, definir uma função que recebe qualquer `IpAddrKind`:

```rust
fn route(ip_kind: IpAddrKind) {}
```

E podemos chamar esta função com qualquer variante:

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

Usar enums tem ainda mais vantagens. Pensando mais sobre nosso tipo de endereço IP, no momento não temos uma maneira de armazenar os _dados_ reais do endereço IP; só sabemos que _tipo_ ele é. Dado que você acabou de aprender sobre structs no Capítulo 5, você pode ser tentado a abordar este problema com structs, como mostrado na Listagem 6-1.

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

Listagem 6-1: Armazenando os dados e a variante `IpAddrKind` de um endereço IP usando uma `struct`

Aqui, definimos uma struct `IpAddr` \[2] que tem dois campos: um campo `kind` \[3] que é do tipo `IpAddrKind` (o enum que definimos anteriormente \[1]) e um campo `address` \[4] do tipo `String`. Temos duas instâncias desta struct. A primeira é `home` \[5], e ela tem o valor `IpAddrKind::V4` como seu `kind` com dados de endereço associados de `127.0.0.1`. A segunda instância é `loopback` \[6]. Ela tem a outra variante de `IpAddrKind` como seu valor `kind`, `V6`, e tem o endereço `::1` associado a ele. Usamos uma struct para agrupar os valores `kind` e `address` juntos, então agora a variante está associada ao valor.

No entanto, representar o mesmo conceito usando apenas um enum é mais conciso: em vez de um enum dentro de uma struct, podemos colocar dados diretamente em cada variante do enum. Esta nova definição do enum `IpAddr` diz que as variantes `V4` e `V6` terão valores `String` associados:

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

Anexamos dados a cada variante do enum diretamente, então não há necessidade de uma struct extra. Aqui, também é mais fácil ver outro detalhe de como os enums funcionam: o nome de cada variante do enum que definimos também se torna uma função que constrói uma instância do enum. Ou seja, `IpAddr::V4()` é uma chamada de função que recebe um argumento `String` e retorna uma instância do tipo `IpAddr`. Obtemos automaticamente esta função construtora definida como resultado da definição do enum.

Há outra vantagem em usar um enum em vez de uma struct: cada variante pode ter diferentes tipos e quantidades de dados associados. Os endereços IP versão quatro sempre terão quatro componentes numéricos que terão valores entre 0 e 255. Se quiséssemos armazenar endereços `V4` como quatro valores `u8`, mas ainda expressar endereços `V6` como um valor `String`, não seríamos capazes com uma struct. Os enums lidam com este caso com facilidade:

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

Mostramos várias maneiras diferentes de definir estruturas de dados para armazenar endereços IP versão quatro e versão seis. No entanto, como acontece, querer armazenar endereços IP e codificar qual tipo eles são é tão comum que a biblioteca padrão tem uma definição que podemos usar! Vamos ver como a biblioteca padrão define `IpAddr`: ela tem o enum e as variantes exatas que definimos e usamos, mas ela incorpora os dados do endereço dentro das variantes na forma de duas structs diferentes, que são definidas de forma diferente para cada variante:

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

Este código ilustra que você pode colocar qualquer tipo de dados dentro de uma variante de enum: strings, tipos numéricos ou structs, por exemplo. Você pode até incluir outro enum! Além disso, os tipos da biblioteca padrão geralmente não são muito mais complicados do que o que você pode inventar.

Observe que, embora a biblioteca padrão contenha uma definição para `IpAddr`, ainda podemos criar e usar nossa própria definição sem conflito porque não trouxemos a definição da biblioteca padrão para nosso escopo. Falaremos mais sobre como trazer tipos para o escopo no Capítulo 7.

Vamos ver outro exemplo de um enum na Listagem 6-2: este tem uma grande variedade de tipos incorporados em suas variantes.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Listagem 6-2: Um enum `Message` cujas variantes armazenam diferentes quantidades e tipos de valores

Este enum tem quatro variantes com tipos diferentes:

- `Quit` não tem dados associados a ele.
- `Move` tem campos nomeados, como uma struct.
- `Write` inclui uma única `String`.
- `ChangeColor` inclui três valores `i32`.

Definir um enum com variantes como as da Listagem 6-2 é semelhante a definir diferentes tipos de definições de struct, exceto que o enum não usa a palavra-chave `struct` e todas as variantes são agrupadas sob o tipo `Message`. As seguintes structs poderiam conter os mesmos dados que as variantes de enum anteriores contêm:

```rust
struct QuitMessage; // unit struct
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // tuple struct
struct ChangeColorMessage(i32, i32, i32); // tuple struct
```

Mas se usássemos as diferentes structs, cada uma com seu próprio tipo, não poderíamos definir tão facilmente uma função para receber qualquer um desses tipos de mensagens como poderíamos com o enum `Message` definido na Listagem 6-2, que é um único tipo.

Há mais uma semelhança entre enums e structs: assim como podemos definir métodos em structs usando `impl`, também podemos definir métodos em enums. Aqui está um método chamado `call` que poderíamos definir em nosso enum `Message`:

```rust
impl Message {
    fn call(&self) {
      1 // method body would be defined here
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

O corpo do método usaria `self` para obter o valor no qual chamamos o método. Neste exemplo, criamos uma variável `m` \[2] que tem o valor `Message::Write(String::from("hello"))`, e é isso que `self` será no corpo do método `call` \[1] quando `m.call()` for executado.

Vamos ver outro enum na biblioteca padrão que é muito comum e útil: `Option`.
