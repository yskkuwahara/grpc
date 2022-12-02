# grpc

## Python

Install packages.
```bash
$ pip3 install grpcio grpcio-tools
```

### For Server
Generate resources from proto definition.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=./servers/python --grpc_python_out=./servers/python ./protos/user.proto
```

### For Client
Generate resources from proto definition.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=./clients/python --grpc_python_out=./clients/python ./protos/user.proto
```
