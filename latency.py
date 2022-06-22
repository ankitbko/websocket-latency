from datetime import datetime
import json


def measure_latency(func):
    def wrapper_measure_latency(*args, **kwargs):
        message = json.loads(args[1])
        _self = args[0]
        if message["type"] == "ack":
            print(f"Recieved message: {message}")
            message["server_ack_ts"] = str(datetime.now().timestamp())
            _self.write_message(json.dumps(message))
        func(*args, **kwargs)
        return

    return wrapper_measure_latency
