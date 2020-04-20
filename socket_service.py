import requests
import struct
from concurrent.futures import ThreadPoolExecutor
from pvc import PVC
# Python Vsphere Client 
#https://pypi.org/project/pvc/
#https://pvc.readthedocs.io/en/latest/screenshots.html

# require user id & content
executor = ThreadPoolExecutor(2)

class SocketService():
    def __init__(self, host, port, conn_id):
        self.host = host
        self.port = port
        self.conn_id = conn_id

    def socket_send(self, message_id, data):
        try:
            db_obj = {**data['CONTROL_HEADER'], **data['BODY'], "_USER_ID":user_id}
            print(db_obj)
            #Code = db_obj['FUNCTION_CODE']
            
            #socket
            pvc = PVC(self.host, self.port, self.conn_id)

            #register connection
            msg_regist = pvc.bodyMess()
            msg_rcv = pvc.send_msg(msg_regist)

            msg = pvc.bodyMess(self.conn_id, ExCode='7', msgTy='O', bodyData=content)
            print(msg)
            msg_rcv = pvc.send_msg(msg)
            print(msg_rcv)

        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    host = "vivy.com"
    port = 8080
    conn_id = 1
    client = SocketService(host, port,conn_id)
    msg_got = client.socket_send()



  
 