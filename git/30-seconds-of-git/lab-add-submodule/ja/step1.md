# サブモジュールを追加する

あなたのタスクは、Git リポジトリに新しいサブモジュールを追加することです。上流のリポジトリからのサブモジュールを、あなたのリポジトリ内のローカルディレクトリに追加するには、`git submodule add` コマンドを使用する必要があります。このコマンドの構文は以下の通りです。

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` は、サブモジュールとして追加したい上流のリポジトリの URL またはパスです。
- `<local-path>` は、サブモジュールをローカルリポジトリに保存したい場所のパスです。

`my-project` という名前の Git リポジトリがあり、`https://github.com/labex-labs/git-playground.git` という Git リポジトリからのサブモジュールを、ローカルリポジトリ内の `git-playground` というディレクトリに追加したい場合があります。以下がその方法です。

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git./git-playground
```

この実験を完了した後の結果は次の通りです。

![Git サブモジュール追加結果](../assets/challenge-add-submodule-step1-1.png)
