
import serial.tools.list_ports, simple_ui, filecreat, keyboard

# < all globals >

ports = serial.tools.list_ports.comports(); serialinst = serial.Serial()

allports = []

on = True
portselect = 17
baundselect = 9600

# < for loops >

for onePort in ports:
    allports.append(str(onePort))

for i in range(0,len( allports)):
    if allports[i].startswith("COM" + str(portselect)):
        portvar = "COM" + str(portselect)

# < set conffig >

serialinst.baurate = baundselect
serialinst.port = portvar
serialinst.open()

# < file txt ui >

nome = simple_ui.baseui("3", "nome do arquivo", 30)
path = simple_ui.baseui("3", "nome do caminho", 30)

# < file creat >

filecreat.makeafile(nome)

# < moin loop >

while not(keyboard.read_event() == "e"):

    #if keyboard.read_key() == "e": # on = False
    
    if serialinst.in_waiting:
        packet = serialinst.readline()
        outputdata = packet.decode('utf-8')
        filecreat.readfile(nome, outputdata)

filecreat.moveafile(path, nome)

# <https://www.youtube.com/watch?v=AHr94RtMj1A>