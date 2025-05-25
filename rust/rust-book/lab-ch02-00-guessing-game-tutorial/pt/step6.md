# Lidando com Potenciais Falhas com Result

Ainda estamos trabalhando nesta linha de código. Agora estamos discutindo uma terceira linha de texto, mas observe que ela ainda faz parte de uma única linha lógica de código. A próxima parte é este método:

```rust
.expect("Failed to read line");
```

Poderíamos ter escrito este código como:

```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```

No entanto, uma linha longa é difícil de ler, por isso é melhor dividi-la. Muitas vezes, é sensato introduzir uma nova linha e outros espaços em branco para ajudar a quebrar linhas longas quando você chama um método com a sintaxe `.method_name()`. Agora, vamos discutir o que esta linha faz.

Como mencionado anteriormente, `read_line` coloca o que o usuário insere na string que passamos para ela, mas também retorna um valor `Result`. `Result` é uma _enumeração_ (enumeration), frequentemente chamada de _enum_, que é um tipo que pode estar em um de vários estados possíveis. Chamamos cada estado possível de _variante_ (variant).

O Capítulo 6 cobrirá enums com mais detalhes. O objetivo desses tipos `Result` é codificar informações de tratamento de erros.

As variantes de `Result` são `Ok` e `Err`. A variante `Ok` indica que a operação foi bem-sucedida, e dentro de `Ok` está o valor gerado com sucesso. A variante `Err` significa que a operação falhou, e `Err` contém informações sobre como ou por que a operação falhou.

Valores do tipo `Result`, como valores de qualquer tipo, têm métodos definidos neles. Uma instância de `Result` tem um método `expect` que você pode chamar. Se esta instância de `Result` for um valor `Err`, `expect` fará com que o programa trave e exiba a mensagem que você passou como argumento para `expect`. Se o método `read_line` retornar um `Err`, provavelmente será o resultado de um erro vindo do sistema operacional subjacente. Se esta instância de `Result` for um valor `Ok`, `expect` pegará o valor de retorno que `Ok` está mantendo e retornará apenas esse valor para você, para que você possa usá-lo. Neste caso, esse valor é o número de bytes na entrada do usuário.

Se você não chamar `expect`, o programa compilará, mas você receberá um aviso:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
warning: unused `Result` that must be used
  --> src/main.rs:10:5
   |
10 |     io::stdin().read_line(&mut guess);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |
   = note: `#[warn(unused_must_use)]` on by default
   = note: this `Result` may be an `Err` variant, which should be handled

warning: `guessing_game` (bin "guessing_game") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s
```

Rust avisa que você não usou o valor `Result` retornado de `read_line`, indicando que o programa não tratou um possível erro.

A maneira correta de suprimir o aviso é realmente escrever código de tratamento de erros, mas, em nosso caso, só queremos que este programa trave quando um problema ocorrer, então podemos usar `expect`. Você aprenderá sobre como se recuperar de erros no Capítulo 9.
