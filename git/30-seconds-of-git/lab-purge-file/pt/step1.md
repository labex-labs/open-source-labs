# Purgar um arquivo do histórico

Suponha que você tenha acidentalmente feito um commit de um arquivo contendo informações sensíveis, como chaves de API ou senhas, para o seu repositório Git. Você percebe que esse arquivo nunca deveria ter sido submetido e deseja removê-lo completamente do histórico do repositório. No entanto, simplesmente excluir o arquivo e fazer o commit da alteração não o removerá do histórico do repositório. O arquivo ainda estará acessível em commits anteriores, o que pode representar um risco à segurança.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta do GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Este repositório contém um arquivo chamado `file1.txt` que nunca deveria ter sido submetido. Por favor, purgue `file1.txt` do histórico do repositório, siga estes passos:

1. Clone o repositório para sua máquina local:

```shell
git clone https://github.com/your-username/git-playground
```

2. Use os seguintes comandos para navegar até o diretório e configurar a identidade:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Exclua o arquivo do índice do repositório.

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. Faça o commit desta alteração com a mensagem de commit "Remove sensitive file1.txt":

```shell
git commit -m "Remove sensitive file1.txt"
```

5. Reescreva o histórico do repositório, removendo todas as instâncias de `file1.txt`:

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. Force o push das alterações para o repositório remoto:

```shell
git push origin --force --all
```

Após concluir estas etapas, `file1.txt` será completamente removido do histórico do repositório e, após executar `git log --remotes`, você não verá o commit em `file1.txt`.
