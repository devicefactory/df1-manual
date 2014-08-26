# DF1-MANUAL

![logo](https://raw.githubusercontent.com/devicefactory/share/master/media/brand/df-icon-solid-black-trans.png)


## About

Welcome to Device Factory's DF1 instruction page!

Here you'll find all the information you need to interact with DF1.
Each markdown file describes how to communicate with DF1 using various platforms.

DF1 marks our first foray into connected device.
We created DF1 so that we can learn, have fun, and invite others to join us in hacking with it.

Below you'll find topics that are broadly separated by the different platforms from which you can
communicate with DF1.

## Tutorials

* [Getting Started](howto_start.md)

  Start here! This document describes how to get up and running with our DF1.

* [Raspberry Pi and DF1](howto_ios.md)

  Learn how to build your own RPi base station. RPi can talk BLE with a small tweaks, and we even
  provide a customized downloadable image you can use. This way, you can use RPi to interact with 
  DF1 almost out-of-the-box. 

* [iOS and DF1](howto_ios.md)

  Learn how to use AND contribute to DF1's iOS library. Here, we highlight parts of the library.
  However, nothing stops you from writing your own app just by using CoreBluetooth framework.
  You just need to know which services and characteristics are available for Df1.

* [Node.js and DF1](howto_ios.md)

  Learn how to communicate with DF1 using node.js library called
  [noble](https://github.com/sandeepmistry/noble) and other library specifically written
  for DF1!

* [Updating the Firmware](howto_fwupdate.md)

  The firmware can be upgraded over the air. Currently, the demo app for Df1 does not contain this
  feature. However, since DF1 uses Texas Instruments CC2541, it can be flashed using TI's iOS app.

## Other Docs

* [Operation Manual](manual.md)

  Regulatory operational manual for DF1.

* [BLE Service Spec](services.md)
  
  Lists all BLE services and characteristics for DF1.
