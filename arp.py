import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *


arp_pkt = ARP(op=2, psrc='192.168.186.100', hwdst='ff:ff:ff:ff:ff:ff', pdst='192.168.186.100')
arp_pkt.show()
for i in range(20):
    sr1(arp_pkt, timeout=2, verbose=False)
