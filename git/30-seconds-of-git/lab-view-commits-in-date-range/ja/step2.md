# 基本的な `git log` コマンドの調査

リポジトリをクローンしたので、`git log` コマンドを使ってコミット履歴を表示する方法を学んでみましょう。

`git log` コマンドは、リポジトリ内のすべてのコミットのリストを表示します。最新のコミットから始まります。各コミットエントリには以下が含まれます。

- 一意のコミットハッシュ (識別子)
- 作者情報
- コミットの日付と時刻
- コミットメッセージ

基本的なコミット履歴を表示してみましょう。

```bash
git log
```

以下のような出力が表示されるはずです。

```
commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

出力が長い場合、以下の操作で移動できます。

- `Space` キーを押すと次に進みます。
- `b` キーを押すと前に戻ります。
- `q` キーを押すとログ表示を終了します。

各コミットには一意の識別子 (長い 16 進数の文字列)、作者情報、コミットの日付と時刻、および行われた変更を説明するメッセージがあることに注意してください。
