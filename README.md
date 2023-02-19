# buildbot-tekton


The buildbot-tekton repository contains a ChatOps Slack app that is integrated with Tekton pipelines. The app allows users to initiate a pipeline run from within a Slack channel by typing a specific [slash commands]()  . 

The repository also includes documentation on how to set up and configure the app, as well as examples of how to use it in practice. Additionally, the repository contains sample Tekton pipeline definitions that can be used as a starting point for creating new pipelines.

Overall, this repository provides a convenient and streamlined way to integrate Tekton pipelines with Slack, enabling teams to easily initiate and monitor pipeline runs from within their messaging platform.

This repository is part of an article on ChatOps and Tekton pipelines, which provides an overview of how to use the app and integrate it with Tekton pipelines. The article also includes documentation on how to set up and configure the app, as well as examples of how to use it in practice.

To access the article, please click on the following [link](). The repository itself contains sample Tekton pipeline definitions that can be used as a starting point for creating new pipelines.




# component 

- sample app - a simple python "hello world" app that will be containerized and pushed to quay.io image registry 
- Tetkton - includes all the the Tekton resources required. can be easily deploy using [kostomize]()  
- Slack-webhook - the code for a customized Tekton interceptor. Designed to parse slack command and pass them to the Tekton pipeline. the image is public available    

# how to deploy 

To deploy the ChatOps Slack app and integrate it with Tekton pipelines, follow these steps:

1. Clone the GitHub repository to your local machine.
2. Install any necessary dependencies, such as the Slack API client library.
   - [kind]() -  version v1.24
   - [kubectl]() 
   - [tkn]() - tekton CLI 

3. Initiate a new kind cluster using the following command 

``` kind create cluster --name demo --image kindest/node:v1.24.0 ```

4. Deploy Tetkton on the local cluster 

- Tekton Pipelines: v0.41.0
- Tekton Triggers: v0.22.3 - or any version that includes [this fix]() 

use the below command to deploy Tekton: 

```
# Deploy pipeline 
kubectl apply -f https://storage.googleapis.com/tekton-releases/pipeline/previous/v0.41.1/release.yaml
 
# Deploy triggers
kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/previous/v0.22.0/release.yaml

#Deploy intercepter 

kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/previous/v0.22.0/interceptors.yaml
 ```

5. create the slack-webhook-secret and replace the existing slack-webhook-secret.yaml file under ./Tekton/Secrets/ 

```
kind: Secret
apiVersion: v1
metadata:
  name: slack-webhook-secret
stringData:
  url: [WEB HOOK FROM SLACK ]
```

6. deploy application using kustomize: 
``` kubectl apply -k Tekton ```
