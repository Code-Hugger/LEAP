def _send_to_server(myDict):
    '''REALLY bad socket client code, used as a wrapper to interface with a remote server'''
    # All functions that start with _ are ignored by the game server
    import socket, sys, pickle
    HOST, PORT = "localhost", 9001

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(pickle.dumps(myDict))

    received = pickle.loads(sock.recv(1024))
    return received

# kwargs is a catch all for future compatability, right now it only contains "playerName"
def net_test(data = None, answer = None, **kwargs):
    '''No business logic for this challenge is exposed to the user'''
    return _send_to_server({"question": "net_test", "data": data, "answer": answer, 'playerName': kwargs["playerName"]})
