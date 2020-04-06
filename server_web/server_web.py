def tip(i):
    switcher={
            "html": "text/html",
            "css": "text/css",
            "js": "application/js",
            "png": "text/png",
            "jpg": "text/jpeg",
            "jpeg": "text/jpeg",
            "gif": "text/gif",
            "ico": "image/x-icon"
            }
    return switcher.get(i,"text/plain")

import socket

# creeaza un server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# specifica ca serverul va rula pe portul 5678, accesibil de pe orice ip al serverului
serversocket.bind(("", 5678))
# serverul poate accepta conexiuni; specifica cati clienti pot astepta la coada
serversocket.listen(5)

while True:
    print("#########################################################################")
    print("Serverul asculta potentialii clienti.")
    # asteapta conectarea unui client la server
    # metoda `accept` este blocanta => connection, care reprezinta socket-ul corespunzator clientului conectat
    (connection, address) = serversocket.accept()
    print(f"S-a conectat un client la adresa: {address[0]} si portul {address[1]}"  )
    # se proceseaza cererea si se citeste prima linie de text
    cerere = ""
    linieDeStart = ""

    while True:
        data = connection.recv(1024)
        cerere = cerere + data.decode()
        print("S-a citit mesajul: \n---------------------------\n" +
              cerere + "\n---------------------------")
        pozitie = cerere.find('\r\n')
        if pozitie > -1:
            linieDeStart = cerere[0:pozitie]
            print("S-a citit linia de start din cerere: ##### " + linieDeStart + " ##### ")
            break
    # TODO interpretarea sirului de caractere `linieDeStart` pentru a extrage numele resursei cerute
    # TODO trimiterea răspunsului HTTP
    print("Raspuns:")
    resursa = linieDeStart.split(" ") #separator
    resursa = resursa[1]   # primul cuvant
    resursa = resursa[1:]   # cuvantul fara "/"

    fisier = open("continut/" + resursa, "rb")
    if fisier:
        mesaj:bytes = fisier.read()
        status = "HTTP/1.1 200 OK" + "\r\n"
        fisier.close()
    else:
        mesaj:bytes = b"File not found"
        status = "HTTP/1.1 404 Not Found" + "\r\n"

    res = resursa.split(".")[-1]
    contentType = tip(res) + "\r\n"
    server = "server_web.py" + "\r\n"
    contentLenght = str(len(mesaj)) + "\r\n"
    response = status + "Content-Length:" + contentLenght + "Content-Type: " + contentType + "Server: " + server + "\r\n"
    httpResponse = response.encode() + mesaj
    connection.sendall(httpResponse)
    print("Raspuns trimis")
    print("Resursa ceruta: " + resursa)
    connection.close()
    print("S-a terminat comunicarea cu clientul.")


