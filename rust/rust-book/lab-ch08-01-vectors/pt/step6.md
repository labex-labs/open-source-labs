# Usando um Enum para Armazenar Múltiplos Tipos

Vetores só podem armazenar valores que são do mesmo tipo. Isso pode ser inconveniente; definitivamente existem casos de uso para a necessidade de armazenar uma lista de itens de tipos diferentes. Felizmente, as variantes de um enum são definidas sob o mesmo tipo enum, então, quando precisamos de um tipo para representar elementos de tipos diferentes, podemos definir e usar um enum!

Por exemplo, digamos que queremos obter valores de uma linha em uma planilha na qual algumas das colunas na linha contêm inteiros, alguns números de ponto flutuante e algumas strings. Podemos definir um enum cujas variantes conterão os diferentes tipos de valor, e todas as variantes do enum serão consideradas do mesmo tipo: o do enum. Então, podemos criar um vetor para conter esse enum e, assim, finalmente, conter diferentes tipos. Demonstramos isso na Listagem 8-9.

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

Listagem 8-9: Definindo um `enum` para armazenar valores de diferentes tipos em um vetor

O Rust precisa saber quais tipos estarão no vetor no tempo de compilação para que saiba exatamente quanta memória no heap será necessária para armazenar cada elemento. Também devemos ser explícitos sobre quais tipos são permitidos neste vetor. Se o Rust permitisse que um vetor contivesse qualquer tipo, haveria uma chance de que um ou mais dos tipos causasse erros com as operações realizadas nos elementos do vetor. Usar um enum mais uma expressão `match` significa que o Rust garantirá no tempo de compilação que todos os casos possíveis sejam tratados, como discutido no Capítulo 6.

Se você não souber o conjunto exaustivo de tipos que um programa obterá em tempo de execução para armazenar em um vetor, a técnica enum não funcionará. Em vez disso, você pode usar um objeto trait, que abordaremos no Capítulo 17.

Agora que discutimos algumas das maneiras mais comuns de usar vetores, certifique-se de revisar a documentação da API para todos os muitos métodos úteis definidos em `Vec<T>` pela biblioteca padrão. Por exemplo, além de `push`, um método `pop` remove e retorna o último elemento.
