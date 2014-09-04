#!/usr/bin/env python
import pexpect
import sys
import time
import datetime
# import json
# import select
import struct
import signal

# will be overridden if 2nd arg is provided
datalog = sys.stdout

def printlog(x):
  if not datalog==sys.stdout:
    print(x)
  datalog.write(x + "\n")


class DF1:

    def __init__( self, bluetooth_adr ):
      self.con = pexpect.spawn('gatttool -i hci0 -b ' + bluetooth_adr + ' -I')
      # self.con.interact(input_filter=self.myfilter)
      self.con.expect('\[LE\]>', timeout=600)
      self.con.sendline('connect')
      # test for success of connect
      self.con.expect('Connection successful.*\[LE\]>')
      # Earlier versions of gatttool returned a different message.  Use this pattern -
      #self.con.expect('\[CON\].*>')
      self.cb = {}
      return

    def exit(i):
      print "tearing down stuff"
      self.con.sendcontrol('c')
      self.con.sendeof()
      self.con.terminate()
      self.con.close()

    def char_write_cmd( self, handle, value ):
        # The 0%x for value is VERY naughty!  Fix this!
        cmd = 'char-write-cmd 0x%02x 0%x' % (handle, value)
        # print cmd
        self.con.sendline( cmd )
        return

    def char_read_hnd( self, handle ):
        self.con.sendline('char-read-hnd 0x%02x' % handle)
        self.con.expect('descriptor: .*? \r')
        after = self.con.after
        rval = after.split()[1:]
        byte = [n.decode("hex") for n in rval]
        self.cb[handle](byte)
        return byte

    # Notification handle = 0x0025 value: 9b ff 54 07
    def notification_loop( self ):
      while True:
        try:
          pnum = self.con.expect('Notification handle = .*? \r', timeout=3600)
        except pexpect.TIMEOUT:
          ts = datetime.datetime.now().strftime("%Y%m%dT%H:%M:%S.%f")
          print "%s TIMEOUT on expect, but keep going" % ts
          continue

        if pnum==0:
          after = self.con.after
          hxstr = after.split()[3:]
          handle = long(float.fromhex(hxstr[0]))
          if True:
            # self.cb[handle]([long(float.fromhex(n)) for n in hxstr[2:]])
            self.cb[handle]([n.decode("hex") for n in hxstr[2:]])
            pass
          else:
            print "TIMEOUT!!"
        pass

    def register_cb( self, handle, fn ):
        self.cb[handle]=fn;
        return


class DF1Callbacks:

    data = {}

    def __init__(self,addr):
        self.data['addr'] = addr

    def batt(self,v):
        blev = struct.unpack('<B',v[0])[0]
        ts = datetime.datetime.now().strftime("%Y%m%dT%H:%M:%S.%f")
        printlog( "batt:%s,%.1f" % (ts,blev) )

    def accel(self,v):
        ts = datetime.datetime.now().strftime("%Y%m%dT%H:%M:%S.%f")
        x = float(struct.unpack('<b',v[0])[0]/64.0)
        y = float(struct.unpack('<b',v[1])[0]/64.0)
        z = float(struct.unpack('<b',v[2])[0]/64.0)
        printlog( "acc:%s,%.6f,%.6f,%.6f" % (ts,x,y,z) )

    def accel14(self,v):
        ts = datetime.datetime.now().strftime("%Y%m%dT%H:%M:%S.%f")
        # printlog("str value x: %s" % (v[0]+v[1]).format('%x'))
        x = float(struct.unpack('<h',v[1]+v[0])[0] >> 2) /4096.0 # dividing by 4 shifts 2 bits
        y = float(struct.unpack('<h',v[3]+v[2])[0] >> 2) /4096.0
        z = float(struct.unpack('<h',v[5]+v[4])[0] >> 2) /4096.0
        printlog( "acc:%s,%.8f,%.8f,%.8f" % (ts,x,y,z) )

def main():
    global datalog

    if len(sys.argv)<2:
      print "usage: %s <baddr> [batt|acc|acc14] [file]" % sys.argv[0]
      sys.exit(1)

    bluetooth_adr = sys.argv[1]
    mode = "batt"
    #data['addr'] = bluetooth_adr
    if len(sys.argv) > 2:
      mode = sys.argv[2]

    if len(sys.argv) > 3:
      # with open(sys.argv[2], 'w+') as datalog
      datalog = open(sys.argv[3], 'w+')

    try:   
     print "[re]starting.."

     tag = DF1(bluetooth_adr)
     cbs = DF1Callbacks(bluetooth_adr)

     # so that we catch ctrl-c and then kill the child as well as the current proc
     def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        tag.exit()
        if not datalog==sys.stdout:
          datalog.close()
        sys.exit(0)

     signal.signal(signal.SIGINT, signal_handler)
     # print('Press Ctrl+C')
     # signal.pause()

     if mode == "acc":
        # enable accelerometer
        tag.register_cb(0x30,cbs.accel)
        tag.char_write_cmd(0x2d,0x01)
        tag.char_write_cmd(0x31,0x0100)

     if mode == "acc14":
        # enable accelerometer
        tag.register_cb(0x34,cbs.accel14)
        tag.char_write_cmd(0x2d,0x02)
        tag.char_write_cmd(0x35,0x0100)

     if mode == "batt":
        # battery
        tag.register_cb(0x25,cbs.batt)
        tag.char_read_hnd(0x25)
        tag.char_write_cmd(0x26,0x0100)

     tag.notification_loop()

    except:
     pass

if __name__ == "__main__":
    main()

