# まとめ

Git を使用する際、ローカルの `master` ブランチをリモートのブランチに合わせることは一般的なタスクです。このチャレンジで示されている手順に従うことで、ローカルブランチがリモートブランチと最新状態に保たれていることを確認できます。リモートから最新の更新を取得するには `git fetch origin` を、`master` ブランチに切り替えるには `git checkout master` を、ローカルの `master` ブランチをリモートのブランチに合わせるには `git reset --hard origin/master` を使用することを忘れないでください。
