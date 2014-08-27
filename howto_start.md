# Getting Started

You've just gotten DF1 in your hands and wondering what you can do with it?
There are tons of things you can do.

![Rear Battery](https://raw.githubusercontent.com/devicefactory/share/master/media/df1/df1-rear-battery-door.png)

Here's a highlevel overview of the features:

* Accelerometer capable of 2/4/8g acceleration detection in both 8 or 14 bit resolution
* Motion detection such as tap, shake, freefall.
* Easily replaceable battery
* Idle battery life >1 year. Active use battery life 2-3 months.
* Antenna range : 150 - 250ft line of sight (subject to effects from surroundings)
* Upgradeable firmware over the air



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

Most of these apps will first discover and represent the BLE device in the following object hierarchy:

```
>
>  Device --->  Service1  --->  Characteristic1  --->  Read/Write
>                               Characteristic2  --->  Read/Notification
>                               ...
>               Service2  --->  Characteristic1  --->  Read/Notification
>                               ...
>                ...    
```


That said, trying downloading any one of these free apps.

* [TI BLE Multitool](https://itunes.apple.com/us/app/ti-ble-multitool/id580494818?mt=8)
* [LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8)

When you "scan" for the devices, our DF1 should show up.
[LightBlue](https://itunes.apple.com/us/app/lightblue-bluetooth-low-energy/id557428110?mt=8) will also allow you to
browse the contents of DF1. It will discover list of services and their associated characteristics.


## Light Me Up!

For fun, let's try to toggle the RGB LED inside of DF1.


