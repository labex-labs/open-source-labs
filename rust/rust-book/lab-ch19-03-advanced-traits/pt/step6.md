# Usando o Padrão Newtype para Implementar Traits Externas

Em "Implementando uma Trait em um Tipo", mencionamos a regra do órfão (orphan rule) que afirma que só podemos implementar uma trait em um tipo se a trait ou o tipo, ou ambos, forem locais para o nosso crate. É possível contornar essa restrição usando o _padrão newtype_, que envolve a criação de um novo tipo em uma struct de tupla. (Cobrimos structs de tupla em "Usando Structs de Tupla Sem Campos Nomeados para Criar Tipos Diferentes".) A struct de tupla terá um campo e será um wrapper fino em torno do tipo para o qual queremos implementar uma trait. Então, o tipo wrapper é local para o nosso crate, e podemos implementar a trait no wrapper. _Newtype_ é um termo que se originou da linguagem de programação Haskell. Não há penalidade de desempenho em tempo de execução para usar este padrão, e o tipo wrapper é elidido em tempo de compilação.

Como exemplo, digamos que queremos implementar `Display` em `Vec<T>`, o que a regra do órfão nos impede de fazer diretamente porque a trait `Display` e o tipo `Vec<T>` são definidos fora do nosso crate. Podemos criar uma struct `Wrapper` que contém uma instância de `Vec<T>`; então podemos implementar `Display` em `Wrapper` e usar o valor `Vec<T>`, conforme mostrado na Listagem 19-23.

Nome do arquivo: `src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

Listagem 19-23: Criando um tipo `Wrapper` em torno de `Vec<String>` para implementar `Display`

A implementação de `Display` usa `self.0` para acessar o `Vec<T>` interno porque `Wrapper` é uma struct de tupla e `Vec<T>` é o item no índice 0 na tupla. Então, podemos usar a funcionalidade do tipo `Display` em `Wrapper`.

A desvantagem de usar essa técnica é que `Wrapper` é um novo tipo, então ele não tem os métodos do valor que está contendo. Teríamos que implementar todos os métodos de `Vec<T>` diretamente em `Wrapper` de forma que os métodos deleguem para `self.0`, o que nos permitiria tratar `Wrapper` exatamente como um `Vec<T>`. Se quiséssemos que o novo tipo tivesse todos os métodos que o tipo interno tem, implementar a trait `Deref` em `Wrapper` para retornar o tipo interno seria uma solução (discutimos a implementação da trait `Deref` em "Tratando Ponteiros Inteligentes como Referências Regulares com Deref"). Se não quiséssemos que o tipo `Wrapper` tivesse todos os métodos do tipo interno - por exemplo, para restringir o comportamento do tipo `Wrapper` - teríamos que implementar apenas os métodos que queremos manualmente.

Este padrão newtype também é útil mesmo quando as traits não estão envolvidas. Vamos mudar o foco e analisar algumas maneiras avançadas de interagir com o sistema de tipos do Rust.
