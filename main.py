import os
import json
import sys
def servers_beheren():
    if sys.argv(1) == "management":
        keuze = input("Wat wil je doen toevoegen(T),verwijderen(V) of weergeven(W)? ")
        match keuze:
            case "T":
                server = input("welke server wil je toevoegen? ")
                with open("servers.json","w") as f:
                    json.dump(server,f)
            case "V":
                server = input("welke server wil je verwijderen? ")
                with open("servers.json","w") as f:
                    lst = json.load(f)
                    del lst[server]
                    json.dump(lst)
            case "W":
                with open("servers.json","r") as f:
                    print(servers = json.load(f))
            case _:
                print("Foutieve invoer probeer opnieuw")
with open("servers.json","r") as f:
    servers = json.load(f)
def ping_server(servers):
    if sys.argv(1) == "check":
        for item in servers:
            response = os.system("ping -c 1 " + item)
            if response == 0:
                print(item, 'is up!')
            else:
                print(item, 'is down!')