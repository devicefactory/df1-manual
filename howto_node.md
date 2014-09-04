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


## Quick Test on noble

When you do `npm install noble`, it should have created `node_modules/noble` sub-directory and installed
the package for you. In that directory, you will see a test script called `dump.js`. Try running it:

```
cd node_modules/noble
sudo node dump.js
```

It should start scanning and try to discover all services and characteristics for any discovered BLE device.
The output will look something like:

```{sh}
// stateChange: poweredOn
// connect: 1cba8c2fcf43 (df1)
// RSSI update: -61 (df1)
// connect: d0ff5066b767 (GTAG2:D0FF5066B767)
// disconnect: d0ff5066b767 (GTAG2:D0FF5066B767)
{ "d0ff5066b767":
  { localName: "GTAG2:D0FF5066B767",
undefined
  }
}
// connect: 84dd20eaf3bc (df1)
// RSSI update: 127 (df1)
{ "1cba8c2fcf43":
  { localName: "df1",
{ '1800':
   { name: 'Generic Access',
     type: 'org.bluetooth.service.generic_access',
     characteristics: {} },
  '1801':
  ... 
```

Additionally, you can try running the `test.js` in the same directory.

```
sudo node test.js
```

## Writing Code

* Scanning

  `node` has nice REPL that you can easily drop into and start testing your code.
  Let's try a simple exercise to test the library.
  
  Fire up `sudo node`. We have to run with root privileges on linux to access `hci0` device.
  
  ```{javascript}
  // make sure you are in the same dir as node_modules
  var noble = require('noble')
  
  // check the state
  noble.state
  ```
  
  Before we start scanning for devices, let's implement 'discover' callback.
  
  ```{javascript}
  // called when new peripheral is discovered
  noble.on('discover', function(peripheral) {
    console.log('found peripheral ' + peripheral.advertisement.localName + ' uuid:' + peripheral.uuid)
  })
  ```
  
  We are just going to print the name of the device and its uuid.
  
  ```{javascript}
  // fire of BLE scanning!
  noble.startScanning()
  ```
  
  You'll see output like the following:
  
  > ```
  > found peripheral GTAG2:D0FF5066B767 uuid:d0ff5066b767
  > found peripheral df1 uuid:1cba8c2fcf43
  > ```
  
  To stop scanning,
  
  ```{javascript}
  noble.stopScanning()
  ```

* Peripheral Object

  We are interested in working with peripherals. There's an object associated with it, and you have to implement
  callback functions in order to interact with it.

  Let's first save the peripheral object we are interested in:

  ```{javascript}
  var p
  noble.on('discover', function(peripheral) {
    if(peripheral.advertisement.localName == "df1") {
      p = peripheral; console.log("found df1"); noble.stopScanning();
    }
  })
  noble.startScanning()
  ```
  Now, we have variable `p` representing our DF1 peripheral.

  Implement the following callback functions to see what they do:
  
  ```{javascript}
  p.on('connect', function() { console.log('connected to ' + p.uuid); p.updateRssi(); })
  p.on('rssiUpdate', function(rssi) { console.log('rssi is ' + rssi); })
  p.on('servicesDiscover', function(services) {
    for(i=0; i<services.length; i++) {
      s = services[i]; console.log('service ' + s.name + ' type: ' + s.type);
    }
  })
  ```
  
  Let's try connecting.

  ```{javascript}
  p.connect()
  ```

  If successful, you'll see the following msg:

  ```
  connected to 1cba8c2fcf43
  rssi is -59
  ```

  After that, list out the services:

  ```
  p.discoverServices()
  ```
  
  Again, the output will look something like:

  ```
  service Generic Access type: org.bluetooth.service.generic_access
  service Generic Attribute type: org.bluetooth.service.generic_attribute
  service Device Information type: org.bluetooth.service.device_information
  service Battery Service type: org.bluetooth.service.battery_service
  service null type: null
  service null type: null
  service null type: null
  ```


## Bit of Internals

The following section might interest people who want to understand how `noble` works under the hood.
Skip this section if you are only interested in the javascript API.

On linux, 2 small binary facilitates BLE communcation. When `noble` is loaded, a child process will be forked
off and the interprocess communication is carried out via system signals. These binaries will output status
and other information on stdout, and node retrieves these values using a read pipe.

All of the low-level communication is handled by two binaries:

* hci-ble

  Implements similar functionality to `hcitool lescan`. System signal `SIGUSR1` triggers underlying
  C function `hci_le_set_scan_enable`.

* l2cap-ble

  Binds and creates a socket connection against the underlying HCI device (often `hci0`). It then
  acts as a bridge between the BLE device and the higher level node.js functions. The command is
  issued through `stdin` of the process, and response is captured via `stdout`. The communication is
  done through hex strings bi-directionally.


In order to test HCI scanning, first run the binary on Linux.

```
sudo node_modules/noble/build/Release/hci-ble
```

Then from a different terminal, try sending that process `SIGUSR1`.

```
sudo kill -s SIGUSR1 `ps -ef | grep hci-ble | grep -v "grep"  | awk '{print $2}' | tail -1`
```

You'll notice that `hci-ble` binary outputs something like this on stdout.

```
$ sudo ./hci-ble
adapterState poweredOn
event DC:78:C8:E5:A1:F8,random,0201041aff590002150112233445566778899aabbccddeeff0000100c3bb,-59
event 1C:BA:8C:2F:CF:43,public,020106,-65
event 1C:BA:8C:2F:CF:43,public,040964663105125000a000020a00,-65
event 84:DD:20:EA:F3:BC,public,020106,-82
event D0:FF:50:66:B7:67,public,020105070203180218041802ff00,-73
event D0:FF:50:66:B7:67,public,140947544147323a44304646353036364237363700,-72
```

