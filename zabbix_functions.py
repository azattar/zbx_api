#!/usr/bin/python

import requests

def zbx_get_auth(url, login, passwd):
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": login,
            "password": passwd
        },
        "id": 1,
    }
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    output = response.json()
    return output['result']


def zbx_get_group_triggers(url, token, groupName):
    payload = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "group": groupName,
        "output": "extend",
        "selectFunctions": "extend"
        },
    "auth": token,
    "id": 1
    }
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    output = response.json()
    return output['result']


def zbx_get_host_triggers(url, token, hostName):
    payload = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "host": hostName,
        "output": "extend",
        "selectFunctions": "extend",
        #"expandExpression": "true",
        "expandDescription": "true",
        #"expandComment": "true",
        },
    "auth": token,
    "id": 1
    }
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    output = response.json()
    return output['result']


def zbx_get_trigger_status(url, token, Triggerid):
    payload = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "triggerids": Triggerid,
        "output": "extend",
        "selectFunctions": "extend"
        },
    "auth": token,
    "id": 1
    }
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    output = response.json()
    return output['result'][0]['status']

def zbx_get_host_id(url, token, host_name):
    print("colocar algo aqui")