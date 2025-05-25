# Removendo um clone usando um iterador

Na Listagem 12-6, adicionamos código que pegava uma fatia de valores `String` e criava uma instância da struct `Config` indexando na fatia e clonando os valores, permitindo que a struct `Config` fosse proprietária desses valores. Na Listagem 13-17, reproduzimos a implementação da função `Config::build` como estava na Listagem 12-23.

Nome do arquivo: `src/lib.rs`

```rust
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

Listagem 13-17: Reprodução da função `Config::build` da Listagem 12-23

Na época, dissemos para não se preocupar com as chamadas `clone` ineficientes porque as removeríamos no futuro. Bem, essa hora é agora!

Precisávamos de `clone` aqui porque temos uma fatia com elementos `String` no parâmetro `args`, mas a função `build` não é proprietária de `args`. Para retornar a propriedade de uma instância `Config`, tivemos que clonar os valores dos campos `query` e `filename` de `Config` para que a instância `Config` pudesse ser proprietária de seus valores.

Com nosso novo conhecimento sobre iteradores, podemos alterar a função `build` para assumir a propriedade de um iterador como seu argumento, em vez de emprestar uma fatia. Usaremos a funcionalidade do iterador em vez do código que verifica o comprimento da fatia e indexa em locais específicos. Isso esclarecerá o que a função `Config::build` está fazendo, porque o iterador acessará os valores.

Assim que `Config::build` assumir a propriedade do iterador e parar de usar operações de indexação que emprestam, podemos mover os valores `String` do iterador para `Config` em vez de chamar `clone` e fazer uma nova alocação.
