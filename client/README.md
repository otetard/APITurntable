# Installation
## Bare installation 
Bare installation needs `go` installed on the host

```bash 
go install ./...
```


## Docker installation
Docker installation needs `docker` installed on the host
```bash 
make build
```

# Running the client
## Env variable used in this CLI command
- VERBOSE (bool): define the verbosity leve of the application 
- SERVER_ADDRESS (string): address of the main apiturntable server 
- DESTINATION_SERVICE_URL (string): address of the service to send request to (ex: mattermost, bell, etc.)

Authentication is not used yet. 

for bare installation, just run `turnt collect` command to launch the client.
it connects to the `SERVER_ADDRESS` URL and retrieve requests in SSE mode. 


## Run with bare installation 

```bash
export SERVER_ADDRESS=https://apiturntables.io
export DESTINATION_SERVICE_URL=http://mattermost.entreprise.com/hooks/123456789
turnt
```

## Run with docker installation 

```bash
docker run \
    --rm -it \
    -e SERVER_ADDRESS=https://apiturntables.io \
    -e DESTINATION_SERVICE_URL=http://mattermost.entreprise.com/hooks/123456789 \
    turnt 
```