import json
from datetime import datetime


def response(status, payload):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(payload),
    }


def lambda_handler(event, context):
    http = event.get(
        "requestContext", {}
    ).get("http", {})

    method = http.get("method")
    path = event.get("rawPath")

    if method == "GET" and path == "/time":
        return response(
            200,
            {
                "time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }
        )

    if method == "POST" and path == "/echo":
        try:
            data = json.loads(
                event.get("body") or "{}"
            )

        except json.JSONDecodeError:
            return response(
                400,
                {
                    "error": "invalid JSON"
                }
            )

        if "message" not in data:
            return response(
                400,
                {
                    "error": "field 'message' is required"
                }
            )

        if not isinstance(
            data["message"],
            str
        ):
            return response(
                400,
                {
                    "error": "field 'message' must be a string"
                }
            )

        return response(
            200,
            {
                "reply": data["message"]
            }
        )

    return response(
        404,
        {
            "error": "not found"
        }
    )