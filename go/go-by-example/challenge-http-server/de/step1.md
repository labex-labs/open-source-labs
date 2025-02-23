# HTTP-Server

Sie müssen einen einfachen HTTP-Server schreiben, der zwei Routen verarbeiten kann: `/hello` und `/headers`. Die `/hello`-Route sollte eine einfache "hello"-Antwort zurückgeben, während die `/headers`-Route alle HTTP-Anfrageheader zurückgeben sollte.

## Anforderungen

- Der Server sollte das Paket `net/http` verwenden.
- Die `/hello`-Route sollte eine "hello"-Antwort zurückgeben.
- Die `/headers`-Route sollte alle HTTP-Anfrageheader zurückgeben.
- Der Server sollte auf Port `8090` lauschen.

## Beispiel

```sh
# Führen Sie den Server im Hintergrund aus.
$ go run http-servers.go &

# Greifen Sie auf die `/hello`-Route zu.
$ curl localhost:8090/hello
hello
```
