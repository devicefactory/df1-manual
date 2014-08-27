# Getting Started

You've just gotten DF1 in your hands and wondering what you can do with it?
There are tons of things you can do.

![Rear Battery](https://raw.githubusercontent.com/devicefactory/share/master/media/df1/df1-rear-battery-door.png)

Here's a highlevel overview of the features:

* Fully realized device that's open source!
* Accelerometer capable of 2/4/8g acceleration detection in both 8 or 14 bit resolution
* Motion detection such as tap, shake, freefall.
* Easily replaceable battery
* Idle battery life >1 year. Active use battery life 2-3 months.
* Antenna range : 150 - 250ft line of sight (subject to effects from surroundings)
* Upgradeable firmware over the air
* RGB LED
* FCC Certified
* High-quality injection molded plastic enclosure


## Discovering What's Inside

First a bit of glossary:
  
| Term            | Description                                                                           |
|:--------------  |:------------------------------------------------------------------------------------- |
| BLE             | Bluetooth Low Energy, otherwise known as Bluetooth Smart, Smart Ready.                |
| Central         | Device associated with scanning and discovering other BLE devices.                    |
| Peripheral      | Device that is discoverable - it advertises and serves data.                          |
| Services        | A unit representing logical grouping of Characteristics.                              |
| Characteristics | Data generating "slots". Think of them as drawers from which you can retrieve values. |

Let's first discover the device using an iPhone / iPod.
There are various BLE apps on the appstore that can easily discover any BLE capable peripherals.

* [TI BLE Multitool](https://itunes.apple.com/us/app/ti-ble-multitool/id580494818?mt=8)
* [LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8)

For this tutorial, let's try using 
[LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8) app.

Most of the BLE browser apps will first discover the device and allow you to select it.
Once the device is selected, the capabilities of the device is presented in the following object
hierarchy:

```
>
>  Device --->  Service1  --->  Characteristic1  --->  Read/Write
>                               Characteristic2  --->  Read/Notification
>                               ...
>               Service2  --->  Characteristic1  --->  Read/Notification
>                               ...
>                ...    
```

When you "scan" for the devices, our DF1 should show up.
[LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8) will also allow you to
browse the contents of DF1. It will discover list of services and their associated characteristics.

You'll notice that these services exist in DF1:


| Service                           | Description
| :-------------------------------- |:-------------------------------------------------------------------------------------
| Device Information Service        | Contains the device name, firmware, hardware versions.
| Battery Service                   | Allows notification of battery levels.
| Acceleration Service (UUID: AA10) | Various "nobs and buttons" to configure the features of the accelerometer. The accelerometer we are using is the top-of-the-line low g accelerometer from Freescale: [MMA8451Q](http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MMA8451Q).
| Test Service (UUID: AA60)         | Allows toggle of LED's
| OAD Service (custom)              | Only used for over-air-update.
 
![DF Services on LightBlue App](https://raw.githubusercontent.com/devicefactory/df1-manual/master/pics/lightblue_df1_top.png)

## Light Me Up!

For fun, let's try to toggle the RGB LED inside of DF1.
For this, you will need to:

1. Find Service `0xAA60`
2. Under that service, find Characteristic `0xAA62`
3. Write hex value `01` into that characteristic

The screenshot should look like the following. Scroll to the section where it says "write value".

<img src=https://raw.githubusercontent.com/devicefactory/df1-manual/master/pics/lightblue_testuuid.png width=200>

Enter `01` as the hexvalue. You'll see the red LED light up!
Enter `02` next. You'll see the green LED.
Enter `04` afterwards. Finally, the blue LED will light up.
Lastly, enter `00` to turn off the LED.

