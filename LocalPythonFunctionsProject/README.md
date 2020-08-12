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

app_name containerexptapp

storage_name saunby

```
az storage account create --name saunby --location ukwest --resource-group recordings-rg --sku Standard_LRS

az functionapp plan create --resource-group recordings-rg --name myBasicPlan --location ukwest --number-of-workers 1 --sku B1 --is-linux
```


```
az functionapp create --name saunbyffmpeg --storage-account saunby --functions-version 3 --resource-group recordings-rg --plan myBasicPlan --deployment-container-image-name msaunby/azurepyfunctionsimage:v1.0.0

az storage account show-connection-string --resource-group recordings-rg --name saunby --query connectionString --output tsv
```