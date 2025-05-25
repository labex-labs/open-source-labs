# Criando Sinônimos de Tipos com Type Aliases (Alias de Tipos)

O Rust oferece a capacidade de declarar um _type alias_ (alias de tipo) para dar a um tipo existente outro nome. Para isso, usamos a palavra-chave `type`. Por exemplo, podemos criar o alias `Kilometers` para `i32` da seguinte forma:

```rust
type Kilometers = i32;
```

Agora, o alias `Kilometers` é um _sinônimo_ para `i32`; ao contrário dos tipos `Millimeters` e `Meters` que criamos na Listagem 19-15, `Kilometers` não é um tipo novo e separado. Valores que têm o tipo `Kilometers` serão tratados da mesma forma que valores do tipo `i32`:

    type Kilometers = i32;

    let x: i32 = 5;
    let y: Kilometers = 5;

    println!("x + y = {}", x + y);

Como `Kilometers` e `i32` são o mesmo tipo, podemos adicionar valores de ambos os tipos e podemos passar valores `Kilometers` para funções que aceitam parâmetros `i32`. No entanto, usando este método, não obtemos os benefícios de verificação de tipo que obtemos do padrão newtype discutido anteriormente. Em outras palavras, se misturarmos valores `Kilometers` e `i32` em algum lugar, o compilador não nos dará um erro.

O principal caso de uso para sinônimos de tipos é reduzir a repetição. Por exemplo, podemos ter um tipo extenso como este:

```rust
Box<dyn Fn() + Send + 'static>
```

Escrever este tipo extenso em assinaturas de funções e como anotações de tipo em todo o código pode ser cansativo e propenso a erros. Imagine ter um projeto cheio de código como o da Listagem 19-24.

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

Listagem 19-24: Usando um tipo longo em muitos lugares

Um alias de tipo torna este código mais gerenciável, reduzindo a repetição. Na Listagem 19-25, introduzimos um alias chamado `Thunk` para o tipo verboso e podemos substituir todos os usos do tipo pelo alias mais curto `Thunk`.

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

Listagem 19-25: Introduzindo um alias de tipo `Thunk` para reduzir a repetição

Este código é muito mais fácil de ler e escrever! Escolher um nome significativo para um alias de tipo pode ajudar a comunicar sua intenção também (_thunk_ é uma palavra para código a ser avaliado em um momento posterior, então é um nome apropriado para uma closure que é armazenada).

Alias de tipos também são comumente usados com o tipo `Result<T, E>` para reduzir a repetição. Considere o módulo `std::io` na biblioteca padrão. Operações de I/O geralmente retornam um `Result<T, E>` para lidar com situações em que as operações falham. Esta biblioteca tem uma struct `std::io::Error` que representa todos os possíveis erros de I/O. Muitas das funções em `std::io` retornarão `Result<T, E>` onde o `E` é `std::io::Error`, como estas funções no trait `Write`:

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

O `Result<..., Error>` é repetido muitas vezes. Como tal, `std::io` tem esta declaração de alias de tipo:

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

Como esta declaração está no módulo `std::io`, podemos usar o alias totalmente qualificado `std::io::Result<T>`; ou seja, um `Result<T, E>` com o `E` preenchido como `std::io::Error`. As assinaturas de função do trait `Write` acabam parecendo assim:

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

O alias de tipo ajuda de duas maneiras: torna o código mais fácil de escrever _e_ nos dá uma interface consistente em todo o `std::io`. Como é um alias, é apenas outro `Result<T, E>`, o que significa que podemos usar quaisquer métodos que funcionem em `Result<T, E>` com ele, bem como sintaxe especial como o operador `?`.
