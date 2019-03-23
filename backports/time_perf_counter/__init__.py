import time


__all__ = ['perf_counter']


try:
    perf_counter = time.perf_counter

except AttributeError:          # Python < 3.3
    import sys

    from monotonic import monotonic

    if sys.platform.startswith('win32'):
        import ctypes
        from ctypes.windll import kernel32
        import ctypes.util

        QueryPerformanceFrequency = kernel32.QueryPerformanceFrequency
        QueryPerformanceCounter = kernel32.QueryPerformanceCounter

        def _win_perf_counter():
            out = ctypes.c_longlong()
            outref = ctypes.byref(out)

            if _win_perf_counter.freq is None:
                QueryPerformanceFrequency(outref)
                _win_perf_counter.freq = float(out.value)

                QueryPerformanceCounter(outref)
                _win_perf_counter.t0 = out.value

            QueryPerformanceCounter(outref)
            return (out.value - _win_perf_counter.t0) / _win_perf_counter.freq

        _win_perf_counter.frequency = None

    def perf_counter():
        """
        perf_counter() -> float

        Performance counter for benchmarking.
        """
        if perf_counter.use_performance_counter:
            try:
                return _win_perf_counter()
            except OSError:
                perf_counter.use_performance_counter = False

        if perf_counter.use_monotonic:
            try:
                return monotonic()
            except OSError:
                perf_counter.use_monotonic = False

        return time.time()

    perf_counter.use_performance_counter = sys.platform.startswith('win32')
    perf_counter.use_monotonic = True  # ``monotonic`` is definitely defined
