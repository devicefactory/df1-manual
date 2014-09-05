# iOS App and DF1

<img src=https://raw.githubusercontent.com/devicefactory/share/master/media/df1/df1-honeycomb-front-transparent.png width=600>

The iOS library for DF1 and its accompanying demo app is open source, and you can find it under:

  [df1-ios repo](https://github.com/devicefactory/df1-ios)

In this tutorial, we will discuss

* How to use the demo app
* How to create your own iOS app using the df1 library


## Installation

First clone the git repo:

```
git clone git@github.com:devicefactory/df1-ios.git
```

You will need Apple Developer license to install the app on your phone.
The iPhones 4S and above has bluetooth low energy equipped. The older iPhones will not work.

Follow the [instruction on README](https://github.com/devicefactory/df1-ios/blob/master/README.md)
to get the project compiled and uploaded to your phone.


## DF1 Demo App

Currently, the demo app can:

* scan and discover DF1 devices
* subscribe to battery level notifications
* subscribe to 8 bit XYZ data
* subscribe to tap event data
* toggle LED
* associate user assigned name to a device

The TODO list is perhaps more numerous than the features.
They will be listed at the end of this tutorial.

When you first open up the app, it will try to scan for BLE devices by default.
It will timeout after couple of seconds. In order to manually initiate scanning,
swipe your finger vertically down the screen (pulldown). You'll see the progress wheel
appear to indicate that the scanning was initiated.

<img src=pic/app_scan.png width=200>

If you have DF1 in detectible range, you'll see each distinct DF1's show up 
as a box like so:

<img src=pic/app_discover.png width=200>

When it detects DF1 device, the app will additionally connect to the device and carry
out the following operations:

* requests for RSSI (signal strength) updates every 2 seconds
* discover subset of service characteristics
* provide Red LED toggle button upon initialization

<img src=pic/app_discover_initialized.png width=200>

Upon successful initialization (may take few seconds for each DF1), a small button
with label "led" will appear. Use this button to light up the red LED, and identify
your desired device in presence of multiple DF1's.

