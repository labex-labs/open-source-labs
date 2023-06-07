# Generating the SSL Certificate in Linux

The Docker docs explain how to [generate a self-signed certificate](https://docs.docker.com/registry/insecure/#/using-self-signed-certificates) on Linux using OpenSSL:

```bash
mkdir -p certs
openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt
```

```
Generating a 4096 bit RSA private key
........++
............................................................++
writing new private key to 'certs/domain.key'