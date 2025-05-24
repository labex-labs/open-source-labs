# Resumo

Usar o Git para encontrar arquivos e commits perdidos pode ser uma tábua de salvação ao trabalhar em um projeto. Ao executar o comando `git fsck --lost-found`, você pode identificar quaisquer objetos pendentes (dangling objects) e extraí-los para o diretório `.git/lost-found`. A partir daí, você pode revisar os arquivos para determinar se são os arquivos ausentes.
