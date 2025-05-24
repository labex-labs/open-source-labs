# 워커 풀 (Worker Pools)

`jobs` 채널에서 작업을 수신하고 `results` 채널에서 해당 결과를 전송하는 워커 풀을 구현합니다. 워커 풀은 여러 개의 동시 인스턴스를 가져야 하며, 각 워커는 비용이 많이 드는 작업을 시뮬레이션하기 위해 작업당 1 초 동안 대기해야 합니다.

- 고루틴 (goroutine) 과 채널 (channel) 을 사용하여 워커 풀을 구현합니다.
- 워커 풀은 여러 개의 동시 인스턴스를 가져야 합니다.
- 각 워커는 비용이 많이 드는 작업을 시뮬레이션하기 위해 작업당 1 초 동안 대기해야 합니다.
- 워커 풀은 `jobs` 채널에서 작업을 수신하고 `results` 채널에서 해당 결과를 전송해야 합니다.

```sh
# 실행 중인 프로그램은 5 개의 작업이
# 다양한 워커에 의해 실행되는 것을 보여줍니다.
# 프로그램은 총 5 초의 작업을 수행하지만
# 3 개의 워커가 동시에 작동하기 때문에 약 2 초가 걸립니다.
$ time go run worker-pools.go
worker 1 started job 1
worker 2 started job 2
worker 3 started job 3
worker 1 finished job 1
worker 1 started job 4
worker 2 finished job 2
worker 2 started job 5
worker 3 finished job 3
worker 1 finished job 4
worker 2 finished job 5

real 0m2.358s
```

전체 코드는 다음과 같습니다.

```go
// 이 예제에서는 고루틴 (goroutine) 과 채널 (channel) 을 사용하여
// _워커 풀 (worker pool)_을 구현하는 방법을 살펴보겠습니다.

package main

import (
	"fmt"
	"time"
)

// 여기는 워커입니다. 여러 개의
// 동시 인스턴스를 실행할 것입니다. 이 워커는
// `jobs` 채널에서 작업을 수신하고 해당
// 결과를 `results` 채널로 보냅니다.
// 비용이 많이 드는 작업을 시뮬레이션하기 위해
// 작업당 1 초 동안 대기합니다.
func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "started  job", j)
		time.Sleep(time.Second)
		fmt.Println("worker", id, "finished job", j)
		results <- j * 2
	}
}

func main() {

	// 워커 풀을 사용하려면
	// 작업을 보내고 결과를 수집해야 합니다.
	// 이를 위해 2 개의 채널을 만듭니다.
	const numJobs = 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)

	// 여기서는 3 개의 워커를 시작합니다.
	// 아직 작업이 없으므로 초기에는 차단됩니다.
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// 여기서는 5 개의 `jobs` 를 보내고
	// 해당 채널을 `close` 하여 모든 작업을
	// 완료했음을 나타냅니다.
	for j := 1; j <= numJobs; j++ {
		jobs <- j
	}
	close(jobs)

	// 마지막으로 모든 작업의 결과를 수집합니다.
	// 이것은 또한 워커 고루틴이
	// 완료되었는지 확인합니다. 여러
	// 고루틴을 기다리는 다른 방법은 [WaitGroup](waitgroups) 을 사용하는 것입니다.
	for a := 1; a <= numJobs; a++ {
		<-results
	}
}
```
