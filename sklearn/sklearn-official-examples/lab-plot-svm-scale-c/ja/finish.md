# まとめ

この実験では、L1およびL2ペナルティの両方に対して、SVMにおける正則化パラメータをスケーリングする効果を示しました。L1ペナルティの場合、サンプル数で `C` をスケーリングするとき、交差検証誤差がテスト誤差と最も相関することが観察されました。L2ペナルティの場合、最良の結果は `C` をスケーリングしない場合から得られます。
