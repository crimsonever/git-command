# 说明

这是一个用于从文本中构建知识图谱的 Python 项目，支持以下功能：

- 实体抽取
- 实体关系识别
- 可视化图谱展示（使用 NetworkX + matplotlib）

但是，它的功能不重要。
我将此项目上传到github，仅用于通过实例来记录GIT基本命令。
每一条步骤都写得尽可能详细，把自己当作一个白痴，以防自己忘记。
并且仅用于大致的理解，未必严谨。

## 一、从github克隆项目到本地
1、克隆仓库

```bash
git clone https://github.com/crimsonever/knowledge-graph.git
```
该命令将GitHub上的远程仓库完整复制一份到本地当前路径下，会自动创建test文件夹并包含项目所有文件。

2、创建并启用虚拟环境

先进入项目目录
```bash
cd knowledge-graph
```

作者在向github上传项目时，不会将运行环境一起上传。 相应地，作者一般会通过requirements.txt来记录其所使用的环境配置。
通过以下命令，你可以创建虚拟的python环境（在名为.venv的文件夹中）
```bash
python -m venv .venv
```
上述命令只是创建了一个虚拟环境，该项目还未使用它作为自己的运行环境。
通过以下命令，使得项目以刚才创建的虚拟环境作为解释器。
```bash
.venv\Scripts\activate
```
若成功，那么此刻你的路径前应该多出了(.venv)，告知你使用了虚拟环境。

3、安装依赖

通过以下命令，在虚拟环境中自动安装项目所需的第三方库。
```bash
pip install -r requirements.txt
```

4、运行项目

```bash
python kg_builder.py
```
```bash
python query_demo.py
```

## 二、将本地项目首次上传到github
1、生成requirements.txt

```bash
pip freeze > requirements.txt
```

requirements.txt文件把当前虚拟环境下已安装的包记录下来，供他人安装。

2、创建.gitignore文件

整个项目中包含一些并不应当被上传的文件，如.venv/
此时可以手动创建一个.gitignore文件，用于排除不希望上传的文件。

3、初始化Git仓库

```bash
git init
```

该命令将生成.git/隐藏目录，里面记录了：提交记录、分支信息、Git配置。
因此，实际上也可以通过是否存在.git隐藏文件夹判断是否需要初始化。

4、添加修改内容到暂存区
```bash
git add .
```

Git有3个区：

| 区域   | 用途                        |
|------|---------------------------|
| 工作区  | 你实际编辑的文件                  |
| 暂存区  | 准备提交的变更（git add）          |
| 本地仓库 | 真正提交（git commit）后进入的历史版本区 |

git add .是将所有当前项目下的新文件或修改过的文件，放入暂存区。

5、提交更改到本地仓库
```bash
git commit -m "first commit"
```
将暂存区的内容提交到本地仓库，并添加提交说明。"first commit" 是这一版本的说明，方便后续回溯和查看。

6、关联远程仓库
```bash
git remote add origin https://github.com/你的用户名/你的仓库名.git
```
给当前 Git 仓库添加一个远程仓库地址，并命名为origin（默认推荐）

执行完后，Git 会记录下来：origin → https://github.com/xxx/xxx.git
之后 push、pull 时就可以用 origin 来代替长地址。

注意：这只是关联地址，不代表上传或同步！

7、推送代码到github
```bash
git branch -M main
git push -u origin main
```

该命令将本地的 main 分支代码推送到远程仓库的 origin仓库

-u：告诉 Git，“以后我用 git push 就默认推送到 origin main”

origin：是在上一步定义的远程仓库名

main：是你本地当前所在分支（可能是 master，具体看你实际分支）

## 三、后续更新本地代码后上传
1、查看当前状态（哪些文件被修改了）
```bash
git status
```

2、添加所有变动到暂存区

```bash
git add .
```

3、提交变更

```bash
git commit -m "update XXX"
```

4、推送到Github

```bash
git push
```

## 四、从远程仓库拉取更新
若在 GitHub 上修改了项目，想同步到本地
```bash
git pull
```