# Uma Análise Mais Detalhada de uma Requisição HTTP

HTTP é um protocolo baseado em texto, e uma requisição tem este formato:

    Método Request-URI HTTP-Version CRLF
    headers CRLF
    message-body

A primeira linha é a _linha de requisição_ que contém informações sobre o que o cliente está solicitando. A primeira parte da linha de requisição indica o _método_ que está sendo usado, como `GET` ou `POST`, que descreve como o cliente está fazendo esta requisição. Nosso cliente usou uma requisição `GET`, o que significa que está pedindo informações.

A próxima parte da linha de requisição é _/_, que indica o _identificador uniforme de recurso_ _(URI)_ que o cliente está solicitando: um URI é quase, mas não exatamente, o mesmo que um _localizador uniforme de recurso_ _(URL)_. A diferença entre URIs e URLs não é importante para nossos propósitos neste capítulo, mas a especificação HTTP usa o termo _URI_, então podemos apenas substituir mentalmente _URL_ por _URI_ aqui.

A última parte é a versão HTTP que o cliente usa, e então a linha de requisição termina em uma sequência CRLF. (CRLF significa _retorno de carro_ e _avanço de linha_, que são termos dos tempos da máquina de escrever!) A sequência CRLF também pode ser escrita como `\r\n`, onde `\r` é um retorno de carro e `\n` é um avanço de linha. A _sequência CRLF_ separa a linha de requisição do restante dos dados da requisição. Observe que, quando o CRLF é impresso, vemos o início de uma nova linha em vez de `\r\n`.

Olhando para os dados da linha de requisição que recebemos ao executar nosso programa até agora, vemos que `GET` é o método, _/_ é o URI da requisição e `HTTP/1.1` é a versão.

Após a linha de requisição, as linhas restantes, começando por `Host:`, são cabeçalhos (headers). Requisições `GET` não têm corpo.

Tente fazer uma requisição de um navegador diferente ou solicitar um endereço diferente, como _127.0.0.1:7878/test_, para ver como os dados da requisição mudam.

Agora que sabemos o que o navegador está pedindo, vamos enviar alguns dados de volta!
