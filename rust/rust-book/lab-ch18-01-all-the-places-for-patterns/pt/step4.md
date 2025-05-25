# Laços condicionais `while let`

Semelhante em construção ao `if let`, o laço condicional `while let` permite que um laço `while` seja executado enquanto um padrão continuar a corresponder. Na Listagem 18-2, codificamos um laço `while let` que usa um vetor como uma pilha e imprime os valores no vetor na ordem inversa em que foram inseridos.

Nome do arquivo: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listagem 18-2: Usando um laço `while let` para imprimir valores enquanto `stack.pop()` retorna `Some`

Este exemplo imprime `3`, `2` e depois `1`. O método `pop` remove o último elemento do vetor e retorna `Some(value)`. Se o vetor estiver vazio, `pop` retorna `None`. O laço `while` continua executando o código em seu bloco enquanto `pop` retorna `Some`. Quando `pop` retorna `None`, o laço para. Podemos usar `while let` para remover cada elemento de nossa pilha.
