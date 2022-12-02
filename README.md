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

#### Run Server
```bash
$ cd servers/python
$ python3 main.py
```

### For Client
Generate resources from proto definition.
```bash
$ python3 -m grpc_tools.protoc -I./protos --python_out=./clients/python --grpc_python_out=./clients/python ./protos/user.proto
```

#### Request
Request by user_id param.
```bash
$ cd servers/python
$ python3 main.py 2
```
