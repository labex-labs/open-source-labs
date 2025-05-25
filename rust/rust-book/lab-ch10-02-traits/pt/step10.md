# Usando Trait Bounds para Implementar Métodos Condicionalmente

Ao usar um trait bound com um bloco `impl` que usa parâmetros de tipo genérico, podemos implementar métodos condicionalmente para tipos que implementam os traits especificados. Por exemplo, o tipo `Pair<T>` na Listagem 10-15 sempre implementa a função `new` para retornar uma nova instância de `Pair<T>` (lembre-se de "Definindo Métodos" que `Self` é um alias de tipo para o tipo do bloco `impl`, que neste caso é `Pair<T>`). Mas no próximo bloco `impl`, `Pair<T>` só implementa o método `cmp_display` se seu tipo interno `T` implementar o trait `PartialOrd` que permite a comparação _e_ o trait `Display` que permite a impressão.

Nome do arquivo: `src/lib.rs`

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

Listagem 10-15: Implementando métodos condicionalmente em um tipo genérico dependendo dos trait bounds

Também podemos implementar condicionalmente um trait para qualquer tipo que implemente outro trait. Implementações de um trait em qualquer tipo que satisfaça os trait bounds são chamadas de _implementações blanket_ e são usadas extensivamente na biblioteca padrão do Rust. Por exemplo, a biblioteca padrão implementa o trait `ToString` em qualquer tipo que implementa o trait `Display`. O bloco `impl` na biblioteca padrão se parece com este código:

```rust
impl<T: Display> ToString for T {
    --snip--
}
```

Como a biblioteca padrão tem esta implementação blanket, podemos chamar o método `to_string` definido pelo trait `ToString` em qualquer tipo que implemente o trait `Display`. Por exemplo, podemos transformar inteiros em seus valores `String` correspondentes assim, porque os inteiros implementam `Display`:

```rust
let s = 3.to_string();
```

Implementações blanket aparecem na documentação do trait na seção "Implementadores".

Traits e trait bounds nos permitem escrever código que usa parâmetros de tipo genérico para reduzir a duplicação, mas também especificar ao compilador que queremos que o tipo genérico tenha um comportamento particular. O compilador pode então usar as informações do trait bound para verificar se todos os tipos concretos usados com nosso código fornecem o comportamento correto. Em linguagens de tipagem dinâmica, teríamos um erro em tempo de execução se chamássemos um método em um tipo que não definisse o método. Mas Rust move esses erros para o tempo de compilação, então somos forçados a corrigir os problemas antes mesmo que nosso código possa ser executado. Além disso, não precisamos escrever código que verifique o comportamento em tempo de execução porque já verificamos em tempo de compilação. Fazer isso melhora o desempenho sem ter que abrir mão da flexibilidade dos genéricos.
