# A Anatomia de uma Função de Teste

Em sua forma mais simples, um teste em Rust é uma função que é anotada com o atributo `test`. Atributos são metadados sobre partes do código Rust; um exemplo é o atributo `derive` que usamos com structs no Capítulo 5. Para transformar uma função em uma função de teste, adicione `#[test]` na linha antes de `fn`. Quando você executa seus testes com o comando `cargo test`, o Rust constrói um binário de execução de testes que executa as funções anotadas e relata se cada função de teste passa ou falha.

Sempre que criamos um novo projeto de biblioteca com o Cargo, um módulo de teste com uma função de teste é gerado automaticamente para nós. Este módulo fornece um modelo para escrever seus testes, para que você não precise procurar a estrutura e a sintaxe exatas toda vez que iniciar um novo projeto. Você pode adicionar quantas funções de teste adicionais e quantos módulos de teste quiser!

Vamos explorar alguns aspectos de como os testes funcionam, experimentando o teste de modelo antes de realmente testar qualquer código. Em seguida, escreveremos alguns testes do mundo real que chamam algum código que escrevemos e afirmam que seu comportamento está correto.

Vamos criar um novo projeto de biblioteca chamado `adder` que irá somar dois números:

```bash
$ cargo new adder --lib
Created library $(adder) project
$ cd adder
```

O conteúdo do arquivo `src/lib.rs` em sua biblioteca `adder` deve ser semelhante ao da Listagem 11-1.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

Listagem 11-1: O módulo de teste e a função gerados automaticamente por `cargo new`

Por enquanto, vamos ignorar as duas primeiras linhas e focar na função. Observe a anotação `#[test]` \[1]: este atributo indica que esta é uma função de teste, então o executor de testes sabe que deve tratar esta função como um teste. Também podemos ter funções que não são de teste no módulo `tests` para ajudar a configurar cenários comuns ou realizar operações comuns, então sempre precisamos indicar quais funções são testes.

O corpo da função de exemplo usa a macro `assert_eq!` \[2] para afirmar que `result`, que contém o resultado da soma de 2 e 2, é igual a 4. Essa asserção serve como um exemplo do formato para um teste típico. Vamos executá-lo para ver que este teste passa.

O comando `cargo test` executa todos os testes em nosso projeto, conforme mostrado na Listagem 11-2.

```bash
[object Object]
```

Listagem 11-2: A saída da execução do teste gerado automaticamente

O Cargo compilou e executou o teste. Vemos a linha `running 1 test` \[1]. A próxima linha mostra o nome da função de teste gerada, chamada `it_works`, e que o resultado da execução desse teste é `ok` \[2]. O resumo geral `test result: ok.` \[3] significa que todos os testes passaram, e a parte que diz `1 passed; 0 failed` totaliza o número de testes que passaram ou falharam.

É possível marcar um teste como ignorado para que ele não seja executado em uma instância específica; abordaremos isso em "Ignorando Alguns Testes, a Menos que Especificamente Solicitado". Como não fizemos isso aqui, o resumo mostra `0 ignored`. Também podemos passar um argumento para o comando `cargo test` para executar apenas testes cujo nome corresponda a uma string; isso é chamado de _filtragem_ e abordaremos isso em "Executando um Subconjunto de Testes por Nome". Aqui, não filtramos os testes que estão sendo executados, então o final do resumo mostra `0 filtered out`.

A estatística `0 measured` é para testes de benchmark que medem o desempenho. Testes de benchmark estão, no momento em que este texto é escrito, disponíveis apenas no Rust nightly. Consulte a documentação sobre testes de benchmark em *https://doc.rust-lang.org/unstable-book/library-features/test.html* para saber mais.

A próxima parte da saída do teste, começando em `Doc-tests adder` \[4], é para os resultados de quaisquer testes de documentação. Ainda não temos nenhum teste de documentação, mas o Rust pode compilar quaisquer exemplos de código que apareçam em nossa documentação da API. Esse recurso ajuda a manter seus documentos e seu código sincronizados! Discutiremos como escrever testes de documentação em "Comentários de Documentação como Testes". Por enquanto, ignoraremos a saída `Doc-tests`.

Vamos começar a personalizar o teste para nossas próprias necessidades. Primeiro, altere o nome da função `it_works` para um nome diferente, como `exploration`, assim:

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Em seguida, execute `cargo test` novamente. A saída agora mostra `exploration` em vez de `it_works`:

    running 1 test
    test tests::exploration ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Agora, adicionaremos outro teste, mas desta vez faremos um teste que falha! Os testes falham quando algo na função de teste entra em pânico. Cada teste é executado em um novo thread, e quando o thread principal vê que um thread de teste morreu, o teste é marcado como falhado. No Capítulo 9, falamos sobre como a maneira mais simples de entrar em pânico é chamar a macro `panic!`. Insira o novo teste como uma função chamada `another`, para que seu arquivo `src/lib.rs` fique como a Listagem 11-3.

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
```

Listagem 11-3: Adicionando um segundo teste que falhará porque chamamos a macro `panic!`

Execute os testes novamente usando `cargo test`. A saída deve ser semelhante à Listagem 11-4, que mostra que nosso teste `exploration` passou e `another` falhou.

    running 2 tests
    test tests::exploration ... ok
    1 test tests::another ... FAILED

    2 failures:

    ---- tests::another stdout ----
    thread 'main' panicked at 'Make this test fail', src/lib.rs:10:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    3 failures:
        tests::another

    4 test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

    error: test failed, to rerun pass '--lib'

Listagem 11-4: Resultados do teste quando um teste passa e um teste falha

Em vez de `ok`, a linha `test tests::another` mostra `FAILED` \[1]. Duas novas seções aparecem entre os resultados individuais e o resumo: a primeira \[2] exibe o motivo detalhado de cada falha no teste. Neste caso, obtemos os detalhes de que `another` falhou porque entrou em pânico em `'Make this test fail'` na linha 10 no arquivo `src/lib.rs`. A próxima seção \[3] lista apenas os nomes de todos os testes com falha, o que é útil quando há muitos testes e muita saída detalhada de testes com falha. Podemos usar o nome de um teste com falha para executar apenas esse teste para depurá-lo mais facilmente; falaremos mais sobre maneiras de executar testes em "Controlando Como os Testes São Executados".

A linha de resumo é exibida no final \[4]: no geral, nosso resultado do teste é `FAILED`. Tivemos um teste que passou e um teste que falhou.

Agora que você viu como os resultados do teste se parecem em diferentes cenários, vamos analisar algumas macros diferentes de `panic!` que são úteis em testes.
