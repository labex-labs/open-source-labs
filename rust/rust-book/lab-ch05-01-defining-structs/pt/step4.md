# Usando Tuple Structs Sem Campos Nomeados para Criar Tipos Diferentes

Rust também suporta structs que se assemelham a tuplas, chamadas de _tuple structs_. Tuple structs têm o significado adicional que o nome da struct fornece, mas não têm nomes associados aos seus campos; em vez disso, elas apenas têm os tipos dos campos. Tuple structs são úteis quando você deseja dar um nome à tupla inteira e tornar a tupla um tipo diferente de outras tuplas, e quando nomear cada campo como em uma struct regular seria verboso ou redundante.

Para definir uma tuple struct, comece com a palavra-chave `struct` e o nome da struct, seguido pelos tipos na tupla. Por exemplo, aqui definimos e usamos duas tuple structs chamadas `Color` e `Point`:

Nome do arquivo: `src/main.rs`

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
```

Observe que os valores `black` e `origin` são tipos diferentes porque são instâncias de diferentes tuple structs. Cada struct que você define é seu próprio tipo, mesmo que os campos dentro da struct possam ter os mesmos tipos. Por exemplo, uma função que recebe um parâmetro do tipo `Color` não pode receber um `Point` como argumento, mesmo que ambos os tipos sejam compostos por três valores `i32`. Caso contrário, as instâncias de tuple struct são semelhantes às tuplas, pois você pode desestruturá-las em suas partes individuais e pode usar um `.` seguido pelo índice para acessar um valor individual.
