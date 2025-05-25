# Seguindo o Ponteiro para o Valor

Uma referência regular é um tipo de ponteiro, e uma maneira de pensar em um ponteiro é como uma seta para um valor armazenado em outro lugar. Na Listagem 15-6, criamos uma referência a um valor `i32` e, em seguida, usamos o operador de desreferenciação para seguir a referência ao valor.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
  1 let x = 5;
  2 let y = &x;

  3 assert_eq!(5, x);
  4 assert_eq!(5, *y);
}
```

Listagem 15-6: Usando o operador de desreferenciação para seguir uma referência a um valor `i32`

A variável `x` contém um valor `i32` `5` \[1]. Definimos `y` igual a uma referência a `x` \[2]. Podemos afirmar que `x` é igual a `5` \[3]. No entanto, se quisermos fazer uma afirmação sobre o valor em `y`, devemos usar `*y` para seguir a referência ao valor para o qual ela está apontando (portanto, _desreferenciação_) para que o compilador possa comparar o valor real \[4]. Depois de desreferenciar `y`, temos acesso ao valor inteiro para o qual `y` está apontando, que podemos comparar com `5`.

Se tentássemos escrever `assert_eq!(5, y);` em vez disso, obteríamos este erro de compilação:

```bash
error[E0277]: can't compare `{integer}` with `&{integer}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementation for `{integer} ==
&{integer}`
  |
  = help: the trait `PartialEq<&{integer}>` is not implemented
for `{integer}`
```

Comparar um número e uma referência a um número não é permitido porque são tipos diferentes. Devemos usar o operador de desreferenciação para seguir a referência ao valor para o qual ela está apontando.
