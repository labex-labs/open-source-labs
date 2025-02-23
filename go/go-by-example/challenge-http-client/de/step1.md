# HTTP-Client

Sie müssen ein Programm schreiben, das einen HTTP GET-Anfrage an einen Server sendet und den HTTP-Antwortstatus sowie die ersten 5 Zeilen des Antwortkörpers ausgibt.

## Anforderungen

- Das Programm sollte das `net/http`-Paket verwenden, um eine HTTP GET-Anfrage zu senden.
- Das Programm sollte den HTTP-Antwortstatus ausgeben.
- Das Programm sollte die ersten 5 Zeilen des Antwortkörpers ausgeben.
- Das Programm sollte Fehler优雅地 (gracefully) behandeln.

## Beispiel

```sh
$ go run http-clients.go
Antwortstatus: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
