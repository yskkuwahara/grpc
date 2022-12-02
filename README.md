# grpc

## Python Server

Preparation.
```bash
$ pip3 install grpcio grpcio-tools
```

Install packages.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/user.proto
```
