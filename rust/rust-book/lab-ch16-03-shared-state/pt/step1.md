# Concorrência de Estado Compartilhado (Shared-State Concurrency)

A passagem de mensagens é uma ótima maneira de lidar com a concorrência, mas não é a única. Outro método seria para múltiplos _threads_ acessarem os mesmos dados compartilhados. Considere novamente esta parte do slogan da documentação da linguagem Go: "Não se comunique compartilhando memória."

Como seria a comunicação por meio do compartilhamento de memória? Além disso, por que os entusiastas da passagem de mensagens alertariam para não usar o compartilhamento de memória?

De certa forma, os canais em qualquer linguagem de programação são semelhantes à propriedade única, porque, uma vez que você transfere um valor por um canal, você não deve mais usar esse valor. A concorrência de memória compartilhada é como a propriedade múltipla: múltiplos _threads_ podem acessar o mesmo local de memória ao mesmo tempo. Como você viu no Capítulo 15, onde os _smart pointers_ tornaram possível a propriedade múltipla, a propriedade múltipla pode adicionar complexidade porque esses diferentes proprietários precisam ser gerenciados. O sistema de tipos e as regras de propriedade do Rust ajudam muito a obter esse gerenciamento corretamente. Como exemplo, vamos analisar os _mutexes_, uma das primitivas de concorrência mais comuns para memória compartilhada.
