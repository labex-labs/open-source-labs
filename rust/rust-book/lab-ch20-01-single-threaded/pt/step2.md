# Ouvindo a Conexão TCP

Nosso servidor web precisa ouvir uma conexão TCP, então essa é a primeira parte em que trabalharemos. A biblioteca padrão oferece um módulo `std::net` que nos permite fazer isso. Vamos criar um novo projeto da maneira usual:

```bash
$ cargo new hello
     Created binary (application) `hello` project
$ cd hello
```

Agora, insira o código na Listagem 20-1 em `src/main.rs` para começar. Este código ouvirá no endereço local `127.0.0.1:7878` por fluxos TCP de entrada. Quando receber um fluxo de entrada, ele imprimirá `Connection established!`.

Nome do arquivo: `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
  1 let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

  2 for stream in listener.incoming() {
      3 let stream = stream.unwrap();

      4 println!("Connection established!");
    }
}
```

Listagem 20-1: Ouvindo fluxos de entrada e imprimindo uma mensagem quando recebemos um fluxo

Usando `TcpListener`, podemos ouvir conexões TCP no endereço `127.0.0.1:7878` \[1]. No endereço, a seção antes dos dois pontos é um endereço IP que representa seu computador (este é o mesmo em todos os computadores e não representa o computador dos autores especificamente), e `7878` é a porta. Escolhemos esta porta por duas razões: HTTP normalmente não é aceito nesta porta, então é improvável que nosso servidor entre em conflito com qualquer outro servidor web que você possa estar executando em sua máquina, e 7878 é _rust_ digitado em um telefone.

A função `bind` neste cenário funciona como a função `new`, pois retornará uma nova instância de `TcpListener`. A função é chamada `bind` porque, em rede, conectar-se a uma porta para ouvir é conhecido como "vincular a uma porta".

A função `bind` retorna um `Result<T, E>`, o que indica que é possível que a vinculação falhe. Por exemplo, conectar-se à porta 80 requer privilégios de administrador (não administradores podem ouvir apenas em portas superiores a 1023), então, se tentássemos conectar-se à porta 80 sem ser um administrador, a vinculação não funcionaria. A vinculação também não funcionaria, por exemplo, se executássemos duas instâncias do nosso programa e, portanto, tivéssemos dois programas ouvindo na mesma porta. Como estamos escrevendo um servidor básico apenas para fins de aprendizado, não nos preocuparemos em lidar com esse tipo de erro; em vez disso, usamos `unwrap` para interromper o programa se ocorrerem erros.

O método `incoming` em `TcpListener` retorna um iterador que nos dá uma sequência de fluxos \[2] (mais especificamente, fluxos do tipo `TcpStream`). Um único _fluxo_ representa uma conexão aberta entre o cliente e o servidor. Uma _conexão_ é o nome do processo completo de requisição e resposta no qual um cliente se conecta ao servidor, o servidor gera uma resposta e o servidor fecha a conexão. Como tal, leremos do `TcpStream` para ver o que o cliente enviou e, em seguida, escreveremos nossa resposta no fluxo para enviar dados de volta ao cliente. No geral, este loop `for` processará cada conexão por sua vez e produzirá uma série de fluxos para que possamos lidar.

Por enquanto, nosso tratamento do fluxo consiste em chamar `unwrap` para encerrar nosso programa se o fluxo tiver algum erro \[3]; se não houver erros, o programa imprime uma mensagem \[4]. Adicionaremos mais funcionalidade para o caso de sucesso na próxima listagem. A razão pela qual podemos receber erros do método `incoming` quando um cliente se conecta ao servidor é que, na verdade, não estamos iterando sobre conexões. Em vez disso, estamos iterando sobre _tentativas de conexão_. A conexão pode não ser bem-sucedida por vários motivos, muitos deles específicos do sistema operacional (OS). Por exemplo, muitos sistemas operacionais têm um limite para o número de conexões abertas simultâneas que podem suportar; novas tentativas de conexão além desse número produzirão um erro até que algumas das conexões abertas sejam fechadas.

Vamos tentar executar este código! Invoque `cargo run` no terminal e, em seguida, carregue _127.0.0.1:7878_ em um navegador web. O navegador deve mostrar uma mensagem de erro como "Connection reset" porque o servidor não está enviando nenhum dado no momento. Mas quando você olha para o seu terminal, você deve ver várias mensagens que foram impressas quando o navegador se conectou ao servidor!

         Running `target/debug/hello`
    Connection established!
    Connection established!
    Connection established!

Às vezes, você verá várias mensagens impressas para uma solicitação do navegador; a razão pode ser que o navegador está fazendo uma solicitação para a página, bem como uma solicitação para outros recursos, como o ícone _favicon.ico_ que aparece na guia do navegador.

Também pode ser que o navegador esteja tentando se conectar ao servidor várias vezes porque o servidor não está respondendo com nenhum dado. Quando `stream` sai do escopo e é descartado no final do loop, a conexão é fechada como parte da implementação `drop`. Os navegadores às vezes lidam com conexões fechadas tentando novamente, porque o problema pode ser temporário. O fator importante é que obtivemos com sucesso um handle para uma conexão TCP!

Lembre-se de parar o programa pressionando ctrl-C quando terminar de executar uma versão específica do código. Em seguida, reinicie o programa invocando o comando `cargo run` depois de fazer cada conjunto de alterações no código para garantir que você esteja executando o código mais recente.
