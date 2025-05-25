# Desempenho do Código Usando Genéricos

Você pode estar se perguntando se há um custo em tempo de execução ao usar parâmetros de tipo genérico. A boa notícia é que usar tipos genéricos não fará com que seu programa seja executado mais lentamente do que seria com tipos concretos.

O Rust consegue isso realizando a monomorfização do código usando genéricos no tempo de compilação. _Monomorfização_ é o processo de transformar código genérico em código específico, preenchendo os tipos concretos que são usados ​​quando compilados. Nesse processo, o compilador faz o oposto das etapas que usamos para criar a função genérica na Listagem 10-5: o compilador olha para todos os lugares onde o código genérico é chamado e gera código para os tipos concretos com os quais o código genérico é chamado.

Vamos ver como isso funciona usando o enum genérico `Option<T>` da biblioteca padrão:

```rust
let integer = Some(5);
let float = Some(5.0);
```

Quando o Rust compila este código, ele realiza a monomorfização. Durante esse processo, o compilador lê os valores que foram usados ​​em instâncias `Option<T>` e identifica dois tipos de `Option<T>`: um é `i32` e o outro é `f64`. Como tal, ele expande a definição genérica de `Option<T>` em duas definições especializadas para `i32` e `f64`, substituindo assim a definição genérica pelas específicas.

A versão monomorfizada do código se parece com o seguinte (o compilador usa nomes diferentes dos que estamos usando aqui para ilustração):

Nome do arquivo: `src/main.rs`

```rust
enum Option_i32 {
    Some(i32),
    None,
}

enum Option_f64 {
    Some(f64),
    None,
}

fn main() {
    let integer = Option_i32::Some(5);
    let float = Option_f64::Some(5.0);
}
```

O `Option<T>` genérico é substituído pelas definições específicas criadas pelo compilador. Como o Rust compila o código genérico em código que especifica o tipo em cada instância, não pagamos nenhum custo em tempo de execução por usar genéricos. Quando o código é executado, ele funciona da mesma forma que funcionaria se tivéssemos duplicado cada definição manualmente. O processo de monomorfização torna os genéricos do Rust extremamente eficientes em tempo de execução.
