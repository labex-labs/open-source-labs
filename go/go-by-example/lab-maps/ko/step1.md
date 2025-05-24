# 맵 (Maps)

이 랩에서는 주어진 문자열에서 각 단어가 나타나는 횟수를 저장하는 맵을 생성해야 합니다. 문자열을 단어로 분할한 다음, 각 단어를 반복하면서 맵에 아직 존재하지 않으면 추가하고, 이미 존재하면 카운트를 증가시켜야 합니다.

- 단어 카운트를 저장하기 위해 맵을 사용해야 합니다.
- 입력 문자열을 단어로 분할해야 합니다.
- 입력 문자열의 각 단어를 반복해야 합니다.
- 맵에 아직 존재하지 않는 경우 각 단어를 맵에 추가하거나, 이미 존재하는 경우 카운트를 증가시켜야 합니다.

```sh
# Note that maps appear in the form `map[k:v k:v]` when
# printed with `fmt.Println`.
$ go run maps.go
map: map[k1:7 k2:13]
v1: 7
v3: 0
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

전체 코드는 다음과 같습니다.

```go
// _Maps_ are Go's built-in [associative data type](https://en.wikipedia.org/wiki/Associative_array)
// (sometimes called _hashes_ or _dicts_ in other languages).

package main

import "fmt"

func main() {

	// To create an empty map, use the builtin `make`:
	// `make(map[key-type]val-type)`.
	m := make(map[string]int)

	// Set key/value pairs using typical `name[key] = val`
	// syntax.
	m["k1"] = 7
	m["k2"] = 13

	// Printing a map with e.g. `fmt.Println` will show all of
	// its key/value pairs.
	fmt.Println("map:", m)

	// Get a value for a key with `name[key]`.
	v1 := m["k1"]
	fmt.Println("v1:", v1)

	// If the key doesn't exist, the
	// [zero value](https://go.dev/ref/spec#The_zero_value) of the
	// value type is returned.
	v3 := m["k3"]
	fmt.Println("v3:", v3)

	// The builtin `len` returns the number of key/value
	// pairs when called on a map.
	fmt.Println("len:", len(m))

	// The builtin `delete` removes key/value pairs from
	// a map.
	delete(m, "k2")
	fmt.Println("map:", m)

	// The optional second return value when getting a
	// value from a map indicates if the key was present
	// in the map. This can be used to disambiguate
	// between missing keys and keys with zero values
	// like `0` or `""`. Here we didn't need the value
	// itself, so we ignored it with the _blank identifier_
	// `_`.
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// You can also declare and initialize a new map in
	// the same line with this syntax.
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}
```
