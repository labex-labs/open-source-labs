# Init your swarm

```bash
docker swarm init --advertise-addr $(hostname -i)
```

Copy the join command (_watch out for newlines_) output and paste it in the other terminal.
