# Dados Apenas na _Stack_: _Copy_

Há outra questão que ainda não discutimos. Este código usando inteiros - parte do qual foi mostrado na Listagem 4-2 - funciona e é válido:

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

Mas este código parece contradizer o que acabamos de aprender: não temos uma chamada para `clone`, mas `x` ainda é válido e não foi movido para `y`.

A razão é que tipos como inteiros que têm um tamanho conhecido em tempo de compilação são armazenados inteiramente na _stack_, então as cópias dos valores reais são rápidas de fazer. Isso significa que não há razão para querermos impedir que `x` seja válido depois de criarmos a variável `y`. Em outras palavras, não há diferença entre cópia profunda e rasa aqui, então chamar `clone` não faria nada diferente da cópia rasa usual, e podemos deixá-lo de fora.

Rust tem uma anotação especial chamada _trait_ `Copy` que podemos colocar em tipos que são armazenados na _stack_, como os inteiros são (falaremos mais sobre _traits_ no Capítulo 10). Se um tipo implementa o _trait_ `Copy`, as variáveis que o usam não se movem, mas sim são trivialmente copiadas, tornando-as ainda válidas após a atribuição a outra variável.

Rust não nos permitirá anotar um tipo com `Copy` se o tipo, ou qualquer uma de suas partes, tiver implementado o _trait_ `Drop`. Se o tipo precisar que algo especial aconteça quando o valor sair do escopo e adicionarmos a anotação `Copy` a esse tipo, receberemos um erro em tempo de compilação. Para saber como adicionar a anotação `Copy` ao seu tipo para implementar o _trait_, consulte "Traits Deriváveis".

Então, quais tipos implementam o _trait_ `Copy`? Você pode verificar a documentação do tipo fornecido para ter certeza, mas, como regra geral, qualquer grupo de valores escalares simples pode implementar `Copy`, e nada que exija alocação ou seja alguma forma de recurso pode implementar `Copy`. Aqui estão alguns dos tipos que implementam `Copy`:

- Todos os tipos inteiros, como `u32`.
- O tipo booleano, `bool`, com os valores `true` e `false`.
- Todos os tipos de ponto flutuante, como `f64`.
- O tipo caractere, `char`.
- Tuplas, se contiverem apenas tipos que também implementam `Copy`. Por exemplo, `(i32, i32)` implementa `Copy`, mas `(i32, String)` não.
