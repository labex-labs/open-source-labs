# 自動テストの紹介

## 自動テストとは？

テストは、コードの動作を確認するためのルーチンです。

テストはさまざまなレベルで行われます。一部のテストは非常に細かい部分に適用されます（特定のモデルメソッドが期待通りの値を返すか？）一方、他のテストはソフトウェアの全体的な動作を調べます（サイト上の一連のユーザー入力が期待される結果を生成するか？）。これは、「**データベースのセットアップ**」で行ったテストと同じではありません。そこでは、`shell` を使ってメソッドの動作を調べたり、アプリケーションを実行してデータを入力してその動作を確認したりしていました。

自動テストの違いは、テスト作業がシステムによって行われるところにあります。一度テストセットを作成すると、アプリケーションを変更するたびに、コードが元の意図通りに動作しているかどうかを確認できます。手作業での時間がかかるテストを行う必要はありません。

## なぜテストを作成する必要があるのか

では、なぜテストを作成する必要があり、なぜ今すぐか？

Python / Django を学ぶだけでも十分忙しいと感じるかもしれません。さらに学ぶことやすることがあると、圧倒的で不必要に感じるかもしれません。結局のところ、私たちの投票アプリケーションは今十分に機能しています。自動テストを作成する手間をかけても、それがもっと良く機能することはありません。もし投票アプリケーションの作成があなたが最後に行う Django プログラミングであるなら、確かに、自動テストを作成する方法を知る必要はありません。しかし、そうでない場合、今が学ぶのに最適な時期です。

### テストは時間を節約します

ある程度までは、「動作しているように見えることを確認する」ことが十分なテストになります。より洗練されたアプリケーションでは、コンポーネント間に数十の複雑な相互作用があるかもしれません。

それらのコンポーネントのいずれかが変更されると、アプリケーションの動作に予期しない結果が生じる可能性があります。「まだ動作しているように見える」ことを確認するには、テストデータの 20 通りの異なるバリエーションでコードの機能を実行して、何かが壊れていないことを確認する必要があります。これは時間の無駄です。

自動テストがこれを数秒で行ってくれる場合、特にそうです。何かが間違っている場合、テストは予期しない動作の原因となっているコードの特定にも役立ちます。

時々、生産的で創造的なプログラミング作業から離れて、テストを書く退屈で面白くない作業に直面するのは苦労に感じるかもしれません。特にコードが正常に動作していることを知っているときです。

しかし、テストを書く作業は、手動でアプリケーションをテストしたり、新しく導入された問題の原因を特定したりするのに何時間も費やすよりもはるかに充実感があります。

### テストは問題を特定するだけでなく、防止します

テストを単に開発の否定的な側面と考えるのは間違いです。

テストがない場合、アプリケーションの目的や意図された動作はかなり不明瞭になります。自分自身のコードであっても、時々、それが何をしているのかを調べるために中を探り回ることになります。

テストはそれを変えます。それは内部からコードを照らしてくれます。何かが間違っているとき、それは間違っている部分に光を当てます。それが間違っていることに気づいていなくてもです。

### テストはコードを魅力的にします

素晴らしいソフトウェアを作成したかもしれませんが、多くの開発者がテストがないために見てもらえないことに気づくでしょう。テストがなければ、彼らはそれを信頼しません。Django の元の開発者の 1 人である Jacob Kaplan-Moss は、「テストのないコードは、設計上、破損している」と言っています。

他の開発者があなたのソフトウェアを真剣に受け取る前にテストを見たいと望むのは、あなたがテストを書き始めるもう 1 つの理由です。

### テストはチームが一緒に働くのを助けます

前述のポイントは、単独の開発者がアプリケーションを保守するという観点から書かれています。複雑なアプリケーションはチームによって保守されます。テストは、同僚が不注意にあなたのコードを破壊しないこと（そしてあなたが彼らのコードを知らずに破壊しないこと）を保証します。Django プログラマーとして生きていくためには、テストを書くことが上手でなければなりません！
