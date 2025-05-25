# Chamando Config::build e Lidando com Erros

Para lidar com o caso de erro e imprimir uma mensagem amigável ao usuário, precisamos atualizar `main` para lidar com o `Result` que está sendo retornado por `Config::build`, como mostrado na Listagem 12-10. Também assumiremos a responsabilidade de sair da ferramenta de linha de comando com um código de erro diferente de zero, em vez de `panic!`, e, em vez disso, implementá-lo manualmente. Um status de saída diferente de zero é uma convenção para sinalizar ao processo que chamou nosso programa que o programa saiu com um estado de erro.

Nome do arquivo: `src/main.rs`

```rust
1 use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

  2 let config = Config::build(&args).3 unwrap_or_else(|4 err| {
      5 println!("Problem parsing arguments: {err}");
      6 process::exit(1);
    });

    --snip--
```

Listagem 12-10: Saindo com um código de erro se a construção de um `Config` falhar

Nesta listagem, usamos um método que ainda não cobrimos em detalhes: `unwrap_or_else`, que é definido em `Result<T, E>` pela biblioteca padrão \[2]. Usar `unwrap_or_else` nos permite definir algum tratamento de erro personalizado, não `panic!`. Se o `Result` for um valor `Ok`, o comportamento deste método é semelhante a `unwrap`: ele retorna o valor interno que `Ok` está encapsulando. No entanto, se o valor for um valor `Err`, este método chama o código na _closure_ (fechamento), que é uma função anônima que definimos e passamos como um argumento para `unwrap_or_else` \[3]. Cobriremos fechamentos em mais detalhes no Capítulo 13. Por enquanto, você só precisa saber que `unwrap_or_else` passará o valor interno do `Err`, que neste caso é a string estática `"not enough arguments"` que adicionamos na Listagem 12-9, para nosso fechamento no argumento `err` que aparece entre as barras verticais \[4]. O código no fechamento pode então usar o valor `err` quando ele é executado.

Adicionamos uma nova linha `use` para trazer `process` da biblioteca padrão para o escopo \[1]. O código no fechamento que será executado no caso de erro tem apenas duas linhas: imprimimos o valor `err` \[5] e, em seguida, chamamos `process::exit` \[6]. A função `process::exit` interromperá o programa imediatamente e retornará o número que foi passado como o código de status de saída. Isso é semelhante ao tratamento baseado em `panic!` que usamos na Listagem 12-8, mas não obtemos mais toda a saída extra. Vamos tentar:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.48s
     Running `target/debug/minigrep`
Problem parsing arguments: not enough arguments
```

Ótimo! Esta saída é muito mais amigável para nossos usuários.
