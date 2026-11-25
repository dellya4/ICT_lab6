import json

from lambda_function import lambda_handler


def make_event(
    method,
    path,
    body=None
):
    return {
        "rawPath": path,
        "body": (
            json.dumps(body)
            if body is not None
            else None
        ),
        "requestContext": {
            "http": {
                "method": method
            }
        },
    }


def test_time_returns_200_and_time():
    r = lambda_handler(
        make_event(
            "GET",
            "/time"
        ),
        None
    )

    assert r["statusCode"] == 200

    body = json.loads(r["body"])

    assert "time" in body


def test_echo_returns_message():
    r = lambda_handler(
        make_event(
            "POST",
            "/echo",
            {
                "message": "hello"
            }
        ),
        None
    )

    assert r["statusCode"] == 200

    body = json.loads(r["body"])

    assert body["reply"] == "hello"


def test_echo_without_message_returns_400():
    r = lambda_handler(
        make_event(
            "POST",
            "/echo",
            {}
        ),
        None
    )

    assert r["statusCode"] == 400


def test_invalid_json_returns_400():
    event = {
        "rawPath": "/echo",
        "body": "{invalid json}",
        "requestContext": {
            "http": {
                "method": "POST"
            }
        },
    }

    r = lambda_handler(
        event,
        None
    )

    assert r["statusCode"] == 400


def test_echo_empty_string():
    r = lambda_handler(
        make_event(
            "POST",
            "/echo",
            {
                "message": ""
            }
        ),
        None
    )

    assert r["statusCode"] == 200

    body = json.loads(r["body"])

    assert body["reply"] == ""


def test_unknown_path_returns_404():
    r = lambda_handler(
        make_event(
            "GET",
            "/unknown"
        ),
        None
    )

    assert r["statusCode"] == 404