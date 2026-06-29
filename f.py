def test():
    return 1

import lps, psn, psw
from datetime import datetime
    
def oopsies():
    print('It seems their is an error. Please do not contact the developer, she is anti-social.')
    exit()
    
def process_cmd(userscmd):
    userscmd = userscmd.split()
    while userscmd[0] != 'exit':
        if userscmd[0] == 'scan':
            if userscmd[1] in ['UDP','udp' ]:
                if userscmd[2] in ['ports', 'ports:']:
                    lps.scan_udp(userscmd[3])
                    cmd_done() 
            elif userscmd[1] in ['TCP', 'tcp']:
                if userscmd[2] in ['ports', 'ports:']:
                    lps.scan_tcp(userscmd[3])
                    cmd_done() 
            elif userscmd[1] == 'both':
                if userscmd[2] in ['ports', 'ports:']:
                    lps.scan_tcp(userscmd[3])
                    lps.scan_udp(userscmd[3])
                    cmd_done()
        #elif userscmd[0] == 'a': psw.PiNgSwEePeR('192.168.50.1/24')
        elif userscmd[0] == 'ping-sweep':psw.PiNgSwEePeR(userscmd[1])
        elif userscmd[0] == 'packet-sniff':psn.SNIFFsniffINHHHHAAAALLLLLLEEEEEEsneeeeeeeeeeeee33333333333333333EEEEEEEEEEEEEEEEEEEEEZZZZZEEEEEEEEbcHAYfever(userscmd[1])

        else:
            print('Please enter a valid command.')

        userscmd = str(input('PeiceOfShxt>>> '))
        userscmd = userscmd.split()
    exit()

def cmd_done():
    print(f'This command has been sucsessfully been completed at {datetime.now()}')
