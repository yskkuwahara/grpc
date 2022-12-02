#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
import json
import grpc
import user_pb2
import user_pb2_grpc

# User data
with open("../users.json") as fp:
    users = json.load(fp)


class UserService(user_pb2_grpc.UserServiceServicer):
    def get(self, request, context):
        user_id = request.id

        # Find user from users by key of user_id string
        if str(user_id) not in users:
            return user_pb2.UserResponse(error=True, message="not found")
        user = users[str(user_id)]

        # Create UserResponse value
        result = user_pb2.User()
        result.id = user["id"]
        result.name = user["name"]
        result.status = user_pb2.User.UserStatus.Value(user["status"])
        result.hobby_list = user["hobby_list"]

        return user_pb2.UserResponse(error=False, user=result)


def main():
    server = grpc.server(ThreadPoolExecutor(max_workers=2))

    # Register Servicer class to server object
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    # Use add_secure_port if you request via HTTPS.
    server.add_insecure_port('[::]:3333')

    # Start listening port
    server.start()

    server.wait_for_termination()


if __name__ == '__main__':
    main()
