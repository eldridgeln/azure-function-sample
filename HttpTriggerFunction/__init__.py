import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function received a request.")

    # Parse name from query string or request body
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get("name", "World")

    # Parse optional action
    action = req.params.get("action", "greet")

    if action == "greet":
        response_payload = {
            "message": f"Hello, {name}!",
            "status": "success"
        }
        return func.HttpResponse(
            body=json.dumps(response_payload),
            mimetype="application/json",
            status_code=200
        )

    elif action == "echo":
        try:
            body = req.get_json()
        except ValueError:
            body = {}
        return func.HttpResponse(
            body=json.dumps({"echo": body}),
            mimetype="application/json",
            status_code=200
        )

    else:
        return func.HttpResponse(
            body=json.dumps({"error": f"Unknown action: {action}"}),
            mimetype="application/json",
            status_code=400
        )
