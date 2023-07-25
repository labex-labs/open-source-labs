# Testing the Registry Image

First we'll test that the registry image is working correctly, by running it without any special configuration:

```bash
docker run -d -p 5000:5000 --name registry registry:2
```
