from xbee import XBee
import serial
import time 

#set up serial port (on USB)
#ser=serial.Serial('/dev/ttyUSB0',9600)

#attempt to set up TX RX pins to transmit
ser=serial.Serial('/dev/ttyS0',9600)

xbee=XBee(ser)

#request Adress of coordinator xbee --------------------------------
#xbee.send('at',frame_id='A',c
ommand='DH')
#print(xbee.wait_read_frame())

#request Adress low of coordinator xbee 
#xbee.send('at',frame_id='B',command='DL')
#print( xbee.wait_read_frame())
#-------------------------------------------------------------


##xbee.remote_at(
##    dest_addr=b'\x56\x78',
##    command='D3',
##    parameter=b'\x05')
##print("stop 1")
##xbee.remote_at(
##    dest_addr=b'\x56\x78',
##    command='WR') 
##print("stop 2")

#clock wise (pin D3 high) ----------------------------------------
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='D3',
    parameter=b'\x05')
print("Counter Clockwise")
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='WR') 


time.sleep(2)
#stop turning (Pin D3 Low)-------------------------------------
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='D3',
    parameter=b'\x04')
print("HALT")
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='WR') 

#counter clock wise (Pin D4 High) ---------------------------------
time.sleep(2)
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='D4',
    parameter=b'\x05')
print("clockwise")
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='WR')


time.sleep(2)

#stop turning (Pin D4 Low) ----------------------------------------
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='D4',
    parameter=b'\x04')
print("HALT")
xbee.remote_at(
    dest_addr=b'\xff\xff',
    command='WR')     