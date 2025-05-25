# Casos em que Você Tem Mais Informações do que o Compilador

Também seria apropriado chamar `unwrap` ou `expect` quando você tem alguma outra lógica que garante que o `Result` terá um valor `Ok`, mas a lógica não é algo que o compilador entende. Você ainda terá um valor `Result` que precisa ser tratado: qualquer operação que você esteja chamando ainda tem a possibilidade de falhar em geral, mesmo que seja logicamente impossível em sua situação particular. Se você pode garantir, inspecionando manualmente o código, que nunca terá uma variante `Err`, é perfeitamente aceitável chamar `unwrap`, e ainda melhor documentar a razão pela qual você acha que nunca terá uma variante `Err` no texto `expect`. Aqui está um exemplo:

```rust
use std::net::IpAddr;

let home: IpAddr = "127.0.0.1"
    .parse()
    .expect("Hardcoded IP address should be valid");
```

Estamos criando uma instância `IpAddr` analisando uma string codificada. Podemos ver que `127.0.0.1` é um endereço IP válido, então é aceitável usar `expect` aqui. No entanto, ter uma string válida e codificada não altera o tipo de retorno do método `parse`: ainda obtemos um valor `Result`, e o compilador ainda nos fará tratar o `Result` como se a variante `Err` fosse uma possibilidade, porque o compilador não é inteligente o suficiente para ver que esta string é sempre um endereço IP válido. Se a string do endereço IP viesse de um usuário em vez de ser codificada no programa e, portanto, _tivesse_ a possibilidade de falha, definitivamente gostaríamos de tratar o `Result` de uma maneira mais robusta. Mencionar a suposição de que este endereço IP é codificado nos levará a mudar `expect` para um código de tratamento de erros melhor se, no futuro, precisarmos obter o endereço IP de alguma outra fonte.
