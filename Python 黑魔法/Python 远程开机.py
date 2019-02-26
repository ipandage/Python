# -*- coding: utf-8 -*-
import time
import socket
import struct
import requests
import os

def wake_up(broadcast='192.168.0.255', mac='DC-4A-3E-78-3E-0A'):
    MAC = mac
    BROADCAST = broadcast
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace(":", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # sock.sendto(send_data, (BROADCAST, 7))
        # time.sleep(1)
        # sock.sendto(send_data, (BROADCAST, 7))
        # time.sleep(1)
        # sock.sendto(send_data, (BROADCAST, 7))

        sock.sendto('shutdown -s -t 00', (BROADCAST, 7))

        print("Done")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    wake_up('127.0.0.1','88:e9:fe:6d:57:16')