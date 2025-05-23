# はじめに

この実験では、階層的クラスタリングを使って 2 次元画像をセグメント化する方法を学びます。階層的クラスタリングは、似たようなデータポイントをグループ化するクラスタリングアルゴリズムです。画像セグメント化の文脈では、階層的クラスタリングは、似たような色の強度を持つ画素をグループ化するために使用でき、画像内の明確な領域や物体を識別するのに役立ちます。

私たちは、Python の scikit-learn ライブラリを使って、コインの画像に対して階層的クラスタリングを行います。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebook を使って練習しましょう。

時々、Jupyter Notebook が読み込み終わるまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証は自動化できません。

学習中に問題に直面した場合は、Labby にお尋ねください。セッション後にフィードバックを提供してください。私たちは迅速に問題を解決いたします。
