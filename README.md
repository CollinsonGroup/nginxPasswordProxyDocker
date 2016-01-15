# nginx Password Proxy

A simple proxy using nginx that will ask for a username and password before passing through to a supplied address.

## Building the Container

Checkout the code and build as normal:

```bash
> docker build -t collinsongroup/nginxpasswordproxy .
```

## Running the Container

The container accepts environment variables to controls it's behavior:

| Variable             | Usage                             | Default                 |
|----------------------|-----------------------------------|-------------------------|
| PASSTHRU_DESTINATION | URL to passthrough to             | http://localhost:8080   |
| PASSTHRU_USERNAME    | Username for the passthrough      | guest                   |
| PASSTHRU_PASSWORD    | Password for the passthrough user | guest                   |

These can be passed in to the Docker **run** command:

```bash
> docker run -d -e PASSTHRU_DESTINATION=http://my.new.service:9090 collinsongroup/nginxpasswordproxy
```
