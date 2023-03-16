# Real-Time Flights API Python SDK

## Installation

You can install Real-Time Flights API Python SDK with pip.

```bash
pip install real_time_flights_api
```

### Making the GET request

```python
>>> from real_time_flights_api import FlightLabsClient

>>> client = FlightLabsClient(access_key='REPLACE-WITH-YOUR-ACCESS-KEY')

>>> response = client.get_flights()