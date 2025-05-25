# Funções Associadas

Todas as funções definidas dentro de um bloco `impl` são chamadas de _funções associadas_ porque estão associadas ao tipo nomeado após o `impl`. Podemos definir funções associadas que não têm `self` como seu primeiro parâmetro (e, portanto, não são métodos) porque não precisam de uma instância do tipo para trabalhar. Já usamos uma função como essa: a função `String::from` que é definida no tipo `String`.

Funções associadas que não são métodos são frequentemente usadas para construtores que retornarão uma nova instância da struct. Elas são frequentemente chamadas de `new`, mas `new` não é um nome especial e não está embutido na linguagem. Por exemplo, poderíamos escolher fornecer uma função associada chamada `square` que teria um parâmetro de dimensão e usaria isso como largura e altura, tornando mais fácil criar um `Rectangle` quadrado em vez de ter que especificar o mesmo valor duas vezes:

Nome do arquivo: `src/main.rs`

```rust
impl Rectangle {
    fn square(size: u32) -> 1 Self  {
      2 Self  {
            width: size,
            height: size,
        }
    }
}
```

As palavras-chave `Self` no tipo de retorno \[1] e no corpo da função \[2] são aliases para o tipo que aparece após a palavra-chave `impl`, que neste caso é `Rectangle`.

Para chamar esta função associada, usamos a sintaxe `::` com o nome da struct; `let sq = Rectangle::square(3);` é um exemplo. Esta função é namespaced pela struct: a sintaxe `::` é usada tanto para funções associadas quanto para namespaces criados por módulos. Discutiremos módulos no Capítulo 7.
