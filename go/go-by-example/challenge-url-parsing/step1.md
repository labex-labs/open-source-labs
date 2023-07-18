# URL Parsing

## Problem

The challenge requires parsing a sample URL that includes a scheme, authentication info, host, port, path, query params, and query fragment. The parsed URL should be used to extract the individual components of the URL.

## Requirements

- The `url` and `net` packages should be imported.
- The sample URL should be parsed and checked for errors.
- The scheme, authentication info, host, port, path, query params, and query fragment should be extracted from the parsed URL.
- The `SplitHostPort` function should be used to extract the hostname and port from the `Host` field.
- The `ParseQuery` function should be used to parse the query params into a map.

## Example

```sh
# Running our URL parsing program shows all the different
# pieces that we extracted.
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```
