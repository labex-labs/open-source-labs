# Fluxo de Controle Conciso com if let

A sintaxe `if let` permite combinar `if` e `let` de uma forma menos verbosa para lidar com valores que correspondem a um padrão, ignorando o restante. Considere o programa na Listagem 6-6 que corresponde a um valor `Option<u8>` na variável `config_max`, mas só quer executar código se o valor for a variante `Some`.

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

Listagem 6-6: Um `match` que só se preocupa em executar código quando o valor é `Some`

Se o valor for `Some`, imprimimos o valor na variante `Some` vinculando o valor à variável `max` no padrão. Não queremos fazer nada com o valor `None`. Para satisfazer a expressão `match`, temos que adicionar `_ => ()` após processar apenas uma variante, o que é um código boilerplate irritante de adicionar.

Em vez disso, poderíamos escrever isso de uma forma mais curta usando `if let`. O código a seguir se comporta da mesma forma que o `match` na Listagem 6-6:

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

A sintaxe `if let` recebe um padrão e uma expressão separados por um sinal de igual. Funciona da mesma forma que um `match`, onde a expressão é dada ao `match` e o padrão é seu primeiro braço. Neste caso, o padrão é `Some(max)`, e o `max` se vincula ao valor dentro de `Some`. Podemos então usar `max` no corpo do bloco `if let` da mesma forma que usamos `max` no braço `match` correspondente. O código no bloco `if let` não é executado se o valor não corresponder ao padrão.

Usar `if let` significa menos digitação, menos indentação e menos código boilerplate. No entanto, você perde a verificação exaustiva que o `match` impõe. A escolha entre `match` e `if let` depende do que você está fazendo em sua situação particular e se ganhar concisão é uma compensação apropriada por perder a verificação exaustiva.

Em outras palavras, você pode pensar em `if let` como açúcar sintático para um `match` que executa código quando o valor corresponde a um padrão e, em seguida, ignora todos os outros valores.

Podemos incluir um `else` com um `if let`. O bloco de código que acompanha o `else` é o mesmo que o bloco de código que acompanharia o caso `_` na expressão `match` que é equivalente ao `if let` e `else`. Recorde a definição da enumeração `Coin` na Listagem 6-4, onde a variante `Quarter` também continha um valor `UsState`. Se quiséssemos contar todas as moedas que não fossem de um quarto que vemos, ao mesmo tempo em que anunciamos o estado dos quartos, poderíamos fazer isso com uma expressão `match`, assim:

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

Ou poderíamos usar uma expressão `if let` e `else`, assim:

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

Se você tiver uma situação em que seu programa tem uma lógica que é muito verbosa para expressar usando um `match`, lembre-se de que `if let` também está em sua caixa de ferramentas Rust.
