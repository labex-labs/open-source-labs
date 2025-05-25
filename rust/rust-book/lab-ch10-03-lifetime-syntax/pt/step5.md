# Sintaxe de Anotação de _Lifetime_

Anotações de _lifetime_ não alteram quanto tempo qualquer uma das referências vive. Em vez disso, elas descrevem as relações dos _lifetimes_ de múltiplas referências entre si, sem afetar os _lifetimes_. Assim como as funções podem aceitar qualquer tipo quando a assinatura especifica um parâmetro de tipo genérico, as funções podem aceitar referências com qualquer _lifetime_ especificando um parâmetro de _lifetime_ genérico.

Anotações de _lifetime_ têm uma sintaxe ligeiramente incomum: os nomes dos parâmetros de _lifetime_ devem começar com um apóstrofo (`'`) e geralmente são todos minúsculos e muito curtos, como tipos genéricos. A maioria das pessoas usa o nome `'a` para a primeira anotação de _lifetime_. Colocamos anotações de parâmetro de _lifetime_ após o `&` de uma referência, usando um espaço para separar a anotação do tipo da referência.

Aqui estão alguns exemplos: uma referência a um `i32` sem um parâmetro de _lifetime_, uma referência a um `i32` que tem um parâmetro de _lifetime_ chamado `'a`, e uma referência mutável a um `i32` que também tem o _lifetime_ `'a`.

```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```

Uma anotação de _lifetime_ por si só não tem muito significado, porque as anotações são destinadas a dizer ao Rust como os parâmetros de _lifetime_ genéricos de múltiplas referências se relacionam entre si. Vamos examinar como as anotações de _lifetime_ se relacionam entre si no contexto da função `longest`.
