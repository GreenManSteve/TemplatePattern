from transport.abs_transport import AbsTransport


class Bus(AbsTransport):
    def start_engine(self):
        print("Bus engine starting")

    def travel_to_destination(self):
        print("Next stop on this bus journey is {}".format(self._destination))