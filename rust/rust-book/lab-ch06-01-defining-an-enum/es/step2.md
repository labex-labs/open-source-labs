# Valores de Enum

Podemos crear instancias de cada una de las dos variantes de `IpAddrKind` de la siguiente manera:

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

Tenga en cuenta que las variantes del enum están en un espacio de nombres bajo su identificador, y usamos dos puntos para separar los dos. Esto es útil porque ahora ambos valores `IpAddrKind::V4` y `IpAddrKind::V6` son del mismo tipo: `IpAddrKind`. Luego, por ejemplo, podemos definir una función que tome cualquier `IpAddrKind`:

```rust
fn route(ip_kind: IpAddrKind) {}
```

Y podemos llamar a esta función con cualquiera de las variantes:

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

Usar enums tiene aún más ventajas. Pensando más en nuestro tipo de dirección IP, en este momento no tenemos una forma de almacenar los datos reales de la dirección IP; solo sabemos de qué _tipo_ es. Dado que acaba de aprender sobre structs en el Capítulo 5, es posible que se sienta tentado de abordar este problema con structs como se muestra en la Lista 6-1.

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

Lista 6-1: Almacenando los datos y la variante `IpAddrKind` de una dirección IP usando un `struct`

Aquí, hemos definido un struct `IpAddr` \[2\] que tiene dos campos: un campo `kind` \[3\] que es del tipo `IpAddrKind` (el enum que definimos anteriormente \[1\]) y un campo `address` \[4\] del tipo `String`. Tenemos dos instancias de este struct. La primera es `home` \[5\], y tiene el valor `IpAddrKind::V4` como su `kind` con los datos de dirección asociados de `127.0.0.1`. La segunda instancia es `loopback` \[6\]. Tiene la otra variante de `IpAddrKind` como su valor `kind`, `V6`, y tiene la dirección `::1` asociada a ella. Hemos usado un struct para agrupar los valores `kind` y `address` juntos, por lo que ahora la variante está asociada con el valor.

Sin embargo, representar el mismo concepto solo con un enum es más conciso: en lugar de un enum dentro de un struct, podemos poner los datos directamente en cada variante de enum. Esta nueva definición del enum `IpAddr` dice que tanto las variantes `V4` como `V6` tendrán valores `String` asociados:

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

Adjuntamos los datos a cada variante del enum directamente, por lo que no es necesario un struct adicional. Aquí, también es más fácil ver otro detalle de cómo funcionan los enums: el nombre de cada variante de enum que definimos también se convierte en una función que construye una instancia del enum. Es decir, `IpAddr::V4()` es una llamada a función que toma un argumento `String` y devuelve una instancia del tipo `IpAddr`. Automáticamente obtenemos esta función constructor definida como resultado de definir el enum.

Hay otra ventaja de usar un enum en lugar de un struct: cada variante puede tener diferentes tipos y cantidades de datos asociados. Las direcciones IP de versión cuatro siempre tendrán cuatro componentes numéricos que tendrán valores entre 0 y 255. Si quisiéramos almacenar las direcciones `V4` como cuatro valores `u8` pero todavía expresar las direcciones `V6` como un valor `String`, no podríamos hacerlo con un struct. Los enums manejan este caso con facilidad:

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

Hemos mostrado varias maneras diferentes de definir estructuras de datos para almacenar direcciones IP de versión cuatro y versión seis. Sin embargo, resulta que querer almacenar direcciones IP y codificar de qué tipo son es tan común que la biblioteca estándar tiene una definición que podemos usar. Echemos un vistazo a cómo la biblioteca estándar define `IpAddr`: tiene exactamente el enum y las variantes que hemos definido y usado, pero embebe los datos de dirección dentro de las variantes en forma de dos structs diferentes, que se definen de manera diferente para cada variante:

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

Este código ilustra que se puede poner cualquier tipo de datos dentro de una variante de enum: cadenas, tipos numéricos o structs, por ejemplo. Incluso se puede incluir otro enum. Además, los tipos de la biblioteca estándar a menudo no son mucho más complicados que los que uno podría inventar.

Tenga en cuenta que aunque la biblioteca estándar contiene una definición para `IpAddr`, todavía podemos crear y usar nuestra propia definición sin conflicto porque no hemos traído la definición de la biblioteca estándar a nuestro ámbito. Hablaremos más sobre traer tipos al ámbito en el Capítulo 7.

Echemos un vistazo a otro ejemplo de un enum en la Lista 6-2: este tiene una amplia variedad de tipos embebidos en sus variantes.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Lista 6-2: Un enum `Message` cuyas variantes cada una almacena diferentes cantidades y tipos de valores

Este enum tiene cuatro variantes con diferentes tipos:

- `Quit` no tiene datos asociados en absoluto.
- `Move` tiene campos con nombre, como un struct.
- `Write` incluye una sola `String`.
- `ChangeColor` incluye tres valores `i32`.

Definir un enum con variantes como las de la Lista 6-2 es similar a definir diferentes tipos de definiciones de struct, excepto que el enum no usa la palabra clave `struct` y todas las variantes se agrupan juntas bajo el tipo `Message`. Los siguientes structs podrían contener los mismos datos que las variantes de enum anteriores:

```rust
struct QuitMessage; // struct unitario
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // struct tupla
struct ChangeColorMessage(i32, i32, i32); // struct tupla
```

Pero si usáramos los diferentes structs, cada uno de los cuales tiene su propio tipo, no podríamos definir una función para tomar cualquiera de estos tipos de mensajes tan fácilmente como lo podríamos hacer con el enum `Message` definido en la Lista 6-2, que es un solo tipo.

Hay una más similitud entre enums y structs: al igual que podemos definir métodos en structs usando `impl`, también podemos definir métodos en enums. Aquí hay un método llamado `call` que podríamos definir en nuestro enum `Message`:

```rust
impl Message {
    fn call(&self) {
      1 // el cuerpo del método se definiría aquí
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

El cuerpo del método usaría `self` para obtener el valor en el que se llamó el método. En este ejemplo, hemos creado una variable `m` \[2\] que tiene el valor `Message::Write(String::from("hello"))`, y eso es lo que `self` será en el cuerpo del método `call` \[1\] cuando se ejecute `m.call()`.

Echemos un vistazo a otro enum en la biblioteca estándar que es muy común y útil: `Option`.
