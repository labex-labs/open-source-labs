# はじめに

このチュートリアルでは、Matplotlib を使って高解像度の三角メッシュの等高線プロットを生成する方法を示します。三角メッシュの等高線は、非構造化三角メッシュ上のデータを表すために使用される手法です。データが不規則な間隔で収集される場合、またはデータが本質的に三角形状の場合によく使用されます。このチュートリアルでは、ランダムな点のセットを生成し、それらの点に対してデロネ三角分割を行い、メッシュ内の一部の三角形をマスクアウトし、データをリファインして補間し、最後に Matplotlib の`tricontour`関数を使ってリファインされたデータをプロットする方法を示します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

時々、Jupyter Notebook が読み込み終了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題に遭遇した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
