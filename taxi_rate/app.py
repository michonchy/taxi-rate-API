import json
import json
from typing import List

# import requests
# 初乗り料金が1700mまで610円、それ以降は313mごとに80円のタクシーがある。
# このタクシーに乗った距離をm単位で入力し、料金を計算するプログラムを作成せよ。
class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def is_taxi_rate(x):
    r  = x-1700
    a = r//313
    t =r%313

    if 0 == t:
        return 610+(80*a)
    else:
        return 610+80+(80*a)





def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = number(n)
        n = is_taxi_rate(n)
        print(n)
    except:
        return{
        "statusCode": 400,
        "headers":{
            "Content-Type": "application/json"
        },
        "body":json.dumps({
            "message":"整数値を入力してください。"
        }),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
