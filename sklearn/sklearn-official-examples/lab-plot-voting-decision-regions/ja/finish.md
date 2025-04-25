# まとめ

この実験では、Scikit-Learn の`VotingClassifier`を使って、2 つの特徴量に基づいてアヤメの花のクラスを予測しました。3 つの分類器を学習しました：`DecisionTreeClassifier`、`KNeighborsClassifier`、および`SVC`。その後、`VotingClassifier`を使ってそれらの予測を組み合わせ、決定境界を描画しました。`VotingClassifier`の決定境界は`SVC`の決定境界に似ていることがわかりましたが、一部の領域では複雑さが少ないです。
