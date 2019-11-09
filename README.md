# Postman

Postman is a module to enable communication between the different computes 
inside the BRHUE Robot. Postman can send any amount of integers or floating 
point numbers through sockets.

# Usage
## Server
To use the server run

```python
from postman import server

def callback(data):
    """
    Do whatever you want with the data. data is either, a list of ints or a
    list of floats
    """
    ### Code ###


with server.Server as s:
    s.connect(callback) # Connects to client and call callback on new data
```

## Client
To use the client run
```python
from postman import client

c = client.Client()

def data_generator():
    data = ... ### Code creates data ###
    c.send_data(data) # send data to host
```