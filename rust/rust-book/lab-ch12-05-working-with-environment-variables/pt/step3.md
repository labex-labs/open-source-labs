# Implementando a Função `search_case_insensitive`

A função `search_case_insensitive`, mostrada na Listagem 12-21, será quase a mesma que a função `search`. A única diferença é que converteremos a `query` e cada `line` para minúsculas, de modo que, qualquer que seja o caso dos argumentos de entrada, eles estarão no mesmo caso quando verificarmos se a linha contém a consulta.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Listagem 12-21: Definindo a função `search_case_insensitive` para converter a consulta e a linha para minúsculas antes de compará-las

Primeiro, convertemos a string `query` para minúsculas e a armazenamos em uma variável sombreada com o mesmo nome \[1]. Chamar `to_lowercase` na consulta é necessário para que, independentemente de a consulta do usuário ser `"rust"`, `"RUST"`, `"Rust"` ou `"rUsT"`, tratemos a consulta como se fosse `"rust"` e sejamos insensíveis ao caso. Embora `to_lowercase` lide com Unicode básico, não será 100% preciso. Se estivéssemos escrevendo uma aplicação real, gostaríamos de fazer um pouco mais de trabalho aqui, mas esta seção é sobre variáveis de ambiente, não sobre Unicode, então vamos deixar assim por aqui.

Observe que `query` agora é um `String` em vez de uma fatia de string porque chamar `to_lowercase` cria novos dados em vez de referenciar dados existentes. Digamos que a consulta seja `"rUsT"`, como exemplo: essa fatia de string não contém um `u` ou `t` minúsculo para usarmos, então temos que alocar um novo `String` contendo `"rust"`. Quando passamos `query` como um argumento para o método `contains` agora, precisamos adicionar um "e comercial" \[3] porque a assinatura de `contains` é definida para receber uma fatia de string.

Em seguida, adicionamos uma chamada para `to_lowercase` em cada `line` para converter todos os caracteres para minúsculas \[2]. Agora que convertemos `line` e `query` para minúsculas, encontraremos correspondências, independentemente do caso da consulta.

Vamos ver se esta implementação passa nos testes:

    running 2 tests
    test tests::case_insensitive ... ok
    test tests::case_sensitive ... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Ótimo! Eles passaram. Agora, vamos chamar a nova função `search_case_insensitive` da função `run`. Primeiro, adicionaremos uma opção de configuração à struct `Config` para alternar entre pesquisa com e sem distinção entre maiúsculas e minúsculas. Adicionar este campo causará erros de compilação porque ainda não estamos inicializando este campo em nenhum lugar:

Nome do arquivo: `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

Adicionamos o campo `ignore_case` que contém um booleano. Em seguida, precisamos que a função `run` verifique o valor do campo `ignore_case` e use isso para decidir se deve chamar a função `search` ou a função `search_case_insensitive`, conforme mostrado na Listagem 12-22. Isso ainda não compilará.

Nome do arquivo: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Listagem 12-22: Chamando `search` ou `search_case_insensitive` com base no valor em `config.ignore_case`

Finalmente, precisamos verificar a variável de ambiente. As funções para trabalhar com variáveis de ambiente estão no módulo `env` na biblioteca padrão, então trazemos esse módulo para o escopo no topo de `src/lib.rs`. Em seguida, usaremos a função `var` do módulo `env` para verificar se algum valor foi definido para uma variável de ambiente chamada `IGNORE_CASE`, conforme mostrado na Listagem 12-23.

Nome do arquivo: `src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listagem 12-23: Verificando qualquer valor em uma variável de ambiente chamada `IGNORE_CASE`

Aqui, criamos uma nova variável, `ignore_case`. Para definir seu valor, chamamos a função `env::var` e passamos a ela o nome da variável de ambiente `IGNORE_CASE`. A função `env::var` retorna um `Result` que será a variante `Ok` bem-sucedida que contém o valor da variável de ambiente se a variável de ambiente estiver definida para qualquer valor. Ele retornará a variante `Err` se a variável de ambiente não estiver definida.

Estamos usando o método `is_ok` no `Result` para verificar se a variável de ambiente está definida, o que significa que o programa deve fazer uma pesquisa sem distinção entre maiúsculas e minúsculas. Se a variável de ambiente `IGNORE_CASE` não estiver definida para nada, `is_ok` retornará `false` e o programa executará uma pesquisa com distinção entre maiúsculas e minúsculas. Não nos importamos com o _valor_ da variável de ambiente, apenas se ela está definida ou não, então estamos verificando `is_ok` em vez de usar `unwrap`, `expect` ou qualquer um dos outros métodos que vimos em `Result`.

Passamos o valor na variável `ignore_case` para a instância `Config` para que a função `run` possa ler esse valor e decidir se deve chamar `search_case_insensitive` ou `search`, como implementamos na Listagem 12-22.

Vamos tentar! Primeiro, executaremos nosso programa sem a variável de ambiente definida e com a consulta `to`, que deve corresponder a qualquer linha que contenha a palavra _to_ em letras minúsculas:

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

Parece que ainda funciona! Agora, vamos executar o programa com `IGNORE_CASE` definido como `1`, mas com a mesma consulta `to`:

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

Se você estiver usando o PowerShell, precisará definir a variável de ambiente e executar o programa como comandos separados:

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

Isso fará com que `IGNORE_CASE` persista pelo restante da sua sessão do shell. Ele pode ser desfeito com o cmdlet `Remove-Item`:

```rust
PS> Remove-Item Env:IGNORE_CASE
```

Devemos obter linhas que contenham _to_ que podem ter letras maiúsculas:

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

Excelente, também obtivemos linhas contendo _To_! Nosso programa `minigrep` agora pode fazer pesquisas sem distinção entre maiúsculas e minúsculas controladas por uma variável de ambiente. Agora você sabe como gerenciar opções definidas usando argumentos de linha de comando ou variáveis de ambiente.

Alguns programas permitem argumentos _e_ variáveis de ambiente para a mesma configuração. Nesses casos, os programas decidem que um ou outro tem precedência. Para outro exercício por conta própria, tente controlar a sensibilidade a maiúsculas e minúsculas por meio de um argumento de linha de comando ou de uma variável de ambiente. Decida se o argumento da linha de comando ou a variável de ambiente deve ter precedência se o programa for executado com um definido como sensível a maiúsculas e minúsculas e outro definido para ignorar maiúsculas e minúsculas.

O módulo `std::env` contém muitos mais recursos úteis para lidar com variáveis de ambiente: consulte sua documentação para ver o que está disponível.
