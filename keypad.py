import RPi.GPIO as io
import time
import urllib
import urllib2

#constans
KEYPAD = [["1","2","3"],["4","5","6"],["7","8","9"],["*","0","#"]]
COLUMNS = [10,11,12]
ROWS = [3,5,7,8]

#variables
countDigits = 0
code = ""

def checkKey(row, column):
    global countDigits
    global code
    io.setup(ROWS[row], io.IN)
    if not io.input(ROWS[row]):
        if KEYPAD[row][column] == "#":
            countDigits = 0
            code = ""
        else:
            countDigits = countDigits + 1
            code = code + KEYPAD[row][column]
        print code
    io.setup(ROWS[row], io.OUT)
    return

def checkRows(column):
    if column == 0:
        for i in range(0,4):
            checkKey(i, column)
    elif column == 1:
        for i in range(0,4):
            checkKey(i, column)
    elif column == 2:
        for i in range(0,4):
            checkKey(i, column)
    return

def request(code):
    product = "apartamento"
    url = "http://internetdelascosas.freeiz.com/test.php"
    values = {'product' : product, 'code' : code}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request).read()
    response = response.find("access");
    return response

#main program
io.setmode(io.BOARD)
io.setwarnings(False)

#setting up pins
for i in range(0,3):
    io.setup(COLUMNS[i], io.OUT)
    io.output(COLUMNS[i], True)

for i in range(0,4):
    io.setup(ROWS[i], io.OUT)
    io.output(ROWS[i], True)

io.setup(13, io.OUT)
io.output(13, False)

while True:
    for i in range(0,3):
        io.output(COLUMNS[i], False)
        checkRows(i)
        io.output(COLUMNS[i], True)
        if countDigits == 6:
            if request(code) > -1:
                io.output(13, True)
                print "access confirmed"
                time.sleep(0.1)
                io.output(13, False)
            else:
                print "access denied"
            countDigits = 0
            code = ""
            
        time.sleep(0.1)
