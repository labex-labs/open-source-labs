# まとめ

この実験では、ブースティングが多クラス問題における予測精度をどのように向上させるかを検討しました。10 次元の標準正規分布を取り、ネストした同心円状の 10 次元の球体によって区切られた 3 つのクラスを定義することで構築されたデータセットを使用しました。SAMME と SAMME.R アルゴリズムの性能を比較し、各モデルのテストエラー、分類エラー、およびブースト重みをプロットしました。結果は、SAMME.R が通常 SAMME よりも速く収束し、より少ないブースティング反復でより低いテストエラーを達成することを示しています。
