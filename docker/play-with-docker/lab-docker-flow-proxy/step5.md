# Bonus

We can add a Swarm visualizer service :

```bash
cat <<EOF > visualizer.yml
version: "3"

services:
  visu:
    image: dockersamples/visualizer
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    networks:
      - proxy_public
    ports:
      - 81:8080
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == manager]
      restart_policy:
        condition: on-failure

networks:
  proxy_public:
    external: true

EOF
```

#### launch the container

```bash
docker stack deploy visu --compose-file visualizer.yml
```

```bash
docker service ps visu_visu
```

> wait few second for the service to start

We can now target directly the port 81 of our swarm cluster and docker will direclty reach our Visualizer service

- [Link to Visualizer service](/){:data-term=".term1"}{:data-port="81"}

This should be something like :

![](./assets/visualizer.png)
