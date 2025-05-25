# Usando Threads para Executar Código Simultaneamente

Na maioria dos sistemas operacionais atuais, o código de um programa executado é executado em um _processo_, e o sistema operacional gerenciará múltiplos processos simultaneamente. Dentro de um programa, você também pode ter partes independentes que são executadas simultaneamente. Os recursos que executam essas partes independentes são chamados de _threads_ (threads). Por exemplo, um servidor web pode ter múltiplas threads para que possa responder a mais de uma requisição ao mesmo tempo.

Dividir a computação em seu programa em múltiplas threads para executar múltiplas tarefas ao mesmo tempo pode melhorar o desempenho, mas também adiciona complexidade. Como as threads podem ser executadas simultaneamente, não há garantia inerente sobre a ordem em que as partes do seu código em diferentes threads serão executadas. Isso pode levar a problemas, como:

- Condições de corrida (race conditions), onde as threads estão acessando dados ou recursos em uma ordem inconsistente
- Deadlocks, onde duas threads estão esperando uma pela outra, impedindo que ambas as threads continuem
- Bugs que acontecem apenas em certas situações e são difíceis de reproduzir e corrigir de forma confiável

Rust tenta mitigar os efeitos negativos do uso de threads, mas programar em um contexto multithreaded ainda exige pensamento cuidadoso e requer uma estrutura de código diferente daquela em programas executados em uma única thread.

Linguagens de programação implementam threads de algumas maneiras diferentes, e muitos sistemas operacionais fornecem uma API que a linguagem pode chamar para criar novas threads. A biblioteca padrão do Rust usa um modelo _1:1_ de implementação de thread, pelo qual um programa usa uma thread do sistema operacional por cada thread da linguagem. Existem crates que implementam outros modelos de threading que fazem diferentes trade-offs em relação ao modelo 1:1.
