# Compilação e Execução são Etapas Separadas

Você acabou de executar um programa recém-criado, então vamos examinar cada etapa do processo.

Antes de executar um programa Rust, você deve compilá-lo usando o compilador Rust, inserindo o comando `rustc` e passando o nome do seu arquivo de código-fonte, assim:

```bash
rustc main.rs
```

Se você tem experiência com C ou C++, notará que isso é semelhante a `gcc` ou `clang`. Após compilar com sucesso, Rust gera um executável binário.

No Linux, macOS e PowerShell no Windows, você pode ver o executável inserindo o comando `ls` no seu shell:

```bash
$ ls
main main.rs
```

A partir daqui, você executa o arquivo `main`, assim:

```bash
./main
```

Se seu `main.rs` for seu programa "Hello, world!", esta linha imprime `Hello, world!` no seu terminal.

Se você está mais familiarizado com uma linguagem dinâmica, como Ruby, Python ou JavaScript, pode não estar acostumado a compilar e executar um programa como etapas separadas. Rust é uma linguagem _compilada antecipadamente_ (ahead-of-time compiled), o que significa que você pode compilar um programa e dar o executável para outra pessoa, e ela pode executá-lo mesmo sem ter o Rust instalado. Se você der a alguém um arquivo `.rb`, `.py` ou `.js`, ela precisa ter uma implementação Ruby, Python ou JavaScript instalada (respectivamente). Mas nessas linguagens, você só precisa de um comando para compilar e executar seu programa. Tudo é uma troca no design de linguagem.

Apenas compilar com `rustc` é bom para programas simples, mas à medida que seu projeto cresce, você vai querer gerenciar todas as opções e facilitar o compartilhamento do seu código. Em seguida, apresentaremos a ferramenta Cargo, que o ajudará a escrever programas Rust do mundo real.
