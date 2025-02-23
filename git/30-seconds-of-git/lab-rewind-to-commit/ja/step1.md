# 特定のコミットに巻き戻す

開発者として、コードベースに対して行った変更を取り消す必要がある場合があります。たとえば、間違いを犯してしまい、コードの以前のバージョンに戻る必要がある場合です。このチャレンジでは、リポジトリ内の特定のコミットに巻き戻すために Git を使用します。

この実験を完了するには、`https://github.com/labex-labs/git-playground.git` の Git リポジトリ `git-playground` を使用します。このチャレンジを完了するには、次の手順に従ってください。

1. リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. リポジトリに移動します。

```shell
cd git-playground
```

3. リポジトリのコミット履歴を表示します。

```shell
git log --oneline
```

4. 巻き戻したいコミットメッセージが「Initial commit」のコミットハッシュであることを確認します。
5. `git reset <コミット>` コマンドを使用して、指定されたコミットに巻き戻します。たとえば、ハッシュ `3050fc0d3` のコミットに巻き戻したい場合：

```shell
git reset 3050fc0d3
```

6. 再度、リポジトリのコミット履歴を表示します。

```shell
git log --oneline
```

7. 変更を削除して、コードの以前のバージョンに戻したい場合は、`git reset --hard <コミット>` コマンドを使用します。たとえば、ハッシュ `c0d30f305` のコミットに変更を削除して戻したい場合：

```shell
git reset --hard c0d30f305
```

これが `git log --oneline` を実行した結果です。

```shell
c0d30f305 (HEAD -> master) Initial commit
```
