# Variáveis e Dados Interagindo com _Clone_

Se _quisermos_ copiar profundamente os dados da _heap_ do `String`, não apenas os dados da _stack_, podemos usar um método comum chamado `clone`. Discutiremos a sintaxe do método no Capítulo 5, mas como os métodos são um recurso comum em muitas linguagens de programação, você provavelmente já os viu antes.

Aqui está um exemplo do método `clone` em ação:

```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("s1 = {s1}, s2 = {s2}");
```

Isso funciona perfeitamente e produz explicitamente o comportamento mostrado na Figura 4-3, onde os dados da _heap_ _são_ copiados.

Quando você vê uma chamada para `clone`, sabe que algum código arbitrário está sendo executado e que esse código pode ser caro. É um indicador visual de que algo diferente está acontecendo.
