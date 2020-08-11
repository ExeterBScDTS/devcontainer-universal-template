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