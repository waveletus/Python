import sys

class Calculator:
    def __init__(self, n):
        self.num = n

    def square(self):
        return self.num * self.num


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()

def test():
    calculator = Calculator(12)
    print(calculator.square())

if __name__ == "__main__": main()