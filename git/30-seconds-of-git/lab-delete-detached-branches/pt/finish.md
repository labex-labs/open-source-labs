# Resumo

Deletar branches detached (desanexados) é um passo importante para manter seu repositório Git organizado e fácil de gerenciar. Ao usar o comando `git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D`, você pode remover facilmente todos os branches detached do seu repositório local. Isso ajudará você a manter seu repositório limpo e facilitará o trabalho no futuro.
