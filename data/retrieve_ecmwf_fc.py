from ecmwf.opendata import Client

# Create a client
client = Client(source="ecmwf")

# Retrieve temperature (2t) and total precipitation (tp)
result = client.retrieve(
    type="fc",
    stream="oper",
    param=["2t", "tp"],
    step=[0, 24, 48, 72],  # Forecast steps in hours
    target="ecmwf_forecast.grib2"
)

print(f"Forecast data retrieved for: {result.datetime}")
