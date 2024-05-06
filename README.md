# g24f2-control
A small python script to control brightness and contrast of Gigabyte G24F2 monitor in Linux. The OSD Sidekick software which controls the various settings of this monitor is only available for Windows. I wanted to do something similar using Linux as well. So here is my little try to make it work with Linux as well.

# How to
1. Copy 99-99-g24f2.rules to /etc/udev/rules.d/

2. Give exec perms
chmod +x ./g24f2.py

3. Execute using two params: 1 - brightness, 2 - contrast
./g24f2.py 15 65

# TODO
Might add more configurations in future with proper args parsing.

# How it works
Sniffed the USB packets that were being transmitted using Wireshark in Windows. Decoded the values. It uses USB control endpoint (EP 0) for configuration. Python's py-usb takes care of most of the low level USB settings, so simply using dev.ctrl_transfer() function will transfer the data. The first four parameters are the bmRequestType, bmRequest, wValue and wIndex (https://github.com/walac/pyusb/blob/master/docs/tutorial.rst).
