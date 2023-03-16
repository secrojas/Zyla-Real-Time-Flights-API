# Real-Time Flights API Python SDK

[Real-Time Flights API](https://www.goflightlabs.com/) is a powerful REST API for real-time flight status and tracking information. Live data for flights, airports, schedules, timetables, IATA codes, and more.

## Installation

You can install Real-Time Flights API Python SDK with pip.

```bash
pip install real_time_flights_api
```

## Usage

The Real-Time Flights API Python SDK is a wrapper around the [requests](https://docs.python-requests.org/en/master/) library. Real-Time Flights API supports a GET request for now.

Signup to FlightLabs to [get your API key](https://app.goflightlabs.com/register) and some credits to get started.

### Making the GET request

```python
>>> from real_time_flights_api import FlightLabsClient

>>> client = FlightLabsClient(access_key='REPLACE-WITH-YOUR-ACCESS-KEY')

>>> response = client.get_flights()
```

You can find all the documentation on [FlightLabs documentation](https://app.goflightlabs.com/dashboard).

## Screenshot

Here a little exemple on how to get the data of flights

```python
>>> from real_time_flights_api import FlightLabsClient

>>> access_key = 'REPLACE-WITH-YOUR-API-KEY'

>>> client = FlightLabsClient(access_key)

>>> response = client.get_flights()
```
