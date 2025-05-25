# Usando Mutexes para Permitir Acesso aos Dados de Um Thread por Vez

_Mutex_ é uma abreviação de _exclusão mútua_ (mutual exclusion), pois um mutex permite que apenas um _thread_ acesse alguns dados em um determinado momento. Para acessar os dados em um mutex, um _thread_ deve primeiro sinalizar que deseja acesso, solicitando a aquisição do _lock_ (bloqueio) do mutex. O bloqueio é uma estrutura de dados que faz parte do mutex e que acompanha quem atualmente tem acesso exclusivo aos dados. Portanto, o mutex é descrito como _guardando_ os dados que ele contém por meio do sistema de bloqueio.

Mutexes têm a reputação de serem difíceis de usar porque você precisa se lembrar de duas regras:

1.  Você deve tentar adquirir o bloqueio antes de usar os dados.
2.  Quando você terminar com os dados que o mutex protege, você deve desbloquear os dados para que outros _threads_ possam adquirir o bloqueio.

Para uma metáfora do mundo real para um mutex, imagine uma mesa redonda em uma conferência com apenas um microfone. Antes que um painelista possa falar, ele precisa pedir ou sinalizar que deseja usar o microfone. Quando ele recebe o microfone, ele pode falar o tempo que quiser e, em seguida, entregar o microfone ao próximo painelista que solicitar para falar. Se um painelista esquecer de entregar o microfone quando terminar com ele, ninguém mais poderá falar. Se o gerenciamento do microfone compartilhado der errado, a mesa redonda não funcionará como planejado!

O gerenciamento de mutexes pode ser incrivelmente complicado de acertar, e é por isso que tantas pessoas são entusiastas de canais. No entanto, graças ao sistema de tipos e às regras de propriedade do Rust, você não pode errar o bloqueio e o desbloqueio.
