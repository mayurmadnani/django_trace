from django.utils.deprecation import MiddlewareMixin

class TraceBackMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        from pprint import pprint
        import traceback
        import sys
        import inspect
        print(exception.__class__.__name__)
        exc_info = sys.exc_info()
        if hasattr(exception, 'message'):
            print(exception.message)
        else:
            pprint(exception)
        traceback.print_exception(*exc_info)
        print("Is the error")
        # import ipdb; ipdb.set_trace();
        # tb = sys.exc_info()[2]
        print(inspect.trace()[-1][0].f_locals)
        local_variables = inspect.trace()[-1][0].f_locals
        trace = Bunch(local_variables)
        import ipdb; ipdb.set_trace();
        return None


class Bunch(object):
  def __init__(self, adict):
    self.__dict__.update(adict)

