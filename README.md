![Build Status](https://elbag.net/wp-content/uploads//arduino-logo-1024x259.png)
![Build Status](https://geekflare.com/wp-content/uploads/2019/07/fast-api-logo.png)

## Getting Started

##### Install the python libs

```console
pip install fastapi uvicorn pyserial
```

##### We flash the Arduino microcontroller with firmware from the Arduino folder

##### We assemble the electrical circuit according to the scheme:

![Build Status](https://i.ibb.co/VH7FH1p/photo-2022-12-08-14-46-58.jpg)

## Launch

##### Open the FastAPI folder from the terminal and start the web server

```python
uvicorn main:app --reload
```

## Using

##### We make a request using the GET method at http://127.0.0.1:8000/arduino/light-level and get a response with a body, example:

```json
{
    "level": 922,
    "type": "dark"
}
```
