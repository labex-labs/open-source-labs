# Creating services

The next step is to create a service and list out the services. This creates a single service called `web` that runs the latest nginx, type the below commands in the first terminal:

```bash
docker service create -p 80:80 --name web nginx:latest
docker service ls
```

You can check that nginx is running by executing the following command:

```bash
curl http://localhost:80
```
