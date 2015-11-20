import spidev

CE=0
spi = spidev.SpiDev()
spi.open(0,CE)
threshold = 48

def judgePotensionmeter():

    while(True):
        retspi = spi.xfer2([0x68,0x00])

        if( (retspi[0]*256+retspi[1]) & 0x3ff >= threshold ):
            print("success")
        else:
            print("failure ")

if __name__ == "__main__":
    judgePotensionmeter()
