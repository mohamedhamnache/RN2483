#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import serial


writeconfig = 1
# Data rate values [0-5]
dr = 5
# Keys Configuration 
DevEUI = "BEEFDEAD0009DEAA"
AppEUI = "63bb9e7802a551c0"
AppKey = "BEEF456789ABCDEF0123456789ABCDEF"


def send(data):
    p = serial.Serial("/dev/ttyACM0", 57600)
    p.write(str.encode(data + "\x0d\x0a"))
    data.rstrip()
    print(data)
    time.sleep(2)
    rdata = p.readline()
    rdata = rdata[:-1]
    print(rdata)


def set_transmission_parameter():
    time.sleep(1)


send("sys reset")
time.sleep(1)

if writeconfig is 1:
    time.sleep(1)
    send("mac set appeui " + AppEUI)
    send("mac set appkey " + AppKey)
    send("mac set deveui " + DevEUI)
    send("mac set dr " + str(dr))
    # Enable ADR
    send("mac set adr off")
    send("mac save")
    time.sleep(5)

send("mac join otaa")

time.sleep(7)
j = 0

while True:

    msg = "mohamed"
    # print(msg)
    # print(msg.encode("utf-8").hex())
    # time.sleep(7)
    # print(r)
    msg = msg.encode("utf-8").hex()
    # print(msg)
    send("mac tx uncnf 1 " + msg)
    # Waite 10 seconds to send the next message.
    time.sleep(10)
    j = j + 1
