FROM golang:1.9-alpine as builder

ENV path /go/src/github.com/gbossert/APITurntable/client

RUN mkdir -p ${path} && \
    apk update && apk add git 
COPY . ${path}

RUN cd ${path} && \
    go get -v ./... && \
    go install ./...

FROM alpine:3.7

COPY --from=builder /go/bin/turnt /turnt

CMD ["/turnt", "collect"]
