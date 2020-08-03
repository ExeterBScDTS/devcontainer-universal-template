

<https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image>

```sh
func init LocalFunctionsProject --worker-runtime dotnet --docker

cd LocalFunctionsProject

func new --name HttpExample --template "HTTP trigger"

func start --build

docker build --tag msaunby/azurefunctionsimage:v1.0.0 .

docker run -p 8080:80 -it msaunby/azurefunctionsimage:v1.0.0

az account list-locations

az group create --name AzureFunctionsContainers-rg --location ukwest

az storage account create --name containerexpt --location ukwest --resource-group AzureFunctionsContainers-rg --sku Standard_LRS

az functionapp plan create --resource-group AzureFunctionsContainers-rg --name myPremiumPlan --location ukwest --number-of-workers 1 --sku EP1 --is-linux
```

app_name containerexptapp

storage_name containerexpt

```
az functionapp create --name <app_name> --storage-account <storage_name> --resource-group AzureFunctionsContainers-rg --plan myPremiumPlan --deployment-container-image-name <docker_id>/azurefunctionsimage:v1.0.0
```

```
az functionapp create --name containerexptapp --storage-account containerexpt --resource-group AzureFunctionsContainers-rg --plan myPremiumPlan --deployment-container-image-name msaunby/azurefunctionsimage:v1.0.0
```

Gives warning
```
No functions version specified so defaulting to 2. In the future, specifying a version will be required. To create a 2.x function you would pass in the flag `--functions-version 2`
```

Cancelled and rerun with ```--functions-version```

```
az functionapp create --name containerexptapp --storage-account containerexpt --functions-version 3 --resource-group AzureFunctionsContainers-rg --plan myPremiumPlan --deployment-container-image-name msaunby/azurefunctionsimage:v1.0.0

az storage account show-connection-string --resource-group AzureFunctionsContainers-rg --name containerexpt --query connectionString --output tsv
```

Result
```
DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=containerexpt;AccountKey=bqjmZBgZd6p57ACG/gU7/hJuc/HKepI/TL2GhhyZ4BoqPoWWNIaK3O6j7ak1HANMiIczkBtWZNQ/DNup0WGU2A==
```