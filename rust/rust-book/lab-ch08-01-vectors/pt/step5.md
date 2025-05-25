# Iterando Sobre os Valores em um Vetor

Para acessar cada elemento em um vetor por sua vez, iteraríamos por todos os elementos em vez de usar índices para acessar um de cada vez. A Listagem 8-7 mostra como usar um loop `for` para obter referências imutáveis a cada elemento em um vetor de valores `i32` e imprimi-los.

```rust
let v = vec![100, 32, 57];
for i in &v {
    println!("{i}");
}
```

Listagem 8-7: Imprimindo cada elemento em um vetor iterando sobre os elementos usando um loop `for`

Também podemos iterar sobre referências mutáveis a cada elemento em um vetor mutável para fazer alterações em todos os elementos. O loop `for` na Listagem 8-8 adicionará `50` a cada elemento.

```rust
let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

Listagem 8-8: Iterando sobre referências mutáveis a elementos em um vetor

Para alterar o valor ao qual a referência mutável se refere, temos que usar o operador de desreferência `*` para chegar ao valor em `i` antes de podermos usar o operador `+=`. Falaremos mais sobre o operador de desreferência em "Seguindo o Ponteiro para o Valor".

Iterar sobre um vetor, seja imutável ou mutavelmente, é seguro por causa das regras do verificador de empréstimo (borrow checker). Se tentássemos inserir ou remover itens nos corpos do loop `for` nas Listagens 8-7 e 8-8, obteríamos um erro do compilador semelhante ao que obtivemos com o código na Listagem 8-6. A referência ao vetor que o loop `for` mantém impede a modificação simultânea de todo o vetor.
