def decorate_C(function):
    def wrap_function(*args, **kwargs):
        print 'before: {}'.format(function.__name__)
        return function(*args, **kwargs)
    return wrap_function
 
class Printer:
    @decorate_C
    def print_message(self, *args, **kwargs):
        print 'message'
 
p = Printer()
p.print_message()
