# グレースフルシャットダウンとクリーンアップ

リスト 20-20 のコードは、意図通りにスレッドプールを使って非同期で要求に応答しています。`workers`、`id`、`thread`フィールドについて、直接使っていないことに関する警告がいくつか表示されます。これは、何もクリーンアップしていないことを思い出させます。よりエレガントではない ctrl-C メソッドを使ってメインスレッドを停止させると、他のすべてのスレッドも即座に停止します。たとえ、要求の処理の途中であってもです。

次に、`Drop`トレイトを実装して、プール内の各スレッドに`join`を呼び出します。これにより、クローズする前に処理している要求を完了させることができます。そして、スレッドに新しい要求を受け付けなくなり、シャットダウンするように伝える方法を実装します。このコードを動作させるには、サーバーを変更して、グレースフルにスレッドプールをシャットダウンする前に 2 つの要求のみを受け付けるようにします。
