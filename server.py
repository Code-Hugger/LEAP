def main():
    while True:
        handler()

def handler():
    import socket, sys, pickle
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    HOST = ''
    PORT = 9001

    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    s.listen(10)
    print 'Socket now listening'
 
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = conn.recv(1024)
    myDict = pickle.loads(data)
    print myDict
    if myDict["question"] == "net_test":
        ans = net_test(myDict["data"], myDict["answer"])
        conn.send(pickle.dumps(ans))
    s.close()

def net_test(data = None, answer = None):
    from random import randint
    if answer == None:
        return [randint(10,99), randint(10, 99)]
    else:
        return answer == sum(data)

if __name__ == '__main__':
    main()
