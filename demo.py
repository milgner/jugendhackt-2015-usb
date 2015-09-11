import usb.core
import sys

# find keyboard
dev = usb.core.find(idVendor=0x046d, idProduct=0xc31f)
if dev is None:
  raise ValueError('Keyboard not found')

# check whether we want to switch or reset the keys
# default is to switch to regular behaviour
reset = (len(sys.argv) >= 2 and sys.argv[1] == '-r')
wIndex = 0 if reset else 1

# send the command: tada!
dev.ctrl_transfer(0x40, 2, 0x001a, wIndex, None, 100)
