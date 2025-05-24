# Resumo

Renomear um _branch_ remoto no Git envolve renomear o _branch_ tanto localmente quanto no remoto. Você pode usar o comando `git branch -m <old-name> <new-name>` para renomear o _branch_ local e os comandos `git push origin --delete <old-name>` e `git push origin -u <new-name>` para deletar o antigo _branch_ remoto e definir o novo _branch_ remoto, respectivamente.
