# buildbot-tekton

This repository provides a convenient and streamlined example to integrate Tekton pipelines with Slack, enabling teams to easily initiate and monitor pipeline runs from within their messaging platform.

This repository is part of an article on ChatOps and Tekton pipelines, which provides an overview of how to integrate slack with Tekton pipelines. 

To access the article, please click on the following [link](). 



# component 

- Sample app - a simple python "hello world" app that will be containerized and pushed to quay.io image registry as part of the pipeline 
- Tetkton - includes all the the Tekton resources required.


# how to deploy 

To deploy the ChatOps Slack app and integrate it with Tekton pipelines, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Install any necessary dependencies, such as the Slack API client library.
   - [kind]() -  version v1.24
   - [kubectl]() 
   - [tkn]() - tekton CLI 

3. Initiate a new kind cluster using the following command 

``` kind create cluster --name demo ```

4. Deploy Tetkton on the local cluster 

- Tekton Pipelines: latest
- Tekton Triggers:latest - any version that includes [this features](https://github.com/tektoncd/triggers/pull/1548) 

use the below commands to deploy Tekton pipeline services  


Deploy pipeline: 
```kubectl apply -f https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml```

Deploy triggers:

```kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml```

Deploy interceptor:
```kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/latest/interceptors.yaml```


5. Add your slack webhook to the slack-webhook-secret.yaml file under ./Tekton/Secrets/ 

```
kind: Secret
apiVersion: v1
metadata:
  name: slack-webhook-secret
stringData:
  url: [WEB HOOK FROM SLACK ]
```

6. Modify file ./Tekton/build-pipeline.yaml 
line 52 - image value - change to your preferred image registry 

7. Deploy the builder bot tekton pipeline resources: 
``` kubectl apply -f Tekton ```

8. Define an ingress for the event listener `builder-bot-listener-interceptor` . or use `port-forward` command:
```kubectl port-forward svc/el-builder-bot-listener-interceptor 8080 -n sample-app```

9. Configure the slack slash command as described in the article 