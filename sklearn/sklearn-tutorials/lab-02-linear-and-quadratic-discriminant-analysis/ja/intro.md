# はじめに

線形判別分析 (Linear Discriminant Analysis, LDA) と二次判別分析 (Quadratic Discriminant Analysis, QDA) は、機械学習で使用される 2 つの古典的な分類器です。LDA は線形の決定面を使用し、QDA は二次の決定面を使用します。これらの分類器は、閉形式の解があり、実際の運用でも良好な結果を得られ、調整するハイパーパラメータがないため、人気があります。

この実験では、Python で人気のある機械学習ライブラリである scikit-learn を使用して、LDA と QDA を実行する方法を探ります。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **Notebook** タブに切り替え、Jupyter Notebook にアクセスして練習を行ってください。

場合によっては、Jupyter Notebook の読み込みが完了するまで数秒待つ必要があることがあります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題が発生した場合は、Labby に質問してください。セッション終了後にフィードバックを提供していただければ、迅速に問題を解決します。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">80.49%</span>です。
</div>
