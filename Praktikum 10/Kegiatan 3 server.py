import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50009))
s.listen(5)
print "Server Siap"
perintah = ""
si=0
a=0
t=0

while perintah != "keluar":
    komm, addr = s.accept()
    while perintah != "keluar":
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == "keluar":
            komm.send("done")
            s.close()
            break
        print "pesan: ", perintah
        if len(item)==2:
            if perintah == "sisi":
                si=int(item[1])
                komm.send("sisi disimpan")
            elif perintah == "alas":
                a=int(item[1])
                komm.send("alas disimpan")
            elif perintah == "tinggi":
                t=int(item[1])
                komm.send("tinggi disimpan")
            else:
                komm.send("Pesan tidak diketahui")
        elif perintah == "hitung":
            L=float(si*si+2*a*t)
            response = "Luas Limas Segiempat dengan sisi {} alas {} tinggi {} adalah {}".format(si,a,t,L)
            komm.send(response)
        else:
            komm.send("Pesan tidak diketahui")
