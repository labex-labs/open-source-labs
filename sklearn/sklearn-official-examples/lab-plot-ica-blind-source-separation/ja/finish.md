# まとめ

FastICA と PCA を使って、混合信号に対してブラインドソース分離を成功裏に行いました。3 つの独立成分からなるサンプルの混合信号を生成し、ノイズを加え、データを標準化しました。その後、独立成分を混合するための混合行列を生成しました。独立成分を推定するために FastICA を使い、比較のために PCA を計算しました。最後に、元の混合信号、元の独立成分、ICA によって推定された成分、および PCA によって推定された成分をプロットしました。
