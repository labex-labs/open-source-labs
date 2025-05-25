# O _Borrow Checker_

O compilador Rust possui um _*borrow checker*_ (verificador de empréstimo) que compara escopos para determinar se todos os empréstimos são válidos. A Listagem 10-17 mostra o mesmo código da Listagem 10-16, mas com anotações mostrando os _lifetimes_ das variáveis.

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

Listagem 10-17: Anotações dos _lifetimes_ de `r` e `x`, nomeados `'a` e `'b`, respectivamente

Aqui, anotamos o _lifetime_ de `r` com `'a` e o _lifetime_ de `x` com `'b`. Como você pode ver, o bloco interno `'b` é muito menor que o bloco externo de _lifetime_ `'a`. Em tempo de compilação, o Rust compara o tamanho dos dois _lifetimes_ e vê que `r` tem um _lifetime_ de `'a`, mas que se refere à memória com um _lifetime_ de `'b`. O programa é rejeitado porque `'b` é menor que `'a`: o sujeito da referência não vive tanto quanto a referência.

A Listagem 10-18 corrige o código para que ele não tenha uma referência pendente e compile sem erros.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Listagem 10-18: Uma referência válida porque os dados têm um _lifetime_ mais longo que a referência

Aqui, `x` tem o _lifetime_ `'b`, que neste caso é maior que `'a`. Isso significa que `r` pode referenciar `x` porque o Rust sabe que a referência em `r` sempre será válida enquanto `x` for válido.

Agora que você sabe onde estão os _lifetimes_ das referências e como o Rust analisa os _lifetimes_ para garantir que as referências sempre sejam válidas, vamos explorar os _lifetimes_ genéricos de parâmetros e valores de retorno no contexto de funções.
