# まとめ

この実験では、Spectral Co-Clustering アルゴリズムを使用してデータセットを生成し、二部クラスタリングする方法を学びました。元のデータセットは、小さな値の行列を作成し、大きな値の二部クラスタを埋め込む `make_biclusters` 関数を使用して生成されました。データセットの行と列をシャッフルし、Spectral Co-Clustering アルゴリズムに渡しました。二部クラスタのコンセンサススコアを計算し、シャッフルされたデータセットを並べ替えて、二部クラスタを連続させました。最後に、二部クラスタを可視化して、アルゴリズムがそれらをどの程度正確に見つけたかを示しました。
