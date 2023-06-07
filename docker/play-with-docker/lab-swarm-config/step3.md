# Getting started

Initialize your swarm:

```bash
docker swarm init --advertise-addr $(hostname -i)
```

Let's peak the `config` options:

```bash
docker config --help
```

As you can see the API is very similar to the [docker secrets](./2017-01-23-swarm-compose-secrets.markdown). Let's create our first config object

```bash
echo "this is some crazy config stuff" | docker config create my_config -
```

As stated before, unlike secrets, you can actually see the content of the config objects directly from the CLI. Let's check this:

```bash
docker config inspect my_config
```

Wait, what?, where's my config?. Docker hides the config information by default to prevent unnecessary large outputs; in order to display
the config value the `--pretty` flag needs to added

```bash
docker config inspect --pretty my_config
```

Finally, let's deploy a service using our recently created config

```bash
docker service create --name test_cfg --config my_config alpine cat /my_config
```

You can check your service logs to see your configuration.

```bash
docker service logs test_cfg
```

As you can see, as we didn't specify any destination mountpoint, by default configs will be located at the root path. However, with configs
you can place them wherever you need.

```bash
docker service create --name test_cfg_mount --config source=my_config,target=/tmp/cfg alpine cat /tmp/cfg
```

Same as before, check your service logs to see the expected configuration:

```bash
docker service logs test_cfg_mount
```