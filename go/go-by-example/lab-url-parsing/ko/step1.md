# URL 파싱

이 랩에서는 스키마, 인증 정보, 호스트, 포트, 경로, 쿼리 매개변수 및 쿼리 프래그먼트를 포함하는 샘플 URL 을 파싱해야 합니다. 파싱된 URL 은 URL 의 개별 구성 요소를 추출하는 데 사용해야 합니다.

- `url` 및 `net` 패키지를 임포트해야 합니다.
- 샘플 URL 을 파싱하고 오류를 확인해야 합니다.
- 스키마, 인증 정보, 호스트, 포트, 경로, 쿼리 매개변수 및 쿼리 프래그먼트를 파싱된 URL 에서 추출해야 합니다.
- `SplitHostPort` 함수를 사용하여 `Host` 필드에서 호스트 이름과 포트를 추출해야 합니다.
- `ParseQuery` 함수를 사용하여 쿼리 매개변수를 맵으로 파싱해야 합니다.

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

전체 코드는 다음과 같습니다.

```go
// URLs provide a [uniform way to locate resources](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/).
// Here's how to parse URLs in Go.

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// We'll parse this example URL, which includes a
	// scheme, authentication info, host, port, path,
	// query params, and query fragment.
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// Parse the URL and ensure there are no errors.
	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	// Accessing the scheme is straightforward.
	fmt.Println(u.Scheme)

	// `User` contains all authentication info; call
	// `Username` and `Password` on this for individual
	// values.
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// The `Host` contains both the hostname and the port,
	// if present. Use `SplitHostPort` to extract them.
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// Here we extract the `path` and the fragment after
	// the `#`.
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// To get query params in a string of `k=v` format,
	// use `RawQuery`. You can also parse query params
	// into a map. The parsed query param maps are from
	// strings to slices of strings, so index into `[0]`
	// if you only want the first value.
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}
```
