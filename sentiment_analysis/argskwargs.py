#!/usr/bin/python

class ArgsKwargs:
    def __init__(self, *args, **kwargs):
        self.arg = []
        self.kwarg = {}
        for arg in args:
            self.arg.append(arg)
        
        for key,val in kwargs.items():
            self.kwarg[key] = val
        
    
    def testArgsInMethod(self, *args, **kwargs):
        for arg in args:
            self.arg.append(arg)

        for key,val in kwargs.items():
            self.kwarg[key] = val

    def toString(self):
        print self.arg, self.kwarg


def main():
    test = ArgsKwargs('a', 1, 'b', 2, val1=1, val2=2, val3=3)
    test.toString()
    test.testArgsInMethod('c',3,'d',4,val4=4,val5=5,val6=6)
    test.toString()

if __name__ == '__main__':
    main()