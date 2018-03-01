#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        resp = str(recvSocket.recv(2048), 'utf-8')

        try:
            res = resp.split()[1]
            _, op1, operation, op2 = res.split('/')
            sol = calculadora.funciones[operation](float(op1), float(op2))
            answer = ("<p>Operacion: " + str(op1) + " " +
                      operation + " " + str(op2) + " = " + str(sol) + "<p>")
        except:
            answer = ('<p>La entrada esta mal, vuelva a intentarlo.' +
                      'Recuerda que la entrada debe ser:' +
                      'localhost:1234/op1/operation/op2.<p>')
        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Bienvenido.</h1>" + answer +
                        "</body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
