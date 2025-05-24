# Visualizar um Gráfico Visual do Repositório

Como desenvolvedor, você pode precisar visualizar o histórico de um repositório para entender como o código mudou ao longo do tempo. No entanto, simplesmente visualizar uma lista de commits pode ser avassalador e difícil de entender. É aqui que o gráfico Git entra em cena. Ao visualizar o histórico de um repositório, você pode ver rapidamente como o código evoluiu e identificar quaisquer problemas ou bugs que possam ter sido introduzidos.

Para visualizar um gráfico visual de um repositório Git, você pode usar o comando `git log` com a opção `--graph`. Por exemplo, digamos que você queira visualizar o histórico do repositório `git-playground` no GitHub.

Depois de clonar o repositório, você pode navegar até o diretório e usar o comando `git log` para visualizar o gráfico:

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

Isso exibirá um gráfico visual de todos os commits e branches no repositório, permitindo que você veja como o código evoluiu ao longo do tempo.

Este é o resultado final:

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
