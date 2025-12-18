# Подюков Илья. ФИТ-2-2024 НМ. Методы и инструменты DevOps. ЛР по лекции 11
- Создаю данный репозиторий и клонирую его на машинку
- Создаю server/application.py, server/test_application.py, requirements.txt, server/dockerfile
- Пушу в гитхаб
```
ilya@podyukov-deb-2 ~/vparanoid11 (main)> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        requirements.txt
        server/

nothing added to commit but untracked files present (use "git add" to track)
ilya@podyukov-deb-2 ~/vparanoid11 (main)> git add .
ilya@podyukov-deb-2 ~/vparanoid11 (main)> git commit -m "add first files"
[main 9e82b5e] add first files
 4 files changed, 38 insertions(+)
 create mode 100644 requirements.txt
 create mode 100644 server/application.py
 create mode 100644 server/dockerfile
 create mode 100644 server/test_application.py
ilya@podyukov-deb-2 ~/vparanoid11 (main)> git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 967 bytes | 483.00 KiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:podyukov/vparanoid11.git
   af11ac4..9e82b5e  main -> main
```
- Перевожу разработку в отдельную ветку dev
```
ilya@podyukov-deb-2 ~/vparanoid11 (main) [127]> git checkout -b dev
Switched to a new branch 'dev'
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> git push -u origin dev
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/podyukov/vparanoid11/pull/new/dev
remote:
To github.com:podyukov/vparanoid11.git
 * [new branch]      dev -> dev
branch 'dev' set up to track 'origin/dev'.
```
- В вебке гитхаба разрешаю только merge-requests
<img width="1181" height="646" alt="изображение" src="https://github.com/user-attachments/assets/4db5a41a-174a-4b1c-97d5-71836f0f24a7" />

## CI

- Добавляю CI-пайплайны
<img width="1112" height="586" alt="изображение" src="https://github.com/user-attachments/assets/bc6a926e-4c98-40c4-ad18-f4c2fa16026d" />

- Добавляю тестовый сценарий .github/workflows/devops_course_pipeline.yml и проверяю его. Получаю ошибку
<img width="849" height="635" alt="изображение" src="https://github.com/user-attachments/assets/9e8eaf99-b1d8-46de-bbbe-a5f8c6556795" />

- Исправляю ошибку с отступом и заново делаю коммит
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> git commit -am "fix ci"
[dev d708267] fix ci
 1 file changed, 8 insertions(+), 8 deletions(-)
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 528 bytes | 528.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:podyukov/vparanoid11.git
   01035a3..d708267  dev -> dev
```
<img width="780" height="608" alt="изображение" src="https://github.com/user-attachments/assets/5683280c-c7cb-407b-9d27-c05491428626" />

- Добавляю боевой тест .github/workflows/cicd.yml
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> nano .github/workflows/cicd.yml
ilya@podyukov-deb-2 ~/vparanoid11 (dev)>
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> git add .
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> git commit -m "workflow"
[dev 58496fd] workflow
 1 file changed, 36 insertions(+)
 create mode 100644 .github/workflows/cicd.yml
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 853 bytes | 853.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:podyukov/vparanoid11.git
   d708267..58496fd  dev -> dev
```
- Снова ловлю ошибки
<img width="1066" height="388" alt="изображение" src="https://github.com/user-attachments/assets/48d63ef3-6359-4185-9a56-38d5441e40ba" />

- Исправляю ошибку с отступом, смотрю тесты
<img width="453" height="140" alt="изображение" src="https://github.com/user-attachments/assets/d90f6376-c230-42be-acdf-859975d059e7" />
<img width="515" height="134" alt="изображение" src="https://github.com/user-attachments/assets/4eaeabac-f91f-4d18-8499-db3573571dc0" />

- Снова исправляю ошибку, unit-tests прошёл успешно, lint ещё жалуется
<img width="652" height="456" alt="изображение" src="https://github.com/user-attachments/assets/4e8d195b-c73d-4879-9566-da804ad25d1e" />

