import logging
import azure.functions as func

# Intentionally fake test secrets for scanner validation only
API_KEY = "1234567890abcdef1234567890abcdef"
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
password = "admin123"
connection_string = "Server=tcp:test.database.windows.net,1433;Initial Catalog=demo;User ID=demo;Password=P@ssw0rd123!"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    return func.HttpResponse("Hello from Azure Function", status_code=200)
