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

- 
