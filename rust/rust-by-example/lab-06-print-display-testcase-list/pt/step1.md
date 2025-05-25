# Caso de Teste: List

Implementar `fmt::Display` para uma estrutura onde os elementos devem ser tratados sequencialmente é complicado. O problema é que cada `write!` gera um `fmt::Result`. O tratamento adequado disso requer lidar com _todos_ os resultados. Rust fornece o operador `?` exatamente para essa finalidade.

Usar `?` em `write!` se parece com isto:

```rust
// Tente `write!` para ver se ele gera erros. Se gerar erros, retorne
// o erro. Caso contrário, continue.
write!(f, "{}", value)?;
```

Com `?` disponível, implementar `fmt::Display` para um `Vec` é simples:

```rust
use std::fmt; // Importa o módulo `fmt`.

// Define uma estrutura chamada `List` contendo um `Vec`.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extrai o valor usando indexação de tupla,
        // e cria uma referência para `vec`.
        let vec = &self.0;

        write!(f, "[")?;

        // Itera sobre `v` em `vec` enquanto enumera a contagem da iteração
        // em `count`.
        for (count, v) in vec.iter().enumerate() {
            // Para cada elemento, exceto o primeiro, adicione uma vírgula.
            // Use o operador ? para retornar em caso de erros.
            if count != 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // Fecha o colchete aberto e retorna um valor fmt::Result.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## Atividade

Tente alterar o programa para que o índice de cada elemento no vetor também seja impresso. A nova saída deve ser assim:

```rust
[0: 1, 1: 2, 2: 3]
```
