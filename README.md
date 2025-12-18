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
- 
