import socket
import base64

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    for i in range(2):
        data = s.recv(2084)
    s.close()
    return data
    
sd="l33tserver pleaseAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#flag="IceCTF{unleash_th3_Blocks_aNd_find_what"
flag =""
for j in range(64):
	sd=sd[:len(sd)-1]
	dt = base64.b64encode(sd)
	f1 = netcat("l33tcrypt.vuln.icec.tf",6001,dt+"\n")
	f1 =f1[53:len(f1)-1]
	f1 = base64.b64decode(f1).encode('hex')[:160]
	for k in range(39,127):
		dt = base64.b64encode(sd+flag+str(chr(k)))
		f2 = netcat("l33tcrypt.vuln.icec.tf",6001,dt+"\n")
		f2 = f2[53:len(f2)-1]
		f2 = base64.b64decode(f2).encode('hex')[:160]
		if f2 == f1 :
			flag += str(chr(k))
			break
	print "flag : "+flag+"\n"
