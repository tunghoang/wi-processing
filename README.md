# wi-processing
WI processing service

Documentation: https://docs.google.com/spreadsheets/d/16A8tmHxTxgT83Ig8RFASakzpkh7QacWU7PhISaSFhC4/edit?usp=sharing

## Requirement
- python 2.7

## Installation
Using the command: pip install -r requirements.txt

Download [alglib](http://www.alglib.net/translator/re/alglib-3.12.0.cpython.free.zip) and follow the manual to install alglib

## Running the service
python main.py

## Functions provided by the service
- Convolutional
- Deconvolutional
- ...

## Config to get tokens
When deploying, you must reset the parameters in the config file to ensure the security of service. This file includes:
- SECRET_KEY: key to generate tokens
- NAME: name of the user had permission to access this service.
- PASSWORD: password of this user.
- ID: id of this user.

## How to use
In this section, we use the curl command to give examples how to use this service

1. First of all, you need get the token from the service by your username and password:
```
curl -H "Content-Type: application/json" -X POST -d '{"username":"your_username","password":"your_password"}' http://your_domain/auth
```
2. After this command, the service will provide a json file contained a token:
```
{
  "access_token": "your_token"
}
```

3. To use this token for requesting functions, you have to change it a bit to the form "JWT your_token" and put it into a header. The header of the next request seems like:
```
{"Authorization": "JWT your_token"}
```

4. Now, you can request the service to use functions:
- Convolutional:
```
curl -H "Authorization": "JWT your_token" -X POST -d '{'refCurve': [0.1, 1.2, 2.3, 3.4], 'curve': [1.1, 2.2, 3.3, 4.4]}' http://your_domain/convolution
```
- Deconvolutional:
```
curl -H "Authorization": "JWT your_token" -X POST -d '{'signal': [2, 1], 'divisor': [0, 1, 0, 0, 1, 1, 0, 0]}' http://your_domain/deconvolution
```
