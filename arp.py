import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *


pkt = ARP()
pkt.show()
arp_pkt = ARP(op=2, psrc='192.168.56.100', hwdst='ff:ff:ff:ff:ff:ff', pdst='192.168.56.100')
arp_pkt.show()
for i in range(20):
    sr1(pkt, timeout=2, verbose=False)