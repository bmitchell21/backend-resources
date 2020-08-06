import boto3
import unittest
import pytest

dynamodb_table_info = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb_table = dynamodb_resource.Table('Res2Counter')
dynamodb_get_request = dynamodb_table.get_item(
    Key = {'Res2Counter': 'number'}
    ProjectiExpression = 'Visits'
    )
    
table_response = dynamodb_response.get('Item')

def test_of_func():
    response = requests.get("https://4u2lic1984.execute-api.us-east-1.amazonaws.com/Prod/vCount")
    assert response.status_code == 200

def test2_of_func():
    assert type(table_response) == int and table_response >= 0
