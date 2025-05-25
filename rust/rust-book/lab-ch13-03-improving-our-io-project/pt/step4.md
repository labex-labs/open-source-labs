# Usando Métodos de Trait de Iterador em Vez de Indexação

Em seguida, corrigiremos o corpo de `Config::build`. Como `args` implementa o trait `Iterator`, sabemos que podemos chamar o método `next` nele! A Listagem 13-20 atualiza o código da Listagem 12-23 para usar o método `next`.

Nome do arquivo: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listagem 13-20: Alterando o corpo de `Config::build` para usar métodos de iterador

Lembre-se de que o primeiro valor no valor de retorno de `env::args` é o nome do programa. Queremos ignorá-lo e ir para o próximo valor, então primeiro chamamos `next` e não fazemos nada com o valor de retorno. Em seguida, chamamos `next` para obter o valor que queremos colocar no campo `query` de `Config`. Se `next` retornar `Some`, usamos um `match` para extrair o valor. Se retornar `None`, significa que não foram fornecidos argumentos suficientes e retornamos antecipadamente com um valor `Err`. Fazemos a mesma coisa para o valor `filename`.
