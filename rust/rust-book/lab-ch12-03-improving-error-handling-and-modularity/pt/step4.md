# Agrupando Valores de Configuração

Podemos dar mais um pequeno passo para melhorar ainda mais a função `parse_config`. No momento, estamos retornando uma tupla, mas então quebramos imediatamente essa tupla em partes individuais novamente. Este é um sinal de que talvez ainda não tenhamos a abstração correta.

Outro indicador que mostra que há espaço para melhorias é a parte `config` de `parse_config`, o que implica que os dois valores que retornamos estão relacionados e fazem parte de um valor de configuração. Atualmente, não estamos transmitindo esse significado na estrutura dos dados, exceto agrupando os dois valores em uma tupla; em vez disso, colocaremos os dois valores em uma struct e daremos a cada um dos campos da struct um nome significativo. Fazer isso facilitará para os futuros mantenedores deste código entenderem como os diferentes valores se relacionam entre si e qual é o seu propósito.

A Listagem 12-6 mostra as melhorias na função `parse_config`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = parse_config(&args);

    println!("Searching for {}", 2 config.query);
    println!("In file {}", 3 config.file_path);

    let contents = fs::read_to_string(4 config.file_path)
        .expect("Should have been able to read the file");

    --snip--
}

5 struct Config {
    query: String,
    file_path: String,
}

6 fn parse_config(args: &[String]) -> Config {
  7 let query = args[1].clone();
  8 let file_path = args[2].clone();

    Config { query, file_path }
}
```

Listagem 12-6: Refatorando `parse_config` para retornar uma instância de uma struct `Config`

Adicionamos uma struct chamada `Config` definida para ter campos chamados `query` e `file_path` \[5]. A assinatura de `parse_config` agora indica que ela retorna um valor `Config` \[6]. No corpo de `parse_config`, onde costumávamos retornar fatias de string que referenciam valores `String` em `args`, agora definimos `Config` para conter valores `String` próprios. A variável `args` em `main` é a proprietária dos valores dos argumentos e só está permitindo que a função `parse_config` os empreste, o que significa que violaríamos as regras de empréstimo do Rust se `Config` tentasse assumir a propriedade dos valores em `args`.

Há várias maneiras de gerenciar os dados `String`; a rota mais fácil, embora um tanto ineficiente, é chamar o método `clone` nos valores \[7] \[8]. Isso fará uma cópia completa dos dados para a instância `Config` possuir, o que leva mais tempo e memória do que armazenar uma referência aos dados da string. No entanto, clonar os dados também torna nosso código muito direto porque não precisamos gerenciar os tempos de vida das referências; nessas circunstâncias, abrir mão de um pouco de desempenho para ganhar simplicidade é uma troca que vale a pena.

> **As Trocas de Usar clone**
>
> Há uma tendência entre muitos Rustaceans de evitar o uso de `clone` para corrigir problemas de propriedade devido ao seu custo em tempo de execução. No Capítulo 13, você aprenderá como usar métodos mais eficientes nesse tipo de situação. Mas, por enquanto, tudo bem copiar algumas strings para continuar progredindo, porque você fará essas cópias apenas uma vez e seu caminho do arquivo e a string de consulta são muito pequenos. É melhor ter um programa funcionando que seja um pouco ineficiente do que tentar hiperotimizar o código na sua primeira passagem. À medida que você se torna mais experiente com Rust, será mais fácil começar com a solução mais eficiente, mas, por enquanto, é perfeitamente aceitável chamar `clone`.

Atualizamos `main` para que ele coloque a instância de `Config` retornada por `parse_config` em uma variável chamada `config` \[1], e atualizamos o código que anteriormente usava as variáveis separadas `query` e `file_path` para que agora use os campos na struct `Config` em vez disso \[2] \[3] \[4].

Agora, nosso código transmite mais claramente que `query` e `file_path` estão relacionados e que seu propósito é configurar como o programa funcionará. Qualquer código que use esses valores sabe onde encontrá-los na instância `config` nos campos nomeados para sua finalidade.
