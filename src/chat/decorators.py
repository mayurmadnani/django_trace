def track_mem(function):
    import tracemalloc
    # Do before the func call
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()
    def wrap(request, *args, **kwargs):
        return function(request, *args, **kwargs)
    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    print("[ Top 10 differences ]")
    for stat in top_stats[:10]:
        print(stat)
    # Do after the func call
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap