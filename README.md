# grpc

## Python Server

Preparation.
```bash
$ pip3 install grpcio grpcio-tools
```

Install packages.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=./output --grpc_python_out=./output ./protos/user.proto
```
