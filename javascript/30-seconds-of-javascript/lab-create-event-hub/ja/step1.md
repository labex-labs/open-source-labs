# イベントハブの作成

`emit`、`on`、および `off` メソッドを持つイベントハブを作成するには、次の手順に従います。

1. `Object.create(null)` を使用して、`Object.prototype` からプロパティを継承しない空の `hub` オブジェクトを作成します。
2. `emit` の場合、`event` 引数に基づいてハンドラの配列を解決し、次に `Array.prototype.forEach()` を使用して各ハンドラをデータを引数として渡して実行します。
3. `on` の場合、イベント用の配列がまだ存在しない場合は作成し、次に `Array.prototype.push()` を使用してハンドラを配列に追加します。
4. `off` の場合、`Array.prototype.findIndex()` を使用してイベント配列内のハンドラのインデックスを見つけ、`Array.prototype.splice()` を使用して削除します。

以下がコードです。

```js
const createEventHub = () => ({
  hub: Object.create(null),
  emit(event, data) {
    (this.hub[event] || []).forEach((handler) => handler(data));
  },
  on(event, handler) {
    if (!this.hub[event]) this.hub[event] = [];
    this.hub[event].push(handler);
  },
  off(event, handler) {
    const i = (this.hub[event] || []).findIndex((h) => h === handler);
    if (i > -1) this.hub[event].splice(i, 1);
    if (this.hub[event].length === 0) delete this.hub[event];
  }
});
```

イベントハブを使用するには：

1. `on()` を使用して異なる種類のイベントをリッスンすることでイベントを購読します。
2. `emit()` を使用してデータを引数として渡して、それらに購読されているすべてのハンドラを呼び出すイベントを発行します。
3. `off()` を使用して特定のハンドラがイベントをリッスンしなくなるようにイベントの購読解除を行います。

以下は例です。

```js
const handler = (data) => console.log(data);
const hub = createEventHub();
let increment = 0;

// 購読: 異なる種類のイベントをリッスンする
hub.on("message", handler);
hub.on("message", () => console.log("Message event fired"));
hub.on("increment", () => increment++);

// 発行: それらに購読されているすべてのハンドラを呼び出すイベントを発行し、データを引数として渡す
hub.emit("message", "hello world"); // 'hello world' と 'Message event fired' がログに表示されます
hub.emit("message", { hello: "world" }); // オブジェクトと 'Message event fired' がログに表示されます
hub.emit("increment"); // `increment` 変数は現在 1 になります

// 購読解除: 'message' イベントをリッスンしている特定のハンドラを停止する
hub.off("message", handler);
```
