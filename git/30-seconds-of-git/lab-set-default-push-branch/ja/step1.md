# 既定のプッシュ ブランチ名を設定する

リモート リポジトリに変更をプッシュする際、Git は現在のローカル ブランチ名をリモート ブランチの既定の名前として使用します。ただし、場合によっては、別のブランチに変更をプッシュしたい場合もあります。この場合、変更をプッシュするたびに、明示的にリモート ブランチ名を指定する必要があります。これは面倒くさく、エラーが発生しやすく、特に複数のブランチを扱っている場合にはそうです。

この実験を完了するには、GitHub アカウントから `git-playground` という Git リポジトリを使用します。これは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。既定のプッシュ ブランチ名を設定するには、以下の手順に従ってください。

1. 以下のコマンドを使用してリポジトリをクローンします。
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. リポジトリ ディレクトリに移動します。
   ```
   cd git-playground
   ```
3. 既定のプッシュ ブランチ名を現在のローカル ブランチ名に設定します。
   ```
   git config push.default current
   ```
4. 新しいブランチを作成し、そのブランチに切り替えます。
   ```
   git checkout -b my-branch
   ```
5. リポジトリにいくつかの変更を加え、コミットします。
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. 変更をリモート リポジトリにプッシュします。
   ```
   git push -u
   ```
   Git は、リモート リポジトリの `my-branch` という名前のブランチに変更をプッシュします。

これが `git log` を実行した結果です。

```shell

ADD hello.txt
```
