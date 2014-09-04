# Node.js and DF1

![nodejs_logo](https://raw.githubusercontent.com/devicefactory/df1-manual/master/pics/nodejs_logo_and_df_logo.png)

There's an excellent library called [noble](https://github.com/sandeepmistry/noble) that gives javascript access to 
the BLE world. The library implements executable C binary that handles low-level BLE communication, acting as a "bridge"
between node.js and specifics of BLE protocol. The library is supported on both Linux and MacOS.

You can find more details about the library in other related github repos. 
Shout out to [sandeep](https://github.com/sandeepmistry), who's done all of this great work on node.js + BLE.

* [noble](https://github.com/sandeepmistry/noble)

  Short for "NOde" + "BLE", it serves as the underlying library to interact with DF1.
  The library is geared towards building javascript based BLE central.

* [bleno](https://github.com/sandeepmistry/bleno)

  We won't cover this library in the tutorial, but "BLE" + "NOde" implements BLE peripherals.
  This library would be useful if you want to use your laptop to masquerade as a BLE device.

* [noble-device](https://github.com/sandeepmistry/noble-device)

  Convenient wrappers to abstract any BLE peripherals. Depends on `noble`.

* [node-device-factory1](https://github.com/sandeepmistry/node-device-factory1)

  An example library that inherits from NobleDevice (`noble-device`) class.
  It first discovers the services and characteristics, then proceeds to toggle the LED's and
  subscribe to xyz events.

* [df1-browser](https://github.com/sandeepmistry/df1-browser)

  Experimental project to run noble directly on the browser. Instead of running the scripts solely on the
  serverside, this technique can enable "full stack" development of BLE.


## Prerequisites

* If you haven't done so already, download and install [node.js](http://nodejs.org/download/).
* If you are on Linux, download and install libbluetooth-dev

  ```
  sudo apt-get install libbluetooth-dev
  ```
  Optionally, you can manually install the entire [bluez](http://www.bluez.org/download/) package.
  If you choose to install bluez from source, you might want `./configure --disable-systemd`.

* Download and install [noble](https://github.com/sandeepmistry/noble)

  You can follow the README.md docs for more detailed explanation of the library.



