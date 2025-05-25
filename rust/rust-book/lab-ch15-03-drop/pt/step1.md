# Executando Código na Limpeza com a Trait Drop

A segunda trait importante para o padrão de ponteiro inteligente (smart pointer) é `Drop`, que permite personalizar o que acontece quando um valor está prestes a sair do escopo. Você pode fornecer uma implementação para a trait `Drop` em qualquer tipo, e esse código pode ser usado para liberar recursos como arquivos ou conexões de rede.

Estamos introduzindo `Drop` no contexto de ponteiros inteligentes porque a funcionalidade da trait `Drop` é quase sempre usada ao implementar um ponteiro inteligente. Por exemplo, quando um `Box<T>` é descartado, ele desalocará o espaço na heap (heap) que a caixa aponta.

Em algumas linguagens, para alguns tipos, o programador deve chamar código para liberar memória ou recursos toda vez que terminar de usar uma instância desses tipos. Exemplos incluem manipuladores de arquivos, sockets e bloqueios. Se eles esquecerem, o sistema pode ficar sobrecarregado e travar. Em Rust, você pode especificar que um determinado trecho de código seja executado sempre que um valor sair do escopo, e o compilador inserirá esse código automaticamente. Como resultado, você não precisa ter cuidado ao colocar código de limpeza em todos os lugares de um programa em que uma instância de um tipo específico é finalizada - você ainda não vazará recursos!

Você especifica o código a ser executado quando um valor sai do escopo implementando a trait `Drop`. A trait `Drop` exige que você implemente um método chamado `drop` que recebe uma referência mutável para `self`. Para ver quando o Rust chama `drop`, vamos implementar `drop` com instruções `println!` por enquanto.

O Listing 15-14 mostra uma struct `CustomSmartPointer` cuja única funcionalidade personalizada é que ela imprimirá `Dropping CustomSmartPointer!` quando a instância sair do escopo, para mostrar quando o Rust executa o método `drop`.

Nome do arquivo: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14: Uma struct `CustomSmartPointer` que implementa a trait `Drop` onde colocaríamos nosso código de limpeza

A trait `Drop` está incluída no prelúdio (prelude), então não precisamos trazê-la para o escopo. Implementamos a trait `Drop` em `CustomSmartPointer` \[1] e fornecemos uma implementação para o método `drop` que chama `println!` \[2]. O corpo do método `drop` é onde você colocaria qualquer lógica que você quisesse executar quando uma instância do seu tipo sair do escopo. Estamos imprimindo algum texto aqui para demonstrar visualmente quando o Rust chamará `drop`.

Em `main`, criamos duas instâncias de `CustomSmartPointer` em \[3] e \[4] e, em seguida, imprimimos `CustomSmartPointers created` \[5]. No final de `main` \[6], nossas instâncias de `CustomSmartPointer` sairão do escopo, e o Rust chamará o código que colocamos no método `drop` \[2], imprimindo nossa mensagem final. Observe que não precisamos chamar o método `drop` explicitamente.

Quando executamos este programa, veremos a seguinte saída:

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

O Rust chamou automaticamente `drop` para nós quando nossas instâncias saíram do escopo, chamando o código que especificamos. As variáveis são descartadas na ordem inversa de sua criação, então `d` foi descartado antes de `c`. O objetivo deste exemplo é fornecer um guia visual de como o método `drop` funciona; geralmente, você especificaria o código de limpeza que seu tipo precisa executar em vez de uma mensagem de impressão.

Infelizmente, não é simples desabilitar a funcionalidade automática de `drop`. Desabilitar `drop` geralmente não é necessário; o objetivo da trait `Drop` é que ela seja cuidada automaticamente. Ocasionalmente, no entanto, você pode querer limpar um valor antecipadamente. Um exemplo é ao usar ponteiros inteligentes que gerenciam bloqueios: você pode querer forçar o método `drop` que libera o bloqueio para que outro código no mesmo escopo possa adquirir o bloqueio. O Rust não permite que você chame o método `drop` da trait `Drop` manualmente; em vez disso, você deve chamar a função `std::mem::drop` fornecida pela biblioteca padrão se quiser forçar um valor a ser descartado antes do final de seu escopo.

Se tentarmos chamar o método `drop` da trait `Drop` manualmente, modificando a função `main` do Listing 15-14, conforme mostrado no Listing 15-15, obteremos um erro do compilador.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15: Tentando chamar o método `drop` da trait `Drop` manualmente para limpar antecipadamente

Quando tentamos compilar este código, obteremos este erro:

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

Esta mensagem de erro afirma que não é permitido chamar `drop` explicitamente. A mensagem de erro usa o termo _destructor_ (destruidor), que é o termo geral de programação para uma função que limpa uma instância. Um _destructor_ é análogo a um _constructor_ (construtor), que cria uma instância. A função `drop` em Rust é um destruidor específico.

O Rust não nos permite chamar `drop` explicitamente porque o Rust ainda chamaria automaticamente `drop` no valor no final de `main`. Isso causaria um erro de _double free_ (liberação dupla) porque o Rust estaria tentando limpar o mesmo valor duas vezes.

Não podemos desabilitar a inserção automática de `drop` quando um valor sai do escopo, e não podemos chamar o método `drop` explicitamente. Portanto, se precisarmos forçar um valor a ser limpo antecipadamente, usamos a função `std::mem::drop`.

A função `std::mem::drop` é diferente do método `drop` na trait `Drop`. Chamamos-a passando como argumento o valor que queremos forçar a descartar. A função está no prelúdio, então podemos modificar `main` no Listing 15-15 para chamar a função `drop`, conforme mostrado no Listing 15-16.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16: Chamando `std::mem::drop` para descartar explicitamente um valor antes que ele saia do escopo

A execução deste código imprimirá o seguinte:

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

O texto `Dropping CustomSmartPointer with data`some data`!` é impresso entre o texto `CustomSmartPointer created.` e `CustomSmartPointer dropped before the end of main.`, mostrando que o código do método `drop` é chamado para descartar `c` nesse ponto.

Você pode usar o código especificado em uma implementação da trait `Drop` de várias maneiras para tornar a limpeza conveniente e segura: por exemplo, você pode usá-lo para criar seu próprio alocador de memória! Com a trait `Drop` e o sistema de propriedade do Rust, você não precisa se lembrar de limpar porque o Rust faz isso automaticamente.

Você também não precisa se preocupar com problemas resultantes da limpeza acidental de valores ainda em uso: o sistema de propriedade que garante que as referências sejam sempre válidas também garante que `drop` seja chamado apenas uma vez quando o valor não estiver mais sendo usado.

Agora que examinamos `Box<T>` e algumas das características dos ponteiros inteligentes, vamos dar uma olhada em alguns outros ponteiros inteligentes definidos na biblioteca padrão.
