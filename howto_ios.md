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
  Simply press anywhere in the box showing your DF1 to go into the detailed view.

  It will take couple of seconds to discover remaining services and characteristics for
  the device. A progress HUD will show until this is done.

  <img src=pics/app_detail_view.png width=250>

  Keep an eye on your DF1. You'll notice that the green light will blink once and then
  blue light will start flashing every 5 seconds or so. The green light is to indicate that
  subscription to notification handle is successful. The blue light blinks whenever the accelerometer
  is turned on and in active state.

  <img src=pics/app_detail_view_data2.png width=250>

  The line chart on the top cell will start updating. The XYZ data from DF1 is reported at 5Hz.
  Thus, you are getting acceleration updates from DF1 every 200 milliseconds.  

  You'll also notice that the second cell shows tap events. Try tapping DF1 on the top surface.
  The motion detection feature inside of DF1's accelerometer should differentiate taps from other
  movements. It will send 1 byte of event notification to the app each time tap is detected.

  Lastly, the battery level is reported. The notification will be sent only when the internal
  readings change.


3. **Configuration View**

  The current demo app is only scratching the surface of DF1's features. Each data generating
  notification handle has other associated configuration parameters. For example, it's possible
  to change the tap threshhold setting, so that it requires user to tap more firmly for an event
  to be generated.

  The purpose of the configuration view is to persist these settings per DF1 device. In addition
  to accelerometer parameters, it should associate each unique device to other user preferences
  such as custom name, alert behavior, last known gps location, etc...

  You can currently change the name of the device. This way, you can associate the device's unique
  UUID to a name you can recognize on your app. It's recommended that you change the name of your
  device right away, so you don't confuse it with other DF1's in the vicinity.

  <img src=pics/app_config2.png width=250>

  As of this writing (2014.09.05), the config view is only partially implemented.
  You can inspect the source code to see how things are structured, and contributors are definitely
  welcome!
