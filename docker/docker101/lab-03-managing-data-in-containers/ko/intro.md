# 소개

기본적으로 컨테이너 내에서 생성된 모든 파일은 쓰기 가능한 컨테이너 레이어에 저장됩니다. 이는 다음을 의미합니다.

- 컨테이너가 더 이상 존재하지 않으면 데이터가 손실됩니다.
- 컨테이너의 쓰기 가능한 레이어는 호스트 머신에 긴밀하게 연결되어 있습니다.
- 파일 시스템을 관리하려면 Linux 커널을 사용하여 유니온 파일 시스템을 제공하는 스토리지 드라이버가 필요합니다. 이 추가적인 추상화는 파일 시스템에 직접 쓰는 `data volumes`에 비해 성능을 저하시킵니다.

Docker 는 호스트 머신에 파일을 저장하기 위한 두 가지 옵션, `volumes`와 `bind mounts`를 제공합니다. Linux 에서 Docker 를 실행하는 경우 `tmpfs mount`를 사용할 수도 있으며, Windows 에서 Docker 를 실행하는 경우 `named pipe`를 사용할 수도 있습니다.

![Types of Mounts](../assets/types-of-mounts.png)

- `Volumes`는 Docker 가 관리하는 호스트 파일 시스템에 저장됩니다.
- `Bind mounts`는 호스트 시스템의 어느 곳에나 저장됩니다.
- `tmpfs mounts`는 호스트 메모리에만 저장됩니다.

원래, `--mount` 플래그는 Docker Swarm 서비스에 사용되었고, `--volume` 플래그는 독립 실행형 컨테이너에 사용되었습니다. Docker 17.06 이상부터는 독립 실행형 컨테이너에도 `--mount`를 사용할 수 있으며, 일반적으로 `--volume`보다 더 명시적이고 자세합니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">100.00%</span>입니다.
</div>
