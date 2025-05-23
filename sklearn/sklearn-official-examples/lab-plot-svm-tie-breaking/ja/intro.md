# はじめに

この実験では、SVM のバイアス解消とその決定境界への影響について説明します。SVM において、バイアス解消は、2 つ以上のクラスの距離が等しい場合に、それらの間の衝突を解消するために使用されるメカニズムです。`decision_function_shape='ovr'`の場合、デフォルトでは有効になっておらず、コストがかかるためです。したがって、この実験では、多クラス分類問題と`decision_function_shape='ovr'`に対する`break_ties`パラメータの影響を示します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

時々、Jupyter Notebook が読み込み完了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証は自動化できません。

学習中に問題に直面した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
