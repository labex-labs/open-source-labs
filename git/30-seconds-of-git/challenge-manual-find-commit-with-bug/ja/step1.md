# 手動でバグを引き起こしたコミットを見つける

あなたのタスクは、`git-playground` リポジトリでバグを引き起こしたコミットを手動で見つけることです。このリポジトリは `https://github.com/labex-labs/git-playground` にあります。

このチャレンジを完了するには、リポジトリのコミット履歴を二分探索する必要があります。バグを引き起こしたコミットを絞り込むまで、コミットを「正常」（バグのない）または「不良」（バグのある）とマークする必要があります。

## タスク

エラーメッセージは、`file2.txt` ファイルが "This is file2." ではなく "This is file2.txt." を表示する必要があるというものです。

1. リポジトリディレクトリに移動します。
2. 二分探索を開始します。
3. 現在のコミットを「不良」とマークします。
4. メッセージが "Initial commit" のコミットを「正常」とマークします。Git は自動的に新しいコミットをチェックアウトしてテストします。
5. チェックされた `file2.txt` ファイルの内容がバグと一致しない場合、それを「正常」とマークします。
6. チェックされた `file2.txt` ファイルの内容がバグと一致する場合、それを「不良」とマークします。
7. バグのあるコミットを見つけたら、二分探索を終了します。

これで、バグのあるコミットのコード変更を調べて、バグの原因を見つけることができます。

これがテストの結果です：

```
d22f46ba8c2d4e07d773c5126e9c803933eb5898 は最初の不良コミットです
コミット d22f46ba8c2d4e07d773c5126e9c803933eb5898
著者: Hang <huhuhang@users.noreply.github.com>
日付:  Wed Apr 26 14:16:25 2023 +0800

    file2.txt を追加

 file2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt
```
