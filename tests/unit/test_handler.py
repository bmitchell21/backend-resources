import boto3
import unittest
import pytest
import json
import requests

dynamodb_table_info = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb_table = dynamodb_table_info.Table('Res2Counter')

def test_of_func():
    response = requests.get("https://4u2lic1984.execute-api.us-east-1.amazonaws.com/Prod/vCount")
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

