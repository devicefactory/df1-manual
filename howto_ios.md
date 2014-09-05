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

1. **Starting the App**

  Currently, the demo app can:
  
  * scan and discover DF1 devices
  * subscribe to battery level notifications
  * subscribe to 8 bit XYZ data
  * subscribe to tap event data
  * toggle LED
  * associate user assigned name to a device
  
  The TODO list for this demo app is perhaps more numerous than the existing features.
  They will be listed at the end of this tutorial.
  
  When you first open up the app, it will try to scan for nearby DF1's.
  The scanning will timeout after couple of seconds. In order to manually initiate scanning,
  slowly swipe vertically down the screen (pulldown). You'll see the progress wheel
  appear to indicate that the scanning has been initiated.
  
  <img src=pics/app_scan.png width=250>
  
  If you have DF1 in detectible range, you'll see each distinct DF1's show up 
  as a box like so:
  
  <img src=pics/app_discover.png width=250>
  
  When it detects DF1 device, the app will additionally connect to the device and carry
  out the following operations:
  
  * requests for RSSI (signal strength) updates every 2 seconds
  * discover subset of service characteristics
  * provide Red LED toggle button upon initialization
  
  Upon successful initialization (may take few seconds for each DF1), a small button
  with label "led" will appear. Use this button to light up the red LED on DF1, and identify
  your desired device in presence of multiple DF1's.
  
  <img src=pics/app_scan_initialized.png width=250>
  
  In addition, a small bar indicating the signal strength will be shown.
  Try putting the device close to the phone and moving it far away. You'll
  see the RSSI value and the bar indicator change accordingly.


2. **Detailed View**

  Now that we can scan and discover our DF1, let's try to get some data off of it.
