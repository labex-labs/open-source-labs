# 履歴を書き換えた後のリモートブランチの更新

ローカルで履歴を書き換えると、異なる SHA-1 ハッシュで新しいコミットが作成されます。これは、ローカルブランチのコミット履歴がリモートブランチのコミット履歴と異なることを意味します。変更をリモートブランチにプッシュしようとすると、Git はコミット履歴が分岐していると見なしてプッシュを拒否します。この問題を解決するには、リモートブランチの更新を強制する必要があります。

この実験を完了するには、GitHub アカウントから `git-playground` という Git リポジトリを使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。

1. `git-playground` リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/your-username/git-playground.git
```

2. メッセージ "Added file2.txt" のコミットを、メッセージ "Update file2.txt" のコミットに更新します。

```shell
git commit --amend
```

3. ローカルブランチからの変更をリモートリポジトリにプッシュします。

```shell
git push
```

4. 正常にプッシュできない場合は、強制プッシュしてください。

```shell
git push -f origin master
```

`-f` フラグは、コミット履歴が分岐している場合でも、Git に変更でリモートブランチを更新させるよう強制します。

これが最終結果です。

```shell

```
