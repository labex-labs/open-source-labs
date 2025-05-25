# Repetindo Código com `loop`

A palavra-chave `loop` diz ao Rust para executar um bloco de código repetidamente para sempre ou até que você explicitamente diga para parar.

Como exemplo, altere o arquivo `src/main.rs` no seu diretório `loops` para que se pareça com isto:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    loop {
        println!("again!");
    }
}
```

Quando executamos este programa, veremos `again!` impresso repetidamente e continuamente até pararmos o programa manualmente. A maioria dos terminais suporta o atalho de teclado ctrl-C para interromper um programa que está preso em um loop contínuo. Experimente:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29s
     Running `target/debug/loops`
again!
again!
again!
again!
^Cagain!
```

O símbolo `^C` representa onde você pressionou ctrl-C. Você pode ou não ver a palavra `again!` impressa após o `^C`, dependendo de onde o código estava no loop quando recebeu o sinal de interrupção.

Felizmente, Rust também fornece uma maneira de sair de um loop usando código. Você pode colocar a palavra-chave `break` dentro do loop para dizer ao programa quando parar de executar o loop. Lembre-se que fizemos isso no jogo de adivinhação em "Saindo Após um Palpite Correto" para sair do programa quando o usuário vencia o jogo ao adivinhar o número correto.

Também usamos `continue` no jogo de adivinhação, que em um loop diz ao programa para pular qualquer código restante nesta iteração do loop e ir para a próxima iteração.