```
Installing collected packages: typing-extensions, tomlkit, tomli, pygments, pluggy, platformdirs, packaging, mccabe, isort, iniconfig, dill, exceptiongroup, astroid, pytest, pylint

Successfully installed astroid-4.0.2 dill-0.4.0 exceptiongroup-1.3.1 iniconfig-2.3.0 isort-7.0.0 mccabe-0.7.0 packaging-25.0 platformdirs-4.5.1 pluggy-1.6.0 pygments-2.19.2 pylint-4.0.4 pytest-9.0.2 tomli-2.3.0 tomlkit-0.13.3 typing-extensions-4.15.0
************* Module application
server/application.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
server/application.py:23:0: C0303: Trailing whitespace (trailing-whitespace)
server/application.py:36:0: C0303: Trailing whitespace (trailing-whitespace)

-----------------------------------
Your code has been rated at 7.69/10

Error: Process completed with exit code 16.
```
- Наконец-то тесты прошли успешно
<img width="507" height="236" alt="изображение" src="https://github.com/user-attachments/assets/584d2380-b312-462b-a2bc-25c84186c2dd" />

<img width="701" height="383" alt="изображение" src="https://github.com/user-attachments/assets/d133c11e-9703-4a88-973e-c09460e7a1d2" />

- Создаю k8s манифест server-k8s-manifests/devops-psu.yml
- Удаляю деплойменты прошлой лабораторной работы
- Применяю k8s-манифесты
```
ilya@podyukov-deb-2 ~> kubectl create namespace devops-psu
namespace/devops-psu created
ilya@podyukov-deb-2 ~/v/server-k8s-manifests (dev)> kubectl apply -f devops-psu.yml 
deployment.apps/devops-psu created
service/service-devops created
```
- Авторизуюсь в своём репозитории
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> docker login -u ilyapod

i Info → A Personal Access Token (PAT) can be used instead.
         To create a PAT, visit https://app.docker.com/settings


Password:

WARNING! Your credentials are stored unencrypted in '/home/ilya/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded
```
- Собираю образ и заливаю его в репозиторий
```
ilya@podyukov-deb-2 ~/v/server (dev)> docker build -t ilyapod/devops-psu:latest .
[+] Building 9.7s (12/12) FINISHED                                                                         docker:default
 => [internal] load build definition from dockerfile                                                                 0.0s
 => => transferring dockerfile: 375B                                                                                 0.0s 
 => [internal] load metadata for docker.io/library/python:3.7-slim                                                   2.2s 
 => [auth] library/python:pull token for registry-1.docker.io                                                        0.0s
 => [internal] load .dockerignore                                                                                    0.0s
 => => transferring context: 2B                                                                                      0.0s 
 => [1/6] FROM docker.io/library/python:3.7-slim@sha256:b53f496ca43e5af6994f8e316cf03af31050bf7944e0e4a308ad86c001c  5.2s 
 => => resolve docker.io/library/python:3.7-slim@sha256:b53f496ca43e5af6994f8e316cf03af31050bf7944e0e4a308ad86c001c  0.0s 
 => => sha256:39312d8b4ab77de264678427265a2668073675bb8666caf723da18c9e4b7e3fc 3.13MB / 3.13MB                       0.5s 
 => => sha256:f9afc3cc0135aad884dad502f28a5b3d8cd32565116131da818ebf2ea6d46095 244B / 244B                           0.7s 
 => => sha256:8973eb85275f19b8d72c6047560629116ad902397e5c1885b2508788197de28b 11.38MB / 11.38MB                     1.2s
 => => sha256:a803e7c4b030119420574a882a52b6431e160fceb7620f61b525d49bc2d58886 29.12MB / 29.12MB                     2.0s
 => => sha256:bf3336e84c8e00632cdea35b18fec9a5691711bdc8ac885e3ef54a3d5ff500ba 3.50MB / 3.50MB                       1.9s 
 => => extracting sha256:a803e7c4b030119420574a882a52b6431e160fceb7620f61b525d49bc2d58886                            1.7s 
 => => extracting sha256:bf3336e84c8e00632cdea35b18fec9a5691711bdc8ac885e3ef54a3d5ff500ba                            0.2s
 => => extracting sha256:8973eb85275f19b8d72c6047560629116ad902397e5c1885b2508788197de28b                            0.7s
 => => extracting sha256:f9afc3cc0135aad884dad502f28a5b3d8cd32565116131da818ebf2ea6d46095                            0.0s
 => => extracting sha256:39312d8b4ab77de264678427265a2668073675bb8666caf723da18c9e4b7e3fc                            0.4s 
 => [internal] load build context                                                                                    0.1s 
 => => transferring context: 800B                                                                                    0.0s 
 => [2/6] RUN mkdir -p /usr/local/http-server                                                                        0.6s 
 => [3/6] RUN useradd runner -d /home/runner -m -s /bin/bash                                                         0.4s 
 => [4/6] WORKDIR /usr/local/http-server                                                                             0.1s 
 => [5/6] ADD ./application.py /usr/local/http-server/application.py                                                 0.0s 
 => [6/6] RUN chown -R runner:runner /usr/local/http-server/                                                         0.3s 
 => exporting to image                                                                                               0.5s 
 => => exporting layers                                                                                              0.3s 
 => => exporting manifest sha256:b6910a64ae9d8193e1c1bf5ad7d990d776ee9a96b2604989b2f78be9a68617ed                    0.0s 
 => => exporting config sha256:b8122b1fb13278f0891b81e2e38967f5db8c73e10b637f09e8c8796c3a815760                      0.0s 
 => => exporting attestation manifest sha256:73bf1869f249a6c92cbb22b8f848899376909da02ae072685adbd5df867c234a        0.0s 
 => => exporting manifest list sha256:4dff82ffe217743850df4a266664ee88f869fb15e62a210820a4f416f07b191f               0.0s 
 => => naming to docker.io/ilyapod/devops-psu:latest                                                                 0.0s 
 => => unpacking to docker.io/ilyapod/devops-psu:latest                                                              0.1s
