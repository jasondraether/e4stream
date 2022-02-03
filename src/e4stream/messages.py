from enum import Enum 

class _Send(Enum):
    PAUSE = "pause ON\r\n"
    RESUME = "pause OFF\r\n"
    DISCONNECT = "device_disconnect\r\n"
    LIST = "device_list\r\n"
    CONNECT_L = lambda device_id: f"device_connect {device_id}\r\n"
    SUBSCRIBE_L = lambda subscription: f"device_subscribe {subscription} ON\r\n"


class _Receive(Enum):
    SUB_OK_L = lambda subscription: f'R device_subscribe {subscription} OK\n'
    DEV_OK = 'R device_connect OK\n'
    PAUSE_ON_ACK = 'R pause ON\n'
    PAUSE_OFF_ACK = 'R pause OFF\n'
    DISCONNECT_MESSAGE = "connection lost to device\n"  

class Messages():
    SEND = _Send
    RECV = _Receive
    
    