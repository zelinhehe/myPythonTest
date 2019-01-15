class myDecorator(object):
 
    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn
 
    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"
 

#@myDecorator
def aFunction():
    print "inside aFunction()"

aFunction = myDecorator(aFunction)
 
print "Finished decorating aFunction()"
 
aFunction()
