# まとめ

この実験では、二次元データセットに対してさまざまな異常検出アルゴリズムを比較しました。これらのデータセットには、1つまたは2つのモード（高密度領域）が含まれており、アルゴリズムが多モーダルデータに対処する能力を示すために使用されました。アウトライア検出に使用する場合、新しいデータに適用できるpredictメソッドがないため、Local Outlier Factor（LOF）を除いて、内点と外れ点の間の決定境界が黒で表示されました。:class:`~sklearn.svm.OneClassSVM`はアウトライアに敏感であることがわかり、したがってアウトライア検出にはあまりうまくいきませんでした。:class:`sklearn.linear_model.SGDOneClassSVM`は、確率的勾配降下法（SGD）に基づくOne-Class SVMの実装でした。:class:`sklearn.covariance.EllipticEnvelope`は、データがガウス分布であると仮定し、楕円を学習しました。また、:class:`~sklearn.ensemble.IsolationForest`と:class:`~sklearn.neighbors.LocalOutlierFactor`は、多モーダルデータセットに対してかなりうまく機能するようでした。
