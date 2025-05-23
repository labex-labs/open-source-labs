# 所有権とは？

**所有権** とは、Rust プログラムがメモリを管理する方法を規定する一連のルールです。すべてのプログラムは、実行中にコンピュータのメモリをどのように使用するかを管理する必要があります。一部の言語では、ガベージコレクションがプログラムの実行中に定期的に使用されなくなったメモリを探します。他の言語では、プログラマが明示的にメモリを割り当てて解放する必要があります。Rust は 3 番目のアプローチを採用しています。メモリは、コンパイラがチェックする一連のルールを持つ所有権システムを通じて管理されます。ルールのいずれかに違反がある場合、プログラムはコンパイルされません。所有権の機能はいずれも、プログラムが実行されている間にプログラムを遅くすることはありません。

所有権は多くのプログラマにとって新しい概念なので、少し慣れるのに時間がかかります。良い知らせは、Rust と所有権システムのルールに慣れるほど、安全で効率的なコードを自然に開発するのが簡単になるということです。がんばりましょう！

所有権を理解すると、Rust を独特なものにする機能を理解するための堅牢な基礎が得られます。この章では、非常に一般的なデータ構造である文字列に焦点を当てたいくつかの例を通じて所有権を学びます。

> **スタックとヒープ**
>
> 多くのプログラミング言語では、スタックとヒープについて頻繁に考える必要はありません。しかし、Rust のようなシステムプログラミング言語では、値がスタック上にあるかヒープ上にあるかによって、言語の動作や、特定の決定をする理由が影響されます。所有権の一部については、この章の後半でスタックとヒープとの関係で説明されますので、準備として以下に簡単な説明を行います。
>
> スタックとヒープは、実行時にコードが使用できるメモリの一部ですが、構造が異なります。スタックは、値を取得する順序で値を格納し、逆順で値を削除します。これは「後入れ先出し」と呼ばれます。皿の山を想像してみてください。皿を追加するときは、山の上に置きます。皿が必要になったときは、一番上の皿を取ります。真ん中や下から皿を追加または取り出すとうまくいきません！データを追加することを「スタックにプッシュする」と呼び、データを削除することを「スタックからポップする」と呼びます。スタックに格納されるすべてのデータは、既知の固定サイズを持たなければなりません。コンパイル時に未知のサイズまたは変更される可能性のあるサイズのデータは、代わりにヒープに格納する必要があります。
>
> ヒープはより無秩序です。ヒープにデータを置くとき、特定の量の空間を要求します。メモリ割り当てプログラムは、十分な大きさの空きスポットをヒープから見つけ、それを使用中としてマークし、その場所のアドレスである _ポインタ_ を返します。このプロセスは「ヒープ上に割り当てる」と呼ばれ、時々単に「割り当てる」と略されます（スタックに値をプッシュすることは割り当てとは見なされません）。ヒープへのポインタは既知の固定サイズなので、ポインタをスタックに格納できますが、実際のデータが必要になったときは、ポインタに従わなければなりません。レストランに着席したと想像してください。入店するとき、グループの人数を伝えます。店員は、誰もが収まる空いたテーブルを見つけ、そこに案内します。グループの誰かが遅れてきた場合、彼らはあなたがどこに着席しているか尋ねることができます。
>
> スタックにプッシュする方が、ヒープ上に割り当てるよりも高速です。なぜなら、割り当てプログラムは新しいデータを格納する場所を探す必要がないからです。その場所は常にスタックの一番上にあります。比較的に、ヒープ上に空間を割り当てるには、割り当てプログラムがまず十分な大きさの空間を見つけ、次に次の割り当ての準備をするための帳簿管理を行う必要があるため、作業が多くなります。
>
> ヒープ上のデータにアクセスするのは、スタック上のデータにアクセスするよりも遅くなります。なぜなら、そこに到達するためにポインタに従わなければならないからです。現代のプロセッサは、メモリ内でのジャンプが少ない場合に高速に動作します。この例えを続けると、レストランの店員がたくさんのテーブルから注文を受け取るときを想像してみてください。次のテーブルに移る前に、1 つのテーブルからすべての注文を受け取る方が最も効率的です。テーブル A から注文を受け取り、次にテーブル B から注文を受け取り、その後また A から注文を受け取り、そしてまた B から注文を受け取ると、はるかに遅いプロセスになります。同じように、プロセッサは、近接したデータ（スタック上のデータの場合）ではなく、離れたデータ（ヒープ上のデータの場合）で作業するときに、より良く仕事をすることができます。
>
> コードが関数を呼び出すとき、関数に渡される値（潜在的にはヒープ上のデータへのポインタも含む）と関数のローカル変数がスタックにプッシュされます。関数が終了すると、それらの値がスタックからポップされます。
>
> ヒープ上のどのコードがどのデータを使用しているかを追跡し、ヒープ上の重複データの量を最小限に抑え、ヒープ上の未使用データをクリーンアップして、空きがなくならないようにすることは、すべて所有権が解決する問題です。所有権を理解すると、スタックとヒープについて頻繁に考える必要はありませんが、所有権の主な目的がヒープデータを管理することであることを知っておくと、それがどのように機能するかを説明するのに役立ちます。
