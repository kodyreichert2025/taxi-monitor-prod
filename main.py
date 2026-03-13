import os
import time
import random
from flask import Flask, Response, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "taxi_requests_total",
    "Total number of taxi requests received"
)

PREDICTION_COUNT = Counter(
    "taxi_predictions_total",
    "Total successful taxi predictions"
)

FAILURE_COUNT = Counter(
    "taxi_prediction_failures_total",
    "Total failed taxi prediction requests"
)

REQUEST_LATENCY = Histogram(
    "taxi_request_latency_seconds",
    "Taxi request latency in seconds"
)

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    start = time.time()

    try:
        # simulate a prediction request
        time.sleep(random.uniform(0.1, 0.5))
        PREDICTION_COUNT.inc()

        return jsonify({
            "status": "ok",
            "prediction": 0
        })

    except Exception:
        FAILURE_COUNT.inc()
        return jsonify({"status": "error"}), 500

    finally:
        REQUEST_LATENCY.observe(time.time() - start)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

 
 