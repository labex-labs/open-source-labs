# まとめ

この実験では、2 つの手法である `FeatureHasher` と `DictVectorizer`、および 4 つの特殊用途のテキストベクトル化手法である `CountVectorizer`、`HashingVectorizer`、および `TfidfVectorizer` を比較することで、テキストベクトル化を検討しました。ベクトル化手法をベンチマークし、結果をプロットしました。その結果、`HashingVectorizer` はハッシュ衝突による変換の逆変換可能性を犠牲にして、`CountVectorizer` よりも良好な性能を示すことがわかりました。また、`DictVectorizer` と `FeatureHasher` は、手動でトークン化されたドキュメントに対して、同等のテキストベクトル化手法よりも良好な性能を示します。なぜなら、前者のベクトル化手法の内部トークン化ステップは、一度正規表現をコンパイルしてから、すべてのドキュメントで再利用するためです。
