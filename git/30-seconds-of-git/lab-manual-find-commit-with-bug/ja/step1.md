# 手動でバグを引き起こしたコミットを見つける

あなたのタスクは、`git-playground` リポジトリでバグを引き起こしたコミットを手動で見つけることです。このリポジトリは `https://github.com/labex-labs/git-playground` にあります。バグは、`file2.txt` ファイルが "This is file2." ではなく "This is file2.txt." を表示する必要があるということです。

この実験を完了するには、`git bisect` コマンドを使用して、リポジトリのコミット履歴を二分探索する必要があります。バグを引き起こしたコミットを絞り込むまで、コミットを「正常」（バグのない）または「不良」（バグのある）としてマークする必要があります。

1. リポジトリディレクトリに移動します。

```
cd git-playground
```

2. `git bisect` プロセスを開始します。

```
git bisect start
```

3. 現在のコミットを「不良」としてマークします。

```
git bisect bad HEAD
```

4. メッセージ "Initial commit" のコミットを「正常」としてマークします。Git は自動的に新しいコミットをチェックアウトしてテストします。

```
git bisect good 3050fc0de
```

Git は自動的に新しいコミットをチェックアウトしてテストします。5. チェックアウトされた `file2.txt` ファイルの内容がバグと一致しない場合は、「正常」としてマークします。

```
cat file2.txt
git bisect good
```

6. チェックアウトされた `file2.txt` ファイルの内容がバグと一致する場合は、「不良」としてマークします。

```
git bisect bad
```

7. バグのあるコミットを見つけたら、`git bisect` プロセスをリセットします。

```
git bisect reset
```

これで、バグのあるコミットのコード変更を調べて、バグの原因を見つけることができます。

これがテストの結果です。

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 は最初の不良コミットです
コミット d22f46ba8c2d4e07d773c5126e9c803933eb5898
著者: Hang <huhuhang@users.noreply.github.com>
日付:  2023年4月26日 水曜日 14:16:25 +0800

    file2.txt を追加

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
