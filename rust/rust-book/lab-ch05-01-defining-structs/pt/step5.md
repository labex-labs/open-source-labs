# Structs Semelhantes a Unidades Sem Nenhum Campo

Você também pode definir structs que não têm nenhum campo! Elas são chamadas de _structs semelhantes a unidades_ porque se comportam de maneira semelhante a `()`, o tipo unitário que mencionamos em "O Tipo Tupla". Structs semelhantes a unidades podem ser úteis quando você precisa implementar um trait em algum tipo, mas não tem nenhum dado que deseja armazenar no próprio tipo. Discutiremos traits no Capítulo 10. Aqui está um exemplo de como declarar e instanciar uma struct unitária chamada `AlwaysEqual`:

Nome do arquivo: `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

Para definir `AlwaysEqual`, usamos a palavra-chave `struct`, o nome que queremos e, em seguida, um ponto e vírgula. Não há necessidade de chaves ou parênteses! Então, podemos obter uma instância de `AlwaysEqual` na variável `subject` de maneira semelhante: usando o nome que definimos, sem chaves ou parênteses. Imagine que, mais tarde, implementaremos um comportamento para este tipo, de modo que cada instância de `AlwaysEqual` seja sempre igual a cada instância de qualquer outro tipo, talvez para ter um resultado conhecido para fins de teste. Não precisaríamos de nenhum dado para implementar esse comportamento! Você verá no Capítulo 10 como definir traits e implementá-los em qualquer tipo, incluindo structs semelhantes a unidades.

> **Propriedade dos Dados da Struct**
>
> Na definição da struct `User` na Listagem 5-1, usamos o tipo `String` próprio em vez do tipo fatia de string `&str`. Esta é uma escolha deliberada porque queremos que cada instância desta struct possua todos os seus dados e que esses dados sejam válidos enquanto toda a struct for válida.
>
> Também é possível que as structs armazenem referências a dados pertencentes a outra coisa, mas, para fazer isso, é necessário o uso de _lifetimes_ (tempo de vida), um recurso do Rust que discutiremos no Capítulo 10. Lifetimes garantem que os dados referenciados por uma struct sejam válidos enquanto a struct for. Digamos que você tente armazenar uma referência em uma struct sem especificar lifetimes, como o seguinte em `src/main.rs`; isso não funcionará:
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> O compilador reclamará que precisa de especificadores de tempo de vida:
>
>     $ `cargo run`
>        Compiling structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> No Capítulo 10, discutiremos como corrigir esses erros para que você possa armazenar referências em structs, mas, por enquanto, corrigiremos erros como esses usando tipos próprios como `String` em vez de referências como `&str`.
