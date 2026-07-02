def test():
    return 1

import nmap





def scan_tcp(address): 
    print(f'Please wait. The program has recieved the address: {address}, and is now working on scanning it to find the open TCP ports.\nThis will take ~30 seconds.')
    nm = nmap.PortScanner()
    result = nm.scan(address, arguments='-sV -Pn --disable-arp-ping')
    output = []
    scannedbynmap = nm[address]['tcp'].keys()
    for port in scannedbynmap:
        if (nm[address]['tcp'][port]['state']) == 'open': output.append(f'Port {port} is open with TCP running, using {nm[address]['tcp'][port]['version']}')
    if (len(scannedbynmap)) == 0: print('The device you are trying to scan seems unreachable.')
    for i in range(len(output)): print(output[i])


def scan_udp(address): 
    print(f'Please wait. The program has recieved the address: {address}, and is now working on scanning it to find the open UDP ports.\nThis will take ~90+ seconds.')
    nm = nmap.PortScanner()
    nm.scan(address, arguments='-sU --top-ports 50 -Pn --disable-arp-ping')
    output = []
    if address not in nm.all_hosts():
        print('The device you are trying to reach is unreachable.')
        return 0
    elif 'udp' not in nm[address].keys(): 
        print('It seems that their is no UDP ports open. UDP is sketchy I don\'t like it.')
        return 0
    elif nm[address]['udp'] == {}: 
        print('It seems that you have UDP ports, but nmap didnt get any response from them. How unreliable of UDP.')
        return 0
    scannedbynmap = nm[address]['udp'].keys()
    for port in scannedbynmap:
        chec_state = nm[address]['udp'][port]['state']
        if chec_state == 'open': output.append(f'Port {port} is {chec_state} with UDP.')
    if not(output):print('Scan finished, no UDP ports detected.')
    else:
        for i in range(len(output)): print(output[i])

