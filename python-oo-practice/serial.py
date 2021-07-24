"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        '''Make a new generator, starting at start'''
        self.start = self.next = start

    def __repr__(self):
        '''Show representation'''
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        '''Return next serial'''
        self.next += 1
        return self.next - 1

    def reset(self):
        '''Reset the number to the original start'''
        self.next = self.start


if __name__ == '__main__':
    help(SerialGenerator.generate)

    serial = SerialGenerator(start = 100)
    print(serial.generate())
    print(serial.generate())
    print(serial.generate())
    serial.reset()
    print(serial.generate())
    print(serial.__repr__())

