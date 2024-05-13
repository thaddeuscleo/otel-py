import opentelemetry.trace as trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


class Tracer:
    def __init__(
        self, svc_name: str, oltp_endpoint: str, insecure_endpoint: bool
    ) -> None:
        resource = Resource(attributes={SERVICE_NAME: svc_name})

        otlp_exporter = OTLPSpanExporter(
            endpoint=oltp_endpoint, insecure=insecure_endpoint
        )

        traceProvider = TracerProvider(resource=resource)
        span_processor = BatchSpanProcessor(otlp_exporter)
        traceProvider.add_span_processor(span_processor)
        trace.set_tracer_provider(traceProvider)
        self.tracer = trace.get_tracer(__name__)
        pass

    def trace_function(self, func):
        def wrapper(*args, **kwargs):
            with self.tracer.start_as_current_span(func.__name__):
                return func(*args, **kwargs)

        return wrapper
