# 欠落しているサブモジュールをクローンする

あなたはサブモジュールを含むプロジェクトを作業しています。プロジェクトをクローンするとき、サブモジュールは自動的にクローンされません。これは、プロジェクトをビルドまたは実行しようとするときに問題を引き起こします。あなたは欠落しているサブモジュールをクローンし、正しいコミットをチェックアウトする必要があります。

この実験では、`https://github.com/git/git` という名前の Git リポジトリを使用します。このリポジトリには、リポジトリをクローンする際に自動的にクローンされないサブモジュールが含まれています。

欠落しているサブモジュールをクローンし、正しいコミットをチェックアウトするには、次の手順に従います。

1. リポジトリディレクトリに移動します。
   ```
   cd git
   ```
2. サブモジュールを初期化します。
   ```
   git submodule update --init --recursive
   ```
3. サブモジュールの正しいコミット、つまり `master` ブランチにチェックアウトします。
   ```
   git submodule foreach git checkout master
   ```
   以下が最終結果です。

```shell
Submodule 'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
