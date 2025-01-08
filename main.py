from waggle.plugin import Plugin
from serial import Serial
import re

pattern = r'\{wind: (\d+) (\d+) \((\d+) (\d+) (\d+)\)\}'

def main():
    with Plugin() as plugin, Serial("/dev/cu.usbmodem2101", baudrate=9600) as dev:
        dev.readline()
        while True:
            data = dev.readline()
            tokens = data.split()
            plugin.publish('davis6410.wind.speed', int(tokens[1]))
            plugin.publish('davis6410.wind.direction', int(tokens[2]))
            plugin.publish('davis6410.debug.iteration', int(tokens[3]))
            plugin.publish('davis6410.debug.rawtops', int(tokens[4]))
            plugin.publish('davis6410.debug.rawpots', int(tokens[5]))        

if __name__ == "__main__":
    main()
