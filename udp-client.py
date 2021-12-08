import pickle
import struct
import socket
import hashlib


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        send_date = pickle.dumps(x)
        data_len = len(send_date)
        data_md5 = pickle.dumps(hashlib.md5(send_date).hexdigest())
        packet = struct.pack('>2h2i2028s16p', version, pkt_type, seq_id, data_len, send_date, data_md5)
        s.sendto(packet, address)
        seq_id += 1
    s.close()


if __name__ == '__main__':
    user_data = ['自动化运维', [1, 'abc'], 3]
    udp_send_data('120.27.210.240', 6666, user_data)
