# Azure Python Function in Docker container

<https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=bash%2Cportal&pivots=programming-language-python>

## Testing

```
func start
```

Open browser with <http://127.0.0.1:7071/api/HttpExample?name=Functions>


```
func start --build

docker build --tag msaunby/azurepyfunctionsimage:v1.0.0 .

docker run -p 8080:80 -it msaunby/azurepyfunctionsimage:v1.0.0

docker push msaunby/azurepyfunctionsimage:v1.0.0
```

app_name saunbyffmpeg

storage_name saunby


```
az storage account create --name saunby --location ukwest --resource-group recordings-rg --sku Standard_LRS

az functionapp plan create --resource-group recordings-rg --name myBasicPlan --location ukwest --number-of-workers 1 --sku B1 --is-linux
```


```
az functionapp create --name saunbyffmpeg --storage-account saunby --functions-version 3 --resource-group recordings-rg --plan myBasicPlan --deployment-container-image-name msaunby/azurepyfunctionsimage:v1.0.0

az storage account show-connection-string --resource-group recordings-rg --name saunby --query connectionString --output tsv
```

### Access Azure storage from local function.

See ```local.settings.json```

```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": ""
  }
}
```

```
func azure functionapp fetch-app-settings saunbyffmpeg
```

Now check for new values.

For some reason I needed to fix mine.

```
"Values": {
    "FUNCTIONS_WORKER_RUNTIME": "dotnet",
```

Replace ```dotnet``` with ```python```.

### Adding more functions to the container

```
$ func new --name HttpJsonExample
Select a number for template:
1. Azure Blob Storage trigger
2. Azure Cosmos DB trigger
3. Durable Functions activity (preview)
4. Durable Functions HTTP starter (preview)
5. Durable Functions orchestrator (preview)
6. Azure Event Grid trigger
7. Azure Event Hub trigger
8. HTTP trigger
9. Azure Queue Storage trigger
10. Azure Service Bus Queue trigger
11. Azure Service Bus Topic trigger
12. Timer trigger
Choose option: 8
HTTP trigger
Function name: [HttpTrigger] Writing /home/codespace/workspace/LocalPythonFunctionsProject/HttpJsonExample/__init__.py
Writing /home/codespace/workspace/LocalPythonFunctionsProject/HttpJsonExample/function.json
The function "HttpJsonExample" was created successfully from the "HTTP trigger" template.
```