ilya@podyukov-deb-2 ~/v/server (dev)> docker push ilyapod/devops-psu:latest
The push refers to repository [docker.io/ilyapod/devops-psu]
a803e7c4b030: Pushed
5d09c54e1297: Pushed
fdad93741f0f: Pushed
f9afc3cc0135: Pushed
bed304655c68: Pushed
3216ac46fbf8: Pushed
39312d8b4ab7: Pushed
4f4fb700ef54: Pushed
8973eb85275f: Pushed
bf3336e84c8e: Pushed
16296d10a69b: Pushed
latest: digest: sha256:4dff82ffe217743850df4a266664ee88f869fb15e62a210820a4f416f07b191f size: 856
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl apply -f server-k8s-manifests/devops-psu.yml
deployment.apps/devops-psu unchanged
service/service-devops unchanged
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
devops-psu-5979c5f77c-zs2pc   1/1     Running   0          14m
```
- Переключаюсь в namespace devops-psu и пробрасываю порты
```
ilya@podyukov-deb-2 ~/v/server-k8s-manifests (dev)> kubectl config set-context --current --namespace=devops-psu
Context "minikube" modified.
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl port-forward --address 0.0.0.0 svc/service-devops 12345:12345
Forwarding from 0.0.0.0:12345 -> 8000
Handling connection for 12345
Handling connection for 12345
Handling connection for 12345
```
- Проверяю работу в браузере
<img width="575" height="183" alt="изображение" src="https://github.com/user-attachments/assets/9f43893b-990e-4a6a-9528-0c9d08c5b30a" />

## CD
- Access token на docherhub создал ранее
- На github добавляю токены DOCKER_USERNAME и DOCKER_TOKEN
- Создаю пайплайн для сборки и публикации образа в Docker Hub .github/workflows/release.yml и делаю коммит в репозиторий
- Создаю pull-request и выполняю merge в главную ветку main
<img width="1051" height="709" alt="изображение" src="https://github.com/user-attachments/assets/4a670a4f-3c3c-4299-b111-bb252088e3d9" />

- Решаю проблемы с конфликтом README.md
<img width="934" height="301" alt="изображение" src="https://github.com/user-attachments/assets/84bfb873-e5e2-43ae-b596-4b4b2f29cb95" />

- Делаю merge
<img width="954" height="380" alt="изображение" src="https://github.com/user-attachments/assets/3e9b7dfb-ed6b-41e1-b122-cfd6f9ab4762" />

<img width="941" height="118" alt="изображение" src="https://github.com/user-attachments/assets/b7c096f2-dddc-4f80-bf70-ceff02cce0bf" />

- Борюсь с мелкими проблемами, в итоге merge успешен
<img width="692" height="356" alt="изображение" src="https://github.com/user-attachments/assets/e447e801-0c80-4163-a1de-5c1c597b47d3" />

<img width="1402" height="321" alt="изображение" src="https://github.com/user-attachments/assets/0e86a396-c47e-4757-8020-e7ba326edf0d" />

### ArgoCD
- Устанавливаю ArgoCD
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl create namespace argocd
namespace/argocd created
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
Warning: unrecognized format "int64"
customresourcedefinition.apiextensions.k8s.io/applications.argoproj.io created
customresourcedefinition.apiextensions.k8s.io/applicationsets.argoproj.io created
customresourcedefinition.apiextensions.k8s.io/appprojects.argoproj.io created
serviceaccount/argocd-application-controller created
serviceaccount/argocd-applicationset-controller created
serviceaccount/argocd-dex-server created
serviceaccount/argocd-notifications-controller created 
serviceaccount/argocd-redis created      
serviceaccount/argocd-repo-server created
serviceaccount/argocd-server created
role.rbac.authorization.k8s.io/argocd-application-controller created
role.rbac.authorization.k8s.io/argocd-applicationset-controller created
role.rbac.authorization.k8s.io/argocd-dex-server created
role.rbac.authorization.k8s.io/argocd-notifications-controller created
role.rbac.authorization.k8s.io/argocd-redis created
role.rbac.authorization.k8s.io/argocd-server created
clusterrole.rbac.authorization.k8s.io/argocd-application-controller created
clusterrole.rbac.authorization.k8s.io/argocd-applicationset-controller created
clusterrole.rbac.authorization.k8s.io/argocd-server created
rolebinding.rbac.authorization.k8s.io/argocd-application-controller created
rolebinding.rbac.authorization.k8s.io/argocd-applicationset-controller created
rolebinding.rbac.authorization.k8s.io/argocd-dex-server created
rolebinding.rbac.authorization.k8s.io/argocd-notifications-controller created
rolebinding.rbac.authorization.k8s.io/argocd-redis created
rolebinding.rbac.authorization.k8s.io/argocd-server created
clusterrolebinding.rbac.authorization.k8s.io/argocd-application-controller created
clusterrolebinding.rbac.authorization.k8s.io/argocd-applicationset-controller created
clusterrolebinding.rbac.authorization.k8s.io/argocd-server created
configmap/argocd-cm created
configmap/argocd-cmd-params-cm created
configmap/argocd-gpg-keys-cm created
configmap/argocd-notifications-cm created
configmap/argocd-rbac-cm created
configmap/argocd-ssh-known-hosts-cm created
configmap/argocd-tls-certs-cm created
secret/argocd-notifications-secret created
secret/argocd-secret created
service/argocd-applicationset-controller created
service/argocd-dex-server created
service/argocd-metrics created
service/argocd-notifications-controller-metrics created
service/argocd-redis created
service/argocd-repo-server created
service/argocd-server created
service/argocd-server-metrics created
deployment.apps/argocd-applicationset-controller created
deployment.apps/argocd-dex-server created
deployment.apps/argocd-notifications-controller created
deployment.apps/argocd-redis created
deployment.apps/argocd-repo-server created
deployment.apps/argocd-server created
statefulset.apps/argocd-application-controller created
networkpolicy.networking.k8s.io/argocd-application-controller-network-policy created
networkpolicy.networking.k8s.io/argocd-applicationset-controller-network-policy created
networkpolicy.networking.k8s.io/argocd-dex-server-network-policy created
networkpolicy.networking.k8s.io/argocd-notifications-controller-network-policy created
networkpolicy.networking.k8s.io/argocd-redis-network-policy created
networkpolicy.networking.k8s.io/argocd-repo-server-network-policy created
networkpolicy.networking.k8s.io/argocd-server-network-policy created
```
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl get deployments -n argocd
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
argocd-applicationset-controller   1/1     1            1           74s
argocd-dex-server                  1/1     1            1           74s
argocd-notifications-controller    1/1     1            1           73s
argocd-redis                       1/1     1            1           73s
argocd-repo-server                 1/1     1            1           73s
argocd-server                      1/1     1            1           73s
```
- Вытаскиваю стартовый админский пароль
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl -n argocd get secret argocd-initial-admin-secret --template={{.data.password}} | base64 -d
p1P5cFDMXC7v6Uck⏎
```
- Пробрасываю api-сервис ArgoCD наружу
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
service/argocd-server patched
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> kubectl patch svc argocd-server -n argocd -p '{"spec": {"externalIPs": [ "10.101.249.250" ]}}'
service/argocd-server patched
```
```
ilya@podyukov-deb-2 ~/vparanoid11 (dev)> kubectl config set-context --current --namespace=argocd
Context "minikube" modified.
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> kubectl get service
NAME                                      TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)                      AGE
argocd-applicationset-controller          ClusterIP      10.101.170.62    <none>           7000/TCP,8080/TCP            7m28s
argocd-dex-server                         ClusterIP      10.105.215.9     <none>           5556/TCP,5557/TCP,5558/TCP   7m28s
argocd-metrics                            ClusterIP      10.99.3.48       <none>           8082/TCP                     7m28s
argocd-notifications-controller-metrics   ClusterIP      10.111.111.221   <none>           9001/TCP                     7m28s
argocd-redis                              ClusterIP      10.107.248.87    <none>           6379/TCP                     7m28s
argocd-repo-server                        ClusterIP      10.107.79.216    <none>           8081/TCP,8084/TCP            7m28s
argocd-server                             LoadBalancer   10.96.80.110     10.101.249.250   80:32532/TCP,443:31416/TCP   7m28s
argocd-server-metrics                     ClusterIP      10.97.136.138    <none>           8083/TCP                     7m28s
ilya@podyukov-deb-2 ~/vparanoid11 (dev) [1]> kubectl port-forward --address 0.0.0.0 svc/argocd-server 8080:80
Forwarding from 0.0.0.0:8080 -> 8080
Handling connection for 8080
Handling connection for 8080
E1218 10:24:03.031795 1500526 portforward.go:404] "Unhandled Error" err="error copying from local connection to remote stream: writeto tcp4 10.101.249.250:8080->10.101.14.143:65212: read tcp4 10.101.249.250:8080->10.101.14.143:65212: read: connection reset by peer"
Handling connection for 8080
```
- Попадаю в веб интерфейс
<img width="1669" height="781" alt="изображение" src="https://github.com/user-attachments/assets/62914997-be07-4303-8574-76e3b9fb2dba" />

- Беру с ВМ приватный ключ для репозитория github
<img width="832" height="627" alt="изображение" src="https://github.com/user-attachments/assets/9f4240f0-f92c-4776-94a1-f5feefed093d" />

<img width="1065" height="135" alt="изображение" src="https://github.com/user-attachments/assets/9cda2e56-c7ea-4b24-a917-98c4a2b12933" />

- Подключаю манифесты приложения для контроля состояния
<img width="1193" height="846" alt="изображение" src="https://github.com/user-attachments/assets/77cf766b-08f3-4882-9ce5-03f6ad8f0fab" />

- Выбираю репо, указываю ветку для отслеживания и путь к манифестам
<img width="391" height="351" alt="изображение" src="https://github.com/user-attachments/assets/31f8cbea-da36-48a5-a7ad-276d704d2806" />

- Указываю реквизиты кластера k8s и пространство имен
<img width="284" height="225" alt="изображение" src="https://github.com/user-attachments/assets/b51f77ec-fcda-4c42-a644-f92174e87ef4" />

- Устанавливаю приложение
<img width="417" height="375" alt="изображение" src="https://github.com/user-attachments/assets/ebe3e925-5ca0-4a95-8f15-feb3743c1a8c" />

<img width="1527" height="525" alt="изображение" src="https://github.com/user-attachments/assets/009fe23e-7611-4068-9473-2b4d44b4150f" />

- Проверяем. Добавляю server/index.html и правлю докер файл
- Делаю коммит в ветку dev
- Открываю pull-request
<img width="944" height="198" alt="изображение" src="https://github.com/user-attachments/assets/8cafa88b-6fa4-4b64-a045-834b6ac01039" />
- Прохожу код-ревью и делаю merge в ветку main
