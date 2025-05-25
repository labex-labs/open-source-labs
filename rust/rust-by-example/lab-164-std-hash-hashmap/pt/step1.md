# HashMap

Onde vetores armazenam valores por um índice inteiro, `HashMap`s armazenam valores por chave. As chaves do `HashMap` podem ser booleanos, inteiros, strings ou qualquer outro tipo que implemente os traits `Eq` e `Hash`. Mais detalhes sobre isso na próxima seção.

Assim como vetores, `HashMap`s são crescentes, mas também podem encolher quando têm espaço em excesso. Você pode criar um `HashMap` com uma determinada capacidade inicial usando `HashMap::with_capacity(uint)`, ou usar `HashMap::new()` para obter um `HashMap` com uma capacidade inicial padrão (recomendado).

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "Desculpe, a chamada não pode ser completada.
            Por favor, desligue e tente novamente.",
        "645-7689" => "Olá, aqui está a Pizzaria Sr. Awesome. Meu nome é Fred.
            O que posso fazer por você hoje?",
        _ => "Olá! Quem fala?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Recebe uma referência e retorna Option<&V>
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Ligando para Daniel: {}", call(number)),
        _ => println!("Não temos o número do Daniel."),
    }

    // `HashMap::insert()` retorna `None`
    // se o valor inserido for novo, `Some(value)` caso contrário
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Ligando para Ashley: {}", call(number)),
        _ => println!("Não temos o número da Ashley."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` retorna um iterador que gera pares (&'a chave, &'a valor) em uma ordem arbitrária.
    for (contact, &number) in contacts.iter() {
        println!("Ligando para {}: {}", contact, call(number));
    }
}
```

Para mais informações sobre como funcionam os hash e os hash maps (às vezes chamados de tabelas hash), consulte a Wikipedia de Tabela Hash.
