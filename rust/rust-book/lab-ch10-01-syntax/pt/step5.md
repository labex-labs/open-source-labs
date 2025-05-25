# Em Definições de Enum

Como fizemos com structs, podemos definir enums para conter tipos de dados genéricos em suas variantes. Vamos dar outra olhada no enum `Option<T>` que a biblioteca padrão fornece, que usamos no Capítulo 6:

```rust
enum Option<T> {
    Some(T),
    None,
}
```

Esta definição agora deve fazer mais sentido para você. Como você pode ver, o enum `Option<T>` é genérico sobre o tipo `T` e tem duas variantes: `Some`, que contém um valor do tipo `T`, e uma variante `None` que não contém nenhum valor. Ao usar o enum `Option<T>`, podemos expressar o conceito abstrato de um valor opcional e, como `Option<T>` é genérico, podemos usar essa abstração, independentemente do tipo do valor opcional.

Enums também podem usar vários tipos genéricos. A definição do enum `Result` que usamos no Capítulo 9 é um exemplo:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

O enum `Result` é genérico sobre dois tipos, `T` e `E`, e tem duas variantes: `Ok`, que contém um valor do tipo `T`, e `Err`, que contém um valor do tipo `E`. Esta definição torna conveniente usar o enum `Result` em qualquer lugar onde tenhamos uma operação que possa ter sucesso (retornar um valor de algum tipo `T`) ou falhar (retornar um erro de algum tipo `E`). Na verdade, é isso que usamos para abrir um arquivo na Listagem 9-3, onde `T` foi preenchido com o tipo `std::fs::File` quando o arquivo foi aberto com sucesso e `E` foi preenchido com o tipo `std::io::Error` quando houve problemas ao abrir o arquivo.

Quando você reconhece situações em seu código com várias definições de struct ou enum que diferem apenas nos tipos de valores que contêm, você pode evitar a duplicação usando tipos genéricos.
