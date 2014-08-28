# Raspberry Pi and DF1

Interested in interacting with DF1 from Raspberry Pi or just hacking BLE in general?
You've come to the right place (or tutorial)!

<img src=https://raw.githubusercontent.com/devicefactory/df1-manual/master/pics/rpi_setup.jpg width=600>

Here, you'll learn how to communicate with DF1 using Raspberry Pi.
But before we begin, we need to make sure Raspberry Pi is equipped with all the necessary parts.

## Prerequisites

* Raspberry Pi (Model B)

  Haven't tested on Model A, but why settle for Model A when you can get Model B??

* BLE Dongle

  [Pluggable USB](http://plugable.com/products/usb-bt4le) dongle is the one we are using.
  You can find it in [Amazon.com](http://www.amazon.com/Plugable-Bluetooth-Adapter-Windows-Compatible/dp/B009ZIILLI/ref=sr_1_fkmr1_2?ie=UTF8&qid=1409195842&sr=8-2-fkmr1&keywords=pluggable+usb+ble+dongle) for just $13 as of this writing.
  There are various supported BLE dongles out there.  Here is a [list](https://github.com/sandeepmistry/noble/wiki/Compatible-devices)

* SD Card (8BG preferred) with necessary software installed.

  Unless you want to install all the necessary packages yourself, we suggest using the Raspberry Pi image we've prepared.
  Refer to the installation section below for more details.  

* Optional: enclosure 
  
  Raspberry Pi looks more sweet with an enclosure.  :-)

* Optional: Lapdock

  <img src=https://raw.githubusercontent.com/devicefactory/df1-manual/master/pics/rpi_lapdock.jpg width=400>

  Used to be [cheaper](http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2054436.m570.l1313.TR11.TRC1.A0.H0.Xatrix+lapdock&_nkw=atrix+lapdock&_sacat=0), but Motorola Atrix 4G Lapdock is perfect for on-the-go Raspberry Pi computing. You can find some more information about the setup [here](http://www.adafruit.com/blog/2012/09/10/cables-adapters-for-the-atrix-raspberry-pi-laptop/).


## Installing Necessary Components

**If You Prefer the Image**

* First click on this link: **[Download RPi Image](link)**

  The image contains all the necessary packages already compiled and installed for you to
  just get up and running with BLE.

* Install the image to an SD card at least 4GB in size
  
  Follow these tutorials to setup your SD card.
  - [For Linux](http://www.raspberrypi.org/documentation/installation/installing-images/linux.md) 
  - [For MacOS](http://www.raspberrypi.org/documentation/installation/installing-images/mac.md)
  - [For Windows](http://www.raspberrypi.org/documentation/installation/installing-images/windows.md)

* Optional: Extending the partition

  If you have a larger SD card, you'll notice that writing the image only allows RPi to "see" only 4GB of usable space.

  > **CAUTION** You can extend the partition under your SD card, but it's easy to cause a serious headache if you don't do it right.
  > Please **Skip** this section if you are unsure about what you are doing.
   
  First insert the SD card to a linux machine. If you don't have a linux machine, follow other tutorials online
  on extending raspberry pi partition on SD cards.
  
  This command will tell you which "disks" are available on your system.

  ```
  $ fdisk -l 
  ```

  Choose the device corresponding to the SD card.
  **BEWARE**: if you choose the wrong disk in the next step, you can mess up your linux machine.
  
  In my case, I had the SD card mounted on /dev/sdd.

  ```
  $ sudo parted /dev/sdd
  GNU Parted 2.3
  Using /dev/sdd
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) print
  Model: USB 2.0 SD/MMC Reader (scsi)
  Disk /dev/sdd: 7948MB
  Sector size (logical/physical): 512B/512B
  Partition Table: msdos

  Number  Start   End     Size    Type     File system  Flags
   1      4194kB  62.9MB  58.7MB  primary  fat16        lba
   2      62.9MB  3905MB  3842MB  primary  ext4
  (parted) rm 2
  (parted) mkpart primary 62.9MB 7948MB
  (parted) p
  (parted) quit
  ```
 
  Now that the partition table was modified using `parted`, I can extend the filesystem.

  ```
  sudo e2fsck -f /dev/sdd2
  sudo resize2fs /dev/sdd2
  ```
  That's it, now you can insert the SD card into RPi and make use of all available space.

* Check the tools

  Run these commands on the command line to confirm:

  ```
  $ which hciconfig
  $ which hcitool
  $ which gatttool
  ```

  These commands should be available under `/usr/local/bin`.
  
  As a bonus, you should also see:

  ```
  $ which node
  $ which tmux
  $ which vim
  ```

**If you prefer installing things yourself** 

* Download and Install [bluez](http://www.bluez.org/) package.
  
  You can find some helpful [instructions](https://learn.adafruit.com/pibeacon-ibeacon-with-a-raspberry-pi/setting-up-the-pi)
  on how to get this package installed on Raspberry Pi. You will need an active network connection, because required libraries
  need to be installed using debian pkg manager (apt-get) first.
  We are currently using older 5.4 version, but the newer versions should work just fine. 

  One bit of note: the installation of required libs as well as compilation of bluez package will take a while.
  It would be faster to just download the 4GB file and write the image to an SD. 

* Optional: Install node.js

  With the help of [noble](https://github.com/sandeepmistry/noble) Node.js library, BLE development gets much easier.


## Testing BLE

With the SD card loaded up with necessary software, first plug in the BLE usb dongle and power on the Raspberry Pi.
Take note that the following sections also apply to any linux machine with BLE usb dongle and Bluez software installed.

1. Turning the adaptor on

  First check if `hci0` adaptor is up.
  
  ```
  $ sudo hciconfig
  ```
  
  It should show output like the following. In the output, `hci0` indicates the device representing your BLE USB dongle.
  ```
  hci0:   Type: BR/EDR  Bus: USB
          BD Address: 00:02:72:C5:C3:4A  ACL MTU: 1021:8  SCO MTU: 64:1
          UP RUNNING PSCAN
          RX bytes:606 acl:0 sco:0 events:36 errors:0
          TX bytes:939 acl:0 sco:0 commands:36 errors:0
  ```

  Run
  ```
  $ sudo hciconfig hci0 up
  ```

2. Discover BLE Devices
  
  In order to connect to any BLE peripheral, we first need to find out their addresses.

  ```
  $ sudo hcitool lescan
  ```
  
  It should start listing out the devices like so:
  ```
  LE Scan ...
  1C:BA:8C:2F:CF:43 (unknown)
  1C:BA:8C:2F:CF:43 df1
  DC:78:C8:E5:A1:F8 (unknown)
  84:DD:20:EA:F3:F0 (unknown)
  84:DD:20:EA:F3:F0 df1
  ```

3. Connect to DF1

  From the discovered devices above, I chose `84:DD:20:EA:F3:F0`. It gets a bit harder to identify the devices when
  you have lots of DF1's around... 

  ```
  $ gatttool -b 84:DD:20:EA:F3:F0 -i hci0 -I
  ```

  Now, this command will put you into an interactive session that looks like:
  
  ```
  [84:DD:20:EA:F3:F0][LE]> 
  ```

  Try typing and you'll get:

  ```
  [84:DD:20:EA:F3:F0][LE]> connect
  Attempting to connect to 84:DD:20:EA:F3:F0
  Connection successful
  ```

4. Discover and Communicate

  Under `gatttool` interface, try the following commands:

  ```
  > primary
  ```

  You'll see that all the services get listed like this:

  ```
  attr handle: 0x0001, end grp handle: 0x000b uuid: 00001800-0000-1000-8000-00805f9b34fb
  attr handle: 0x000c, end grp handle: 0x000f uuid: 00001801-0000-1000-8000-00805f9b34fb
  attr handle: 0x0010, end grp handle: 0x0022 uuid: 0000180a-0000-1000-8000-00805f9b34fb
  attr handle: 0x0023, end grp handle: 0x0027 uuid: 0000180f-0000-1000-8000-00805f9b34fb
  attr handle: 0x0028, end grp handle: 0x006a uuid: 0000aa10-0000-1000-8000-00805f9b34fb
  attr handle: 0x006b, end grp handle: 0x0071 uuid: 0000aa60-0000-1000-8000-00805f9b34fb
  attr handle: 0x0072, end grp handle: 0xffff uuid: f000ffc0-0451-4000-b000-000000000000
  ```

  ```
  > characteristics
  ```
  This command will take a bit longer, and it will come back with exhaustive list of all 
  available characteristics in the peripheral.

  Let's try to toggle the LED. Locate the interested UUID by looking at the long string that comes after
  `uuid:` on each line. For example, you can spot the Test Service characteristics here:

  ```
  handle: 0x006c, char properties: 0x02, char value handle: 0x006d, uuid: 0000**aa61**-0000-1000-8000-00805f9b34fb
  handle: 0x006f, char properties: 0x0a, char value handle: 0x0070, uuid: 0000**aa62**-0000-1000-8000-00805f9b34fb
  ```

