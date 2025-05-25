# Prevenindo Referências Pendentes com _Lifetimes_

O objetivo principal dos _lifetimes_ é prevenir _referências pendentes_ (dangling references), que fazem com que um programa referencie dados diferentes dos dados que ele pretende referenciar. Considere o programa na Listagem 10-16, que possui um escopo externo e um escopo interno.

```rust
fn main() {
  1 let r;

    {
      2 let x = 5;
      3 r = &x;
  4 }

  5 println!("r: {r}");
}
```

Listagem 10-16: Uma tentativa de usar uma referência cujo valor saiu do escopo

> Nota: Os exemplos nas Listagens 10-16, 10-17 e 10-23 declaram variáveis sem dar a elas um valor inicial, então o nome da variável existe no escopo externo. À primeira vista, isso pode parecer em conflito com o fato de o Rust não ter valores nulos. No entanto, se tentarmos usar uma variável antes de dar a ela um valor, obteremos um erro em tempo de compilação, o que mostra que o Rust de fato não permite valores nulos.

O escopo externo declara uma variável chamada `r` sem valor inicial \[1], e o escopo interno declara uma variável chamada `x` com o valor inicial de `5` \[2]. Dentro do escopo interno, tentamos definir o valor de `r` como uma referência a `x` \[3]. Então o escopo interno termina \[4], e tentamos imprimir o valor em `r` \[5]. Este código não compilará porque o valor ao qual `r` está se referindo saiu do escopo antes de tentarmos usá-lo. Aqui está a mensagem de erro:

```bash
error[E0597]: `x` does not live long enough
 --> src/main.rs:6:13
  |
6 |         r = &x;
  |             ^^ borrowed value does not live long enough
7 |     }
  |     - `x` dropped here while still borrowed
8 |
9 |     println!("r: {r}");
  |                   - borrow later used here
```

A mensagem de erro diz que a variável `x` "não vive tempo suficiente". A razão é que `x` estará fora do escopo quando o escopo interno terminar na linha 7. Mas `r` ainda é válido para o escopo externo; como seu escopo é maior, dizemos que ele "vive mais tempo". Se o Rust permitisse que este código funcionasse, `r` estaria referenciando a memória que foi desalocada quando `x` saiu do escopo, e qualquer coisa que tentássemos fazer com `r` não funcionaria corretamente. Então, como o Rust determina que este código é inválido? Ele usa um _borrow checker_ (verificador de empréstimo).
