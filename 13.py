from ipaddress import ip_network as ip

net = ip("212.63.12.182/255.255.255.192", 0)
for i in range(len(list(net))):
    print(i, list(net)[i])
    input() #wait untill our ip come... 
#54 - answer

