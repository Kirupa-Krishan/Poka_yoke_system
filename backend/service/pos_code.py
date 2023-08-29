from mfrc522 import MFRC522 
import utime

#Use MQTT to transfer data to server

from machine import Pin

RLed =Pin(18,Pin.OUT)
GLed =Pin(19,Pin.OUT)
RLed.value(0)
GLed.value(0)
# Create a map between keypad buttons and characters
matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]
# PINs according to schematic - Change the pins to match with your connections
keypad_rows = [15,14,13,12]
keypad_columns = [11,10,9,8]
# Create two empty lists to set up pins ( Rows output and columns input )
col_pins = []
row_pins = []
guess = []
#our secret pin, shhh do not tell anyone
secret_pin = ['7','6','7','2','0','0']
for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    
##############################Scan keys ####################
def scankeys():
    for row in range(4):
        for col in range(4): 
            row_pins[row].high()
            key = None
            if col_pins[col].value() == 1:
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                utime.sleep(0.3)
                guess.append(key_press)
               
                
            if len(guess) == 6:
                checkPin(guess)
                
                for x in range(0,6):
                    guess.pop() 
                    
        row_pins[row].low()
##############################To check Pin #################
def checkPin(guess):
    if guess == secret_pin:
        print("You got the secret pin correct")
        GLed.value(1)
        utime.sleep(3)
        GLed.value(0)
    else:
        def uidToString(uid):
            mystring = ""
            for i in uid:
                mystring = "%02X" % i + mystring
            return mystring                  
        rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
        print("")
        print("Place the RFID Card")
        print("")
        while True:
            (stat, tag_type) = rc522.request(rc522.REQALL)
            if stat == rc522.OK:
                (status, raw_uid) = rc522.SelectTagSN()
                if stat == rc522.OK:
                    rfid_data = "{:02x}".format(raw_uid[0])
                    print("Card detected! UID: {}".format(rfid_data))
                    if rfid_data == "53":
                        GLed.value(1)
                        utime.sleep(5)
                        GLed.value(0)
                    else:
                        RLed.value(1)
                        utime.sleep(1)
                        RLed.value(0)
print("Enter the secret Pin")
def PokaYokeSystem():
    while True:
        scankeys()
