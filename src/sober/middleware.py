from django.utils.deprecation import MiddlewareMixin

class TraceBackMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        import traceback
        import ipdb; ipdb.set_trace();
        print(exception.__class__.__name__)
        print(exception.message)
        print("Is the error")
        return None