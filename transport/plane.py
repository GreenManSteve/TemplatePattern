from transport.abs_transport import AbsTransport


class Plane(AbsTransport):
    def start_engine(self):
        print("Start Turbines...")

    def leave_terminal(self):
        print("Leaving terminal")

    def travel_to_destination(self):
        print("We will be landing at {} airport".format(self._destination))

    def entertainment(self):
        print("Inflight movies")

    def arrive_at_destination(self):
        print("Arriving at {}".format(self._destination))