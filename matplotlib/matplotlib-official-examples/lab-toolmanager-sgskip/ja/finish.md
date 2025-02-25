# まとめ

このチュートリアルでは、`matplotlib.backend_managers.ToolManager` を使用して Toolbar を変更し、カスタム ツールを作成し、ツールを追加し、削除する方法を学びました。`ToolManager` によって制御されるすべてのツールを一覧表示する `ListTools` という名前のカスタム ツールを作成しました。また、指定された `gid` を持つプロット上のすべての線の表示を、ツールが有効または無効になっているかどうかに応じて True または False に設定する `GroupHideTool` という名前のカスタム ツールも作成しました。最後に、カスタム ツールを `ToolManager` に追加し、`Toolbar` に `Show` ツールを追加し、`Toolbar` から `forward` ボタンを削除しました。
