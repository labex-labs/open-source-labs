# はじめに

この実験では、指定された条件が真の間、実行を続けるループを作成するために使用される `while` キーワードについて学びます。その使い方を示すために、Rust で FizzBuzz と呼ばれるプログラムを書きます。このプログラムは `while` ループを使って 1 から 100 までの数を反復処理します。ループ内では、現在の数が 3 と 5 の両方で割り切れる（つまり 15 の倍数）場合、その場合には "fizzbuzz" を出力します。数が 3 でのみ割り切れる場合、"fizz" を出力し、5 でのみ割り切れる場合、"buzz" を出力します。それ以外のすべての数については、その数自体を出力します。カウンタ変数が 101 に達するまでループが続き、各数またはラベルを出力した後にそれをインクリメントします。

> **注：** 実験でファイル名が指定されていない場合、好きなファイル名を使用できます。たとえば、`main.rs` を使用して、`rustc main.rs &&./main` でコンパイルして実行することができます。
