# About

Evaluates performance for LLM-apps by using [Locust](https://locust.io/)

# Setup

```
python3 -m venv perf-tests-venv
source perf-tests-venv/bin/activate
python3 -m pip install locust
locust -V
```

# Usage

1- Run locust
```
# If chat endpoint requires authentication.
API_TOKEN=<TOKEN> locust -f chatbot_locustfile.py

# Otherwise.
locust -f chatbot_locustfile.py
```

2- Open http://localhost:8089 and set:
* Users=100
* Ramp Up Users=10
* Chat endpoint URL. Eg: http://0.0.0.0:8080/v1/query/
* Run Time: 60s

3- Monitor and Analyze Results
* Response Time: How quickly are we getting answers
* Success Rate: How often are we hitting the mark versus crashing and burning
* Throughput: How many requests are we churning through per second

# Headless run

```
# Set the API_TOKEN env, if necessary.
locust -f chatbot_locustfile.py --headless --users 10 --spawn-rate 1 --run-time 60s -H http://0.0.0.0:8080/v1/query/
```