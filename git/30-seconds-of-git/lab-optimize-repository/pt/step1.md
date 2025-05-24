# Otimizar o Repositório Local

Com o tempo, seu repositório Git pode ficar desorganizado com versões antigas de arquivos e outros dados desnecessários. Isso pode lentificar o Git e dificultar o trabalho com seu repositório. Para otimizar seu repositório local, você precisa remover esses dados desnecessários. Isso pode ser feito usando o comando `git gc`.

O comando `git gc` significa "Git garbage collector" (coletor de lixo do Git). Ele é usado para limpar dados desnecessários em seu repositório. Quando você executa `git gc`, o Git removerá quaisquer objetos soltos (objetos que não são referenciados por nenhum branch ou tag) e empacotará os objetos restantes em um novo conjunto de arquivos de pacote (pack files). Isso pode reduzir significativamente o tamanho do seu repositório e melhorar o desempenho do Git.

Para otimizar o repositório local, você pode usar o comando `git gc` com as opções `--prune=now` e `--aggressive`. Por exemplo, digamos que você tenha um repositório Git chamado `git-playground` localizado em seu diretório home. Para otimizar este repositório, você executaria o seguinte comando:

```shell
cd git-playground
git gc --prune=now --aggressive
```

Este é o resultado da otimização do repositório `git-playground` removendo todos os objetos soltos e empacotando os objetos restantes em um novo conjunto de arquivos de pacote:

![Resultado da otimização do repositório Git](../assets/challenge-optimize-repository-step1-1.png)
