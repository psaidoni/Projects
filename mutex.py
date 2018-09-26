from threading import Thread, Lock

mutex = Lock()
CAN_message_1= [0x01, 0x40, 0x00, 0x00, 0x00]
print(CAN_message_1)
def CANDecode():
  mutex.acquire() #locking the resource
  CAN_message_1[0]=CAN_message_1[0] & 0x3f
  decoded = (CAN_message_1[0] << 3) + (CAN_message_1[1] >> 5)
  print(decoded)
  mutex.release() #releasing the resource

def CANUpdate():
  mutex.acquire() #locking the resource
  CAN_message_1[1] = CAN_message_1[1]+10
  mutex.release() #releasing the resource

th_CANDecode  = Thread(target=CANDecode)
th_CANUpdate  = Thread(target=CANUpdate)

th_CANDecode.start()
th_CANUpdate.start()
print(CAN_message_1)
