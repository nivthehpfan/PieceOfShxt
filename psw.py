def test():
    return 1

import nmap

def PiNgSwEePeR(SUBNET):
    nm = nmap.PortScanner()
    print(f'Please wait. Pinging devices on subnet {SUBNET}.')
    output = []
    try:
        result = nm.scan(hosts=SUBNET, arguments='-sn')
        for host in nm.all_hosts():
            stateofTHING = nm[host].state()
            if stateofTHING == 'up':
                output.append(f'The device with the IPv4 address {host} is on and connected to the internet.')
        for i in range(len(output)): print(output[i])
    except BaseException as aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:
        print(f'Error:{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}')

