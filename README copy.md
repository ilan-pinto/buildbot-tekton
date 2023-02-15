# buildbot-tekton


# how to deploy 
Tekton Pipelines: v0.41.0
Tekton Triggers: v0.22.0
Pipelines as Code: 0.15.2
Kubernetes version v1.24.6+5658434




- start kind 

- install 
```
kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/previous/v0.21.0/release.yaml

kubectl apply -f https://storage.googleapis.com/tekton-releases/triggers/previous/v0.22.0/interceptors.yaml
```



