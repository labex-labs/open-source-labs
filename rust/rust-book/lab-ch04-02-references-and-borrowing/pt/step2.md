# Referências Mutáveis (Mutable References)

Podemos corrigir o código do Listing 4-6 para nos permitir modificar um valor emprestado com apenas alguns pequenos ajustes que usam, em vez disso, uma _referência mutável_:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

Primeiro, mudamos `s` para ser `mut`. Em seguida, criamos uma referência mutável com `&mut s` onde chamamos a função `change` e atualizamos a assinatura da função para aceitar uma referência mutável com `some_string: &mut String`. Isso deixa muito claro que a função `change` irá mutar o valor que ela empresta.

Referências mutáveis têm uma grande restrição: se você tem uma referência mutável a um valor, você não pode ter outras referências a esse valor. Este código que tenta criar duas referências mutáveis a `s` falhará:

Nome do arquivo: `src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

Aqui está o erro:

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

Este erro diz que este código é inválido porque não podemos emprestar `s` como mutável mais de uma vez por vez. O primeiro empréstimo mutável está em `r1` e deve durar até que seja usado no `println!`, mas entre a criação dessa referência mutável e seu uso, tentamos criar outra referência mutável em `r2` que empresta os mesmos dados que `r1`.

A restrição que impede múltiplas referências mutáveis aos mesmos dados ao mesmo tempo permite a mutação, mas de uma forma muito controlada. É algo com o qual os novos Rustaceans lutam porque a maioria das linguagens permite que você mute sempre que quiser. O benefício de ter essa restrição é que o Rust pode evitar condições de corrida de dados (data races) em tempo de compilação. Uma _condição de corrida de dados_ (data race) é semelhante a uma condição de corrida (race condition) e acontece quando esses três comportamentos ocorrem:

- Dois ou mais ponteiros acessam os mesmos dados ao mesmo tempo.
- Pelo menos um dos ponteiros está sendo usado para escrever nos dados.
- Não há nenhum mecanismo sendo usado para sincronizar o acesso aos dados.

Condições de corrida de dados causam comportamento indefinido e podem ser difíceis de diagnosticar e corrigir quando você está tentando rastreá-las em tempo de execução; Rust impede esse problema recusando-se a compilar código com condições de corrida de dados!

Como sempre, podemos usar chaves para criar um novo escopo, permitindo múltiplas referências mutáveis, mas não _simultâneas_:

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // r1 sai do escopo aqui, então podemos fazer uma nova referência sem problemas

let r2 = &mut s;
```

Rust impõe uma regra semelhante para combinar referências mutáveis e imutáveis. Este código resulta em um erro:

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
let r3 = &mut s; // BIG PROBLEM

println!("{r1}, {r2}, and {r3}");
```

Aqui está o erro:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // no problem
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // no problem
6 |     let r3 = &mut s; // BIG PROBLEM
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

Ufa! _Também_ não podemos ter uma referência mutável enquanto temos uma imutável para o mesmo valor.

Os usuários de uma referência imutável não esperam que o valor mude repentinamente sob eles! No entanto, múltiplas referências imutáveis são permitidas porque ninguém que está apenas lendo os dados tem a capacidade de afetar a leitura dos dados por outra pessoa.

Observe que o escopo de uma referência começa de onde ela é introduzida e continua até a última vez que essa referência é usada. Por exemplo, este código será compilado porque o último uso das referências imutáveis, o `println!`, ocorre antes que a referência mutável seja introduzida:

```rust
let mut s = String::from("hello");

let r1 = &s; // no problem
let r2 = &s; // no problem
println!("{r1} and {r2}");
// variáveis r1 e r2 não serão usadas após este ponto

let r3 = &mut s; // no problem
println!("{r3}");
```

Os escopos das referências imutáveis `r1` e `r2` terminam após o `println!` onde são usadas pela última vez, que é antes que a referência mutável `r3` seja criada. Esses escopos não se sobrepõem, então este código é permitido: o compilador pode dizer que a referência não está mais sendo usada em um ponto antes do final do escopo.

Embora os erros de empréstimo possam ser frustrantes às vezes, lembre-se de que é o compilador Rust que aponta um possível bug no início (em tempo de compilação, em vez de em tempo de execução) e mostra exatamente onde está o problema. Então você não precisa rastrear por que seus dados não são o que você pensava que eram.
