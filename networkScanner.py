import nmap

ns = nmap.PortScanner()

print(ns.nmap_version())
ns.scan('192.168.0.1' , '1-1024', '-v')
print(ns.scaninfo())

print(ns.csv())

print(ns.ns.scanstats())
print(ns.all_hosts())

print(ns['192.168.0.1'].state())

print(ns['192.168.0.1'].all_protocols())

print(ns['192.168.0.1']['tcp'].keys())

print(ns['192.168.0.1'].has_tcp(80))