# Criando Comentários de Documentação Úteis

Documentar seus pacotes com precisão ajudará outros usuários a saber como e quando usá-los, por isso vale a pena investir tempo na escrita da documentação. No Capítulo 3, discutimos como comentar o código Rust usando duas barras, `//`. Rust também possui um tipo específico de comentário para documentação, conhecido convenientemente como _comentário de documentação_ (documentation comment), que gerará documentação HTML. O HTML exibe o conteúdo dos comentários de documentação para itens de API pública destinados a programadores interessados em saber como _usar_ seu crate, em oposição a como seu crate é _implementado_.

Comentários de documentação usam três barras, `///`, em vez de duas e suportam a notação Markdown para formatar o texto. Coloque os comentários de documentação logo antes do item que eles estão documentando. A Listagem 14-1 mostra comentários de documentação para uma função `add_one` em um crate chamado `my_crate`.

Nome do arquivo: `src/lib.rs`

````rust
/// Adiciona um ao número fornecido.
///
/// # Exemplos
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
````

Listagem 14-1: Um comentário de documentação para uma função

Aqui, fornecemos uma descrição do que a função `add_one` faz, iniciamos uma seção com o título `Exemplos` e, em seguida, fornecemos código que demonstra como usar a função `add_one`. Podemos gerar a documentação HTML a partir deste comentário de documentação executando `cargo doc`. Este comando executa a ferramenta `rustdoc` distribuída com Rust e coloca a documentação HTML gerada no diretório `target/doc`.

Para conveniência, executar `cargo doc --open` construirá o HTML para a documentação do seu crate atual (bem como a documentação para todas as dependências do seu crate) e abrirá o resultado em um navegador da web. Navegue até a função `add_one` e você verá como o texto nos comentários de documentação é renderizado, conforme mostrado na Figura 14-1.

Figura 14-1: Documentação HTML para a função `add_one`
