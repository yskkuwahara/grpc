# grpc

## Python Server

Install packages.
```bash
$ pip3 install grpcio grpcio-tools
```

Generate resources from proto definition.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=./servers/python --grpc_python_out=./servers/python ./protos/user.proto
```
