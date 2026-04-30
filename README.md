# Sample Azure HTTP Trigger Function (Python)

A simple Python Azure Function with an HTTP trigger, structured for local Aqua Security scanning.

## Project Structure

```
azure-function-sample/
├── HttpTriggerFunction/
│   ├── __init__.py          # Main function logic
│   └── function.json        # Binding configuration
├── host.json                # Host-level configuration
├── local.settings.json      # Local dev settings (not deployed)
├── requirements.txt         # Python dependencies
├── function-permissions.json # IAM role permissions (for Aqua scanning)
└── README.md
```

## Endpoints

| Method | Route         | Params                        | Description              |
|--------|---------------|-------------------------------|--------------------------|
| GET    | /api/hello    | `?name=YourName`              | Returns a greeting       |
| GET    | /api/hello    | `?name=YourName&action=greet` | Same as above            |
| POST   | /api/hello    | JSON body with `name`         | Returns a greeting       |
| GET    | /api/hello    | `?action=echo`                | Echoes the request body  |

## Running Locally (Azure Functions Core Tools)

```bash
# Install dependencies
pip install -r requirements.txt

# Start the function locally
func start
```

## Aqua Security Scanning

### Basic scan (without permissions check)
```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /<path-to>/azure-function-sample/:/tmp/azure-function-sample/ \
  registry.aquasec.com/scanner:latest-saas scan \
  -H https://<ENVIRONMENT_ID>.cloud.aquasec.com \
  -A <SCANNER_TOKEN> \
  --code-scan /tmp/azure-function-sample/ \
  --html --htmlfile /tmp/scanresult.html
```

### Scan with permissions analysis (detects excessive IAM permissions)
```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /<path-to>/azure-function-sample/:/tmp/azure-function-sample/ \
  registry.aquasec.com/scanner:latest-saas scan \
  -H https://<ENVIRONMENT_ID>.cloud.aquasec.com \
  -A <SCANNER_TOKEN> \
  --code-scan /tmp/azure-function-sample/ \
  --function-permissions /tmp/azure-function-sample/function-permissions.json \
  --html --htmlfile /tmp/azure-function-sample/scanresult.html \
  --jsonfile /tmp/azure-function-sample/scanresult.json
```

## Notes on Permissions File

The `function-permissions.json` intentionally includes some **overly broad permissions** 
(e.g., `roleAssignments/write`, `policyAssignments/write`, `resourceGroups/write`) 
to trigger excessive permissions findings in Aqua's scanner — useful for validating 
that the `--function-permissions` flag works correctly during your test.
