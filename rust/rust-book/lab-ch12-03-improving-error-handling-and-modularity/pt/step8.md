# Retornando um Result em Vez de Chamar panic!

Em vez disso, podemos retornar um valor `Result` que conterá uma instância `Config` no caso de sucesso e descreverá o problema no caso de erro. Também vamos mudar o nome da função de `new` para `build` porque muitos programadores esperam que as funções `new` nunca falhem. Quando `Config::build` estiver se comunicando com `main`, podemos usar o tipo `Result` para sinalizar que houve um problema. Então, podemos mudar `main` para converter uma variante `Err` em um erro mais prático para nossos usuários, sem o texto circundante sobre `thread 'main'` e `RUST_BACKTRACE` que uma chamada para `panic!` causa.

A Listagem 12-9 mostra as mudanças que precisamos fazer no valor de retorno da função que agora estamos chamando de `Config::build` e no corpo da função necessário para retornar um `Result`. Observe que isso não compilará até que atualizemos `main` também, o que faremos na próxima listagem.

Nome do arquivo: `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

Listagem 12-9: Retornando um `Result` de `Config::build`

Nossa função `build` retorna um `Result` com uma instância `Config` no caso de sucesso e um `&'static str` no caso de erro. Nossos valores de erro sempre serão literais de string que têm o tempo de vida `'static`.

Fizemos duas mudanças no corpo da função: em vez de chamar `panic!` quando o usuário não passa argumentos suficientes, agora retornamos um valor `Err`, e envolvemos o valor de retorno `Config` em um `Ok`. Essas mudanças fazem com que a função se conforme à sua nova assinatura de tipo.

Retornar um valor `Err` de `Config::build` permite que a função `main` lide com o valor `Result` retornado da função `build` e saia do processo de forma mais limpa no caso de erro.
