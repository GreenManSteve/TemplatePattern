from transport.bus import Bus
from transport.plane import Plane

def main():
    travel("New York", Plane)

def travel(destination, transport):
    print("Travelling to {} via {}".format(destination, transport.__name__))
    means = transport(destination)
    means.take_tripe()

if __name__ == '__main__':
    main()