import time

# Import Tracer
from lib.tracing import Tracer

# Create Tracer Instance
otel_tracer = Tracer("Demo 4", "localhost:4317", True)

# Trace Function
@otel_tracer.trace_function
def add(a, b):
    time.sleep(0.5)
    return a + b

# Trace Function
@otel_tracer.trace_function
def subtract(a, b):
    time.sleep(0.3)
    return a - b

def main():
    # Trace Root
    with otel_tracer.tracer.start_as_current_span("main") as _:
        result1 = add(2, 3)
        result2 = subtract(5, 2)
        print("Result of add:", result1)
        print("Result of subtract:", result2)

if __name__ == "__main__":
    main()
