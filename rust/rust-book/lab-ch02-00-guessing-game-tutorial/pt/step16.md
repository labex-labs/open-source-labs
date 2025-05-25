# Saindo Após um Palpite Correto

Vamos programar o jogo para sair quando o usuário vencer, adicionando uma declaração `break`:

Nome do arquivo: `src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

Adicionar a linha `break` após `You win!` faz com que o programa saia do loop quando o usuário adivinha o número secreto corretamente. Sair do loop também significa sair do programa, porque o loop é a última parte de `main`.
