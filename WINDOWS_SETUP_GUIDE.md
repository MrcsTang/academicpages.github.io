# Windows 命令行操作指南

本指南将 README_SETUP.md 中的步骤转换为具体的 Windows 命令行操作。

## 准备工作

### 1. 安装必要工具

```powershell
# 安装 Git (如果未安装)
winget install Git.Git

# 安装 GitHub CLI (用于命令行操作 GitHub)
winget install GitHub.cli

# 安装 Ruby 和 Bundler (用于本地预览)
winget install RubyInstallerTeam.RubyWithDevKit

# 安装 Chocolatey (可选，包管理器)
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

### 2. 配置 Git

```bash
# 配置用户名和邮箱
git config --global user.name "MrcsTang"
git config --global user.email "your-email@example.com"

# 生成 SSH 密钥 (用于 GitHub 认证)
ssh-keygen -t ed25519 -C "your-email@example.com"

# 将 SSH 密钥添加到 GitHub
# 复制公钥内容到剪贴板
cat ~/.ssh/id_ed25519.pub | clip
# 然后在 GitHub Settings > SSH and GPG keys 中添加
```

### 3. 克隆仓库

```bash
# 克隆仓库到本地
git clone git@github.com:MrcsTang/TTTb0521.github.io.git
cd TTTb0521.github.io
```

---

## 步骤 1: 删除模板示例文件

### 方法 A: 使用 Git 命令删除

```bash
# 删除模板示例文件
del _posts\2012-08-14-blog-post-1.md
del _posts\2013-08-14-blog-post-2.md
del _posts\2014-08-14-blog-post-3.md
del _posts\2015-08-14-blog-post-4.md
del _posts\2199-01-01-future-post.md

# 提交更改
git add -A
git commit -m "删除模板示例文件"
git push origin master
```

### 方法 B: 使用 GitHub CLI

```bash
# 安装 GitHub CLI 后，登录
gh auth login

# 删除文件
gh repo delete _posts/2012-08-14-blog-post-1.md --yes
gh repo delete _posts/2013-08-14-blog-post-2.md --yes
gh repo delete _posts/2014-08-14-blog-post-3.md --yes
gh repo delete _posts/2015-08-14-blog-post-4.md --yes
gh repo delete _posts/2199-01-01-future-post.md --yes
```

**注意**: GitHub CLI 不能直接删除仓库内的单个文件，需要通过网页操作或使用 API。

### 推荐方法: 使用网页操作

```powershell
# 直接在浏览器中打开仓库
start https://github.com/MrcsTang/academicpages.github.io
```

然后手动删除 `_posts/` 文件夹中的模板文件。

---

## 步骤 2: 重命名仓库

**此步骤必须在 GitHub 网页上完成**，因为重命名仓库会影响远程 URL。

### 使用 GitHub CLI 重命名

```bash
# 使用 GitHub CLI 重命名仓库
gh repo rename MrcsTang.github.io --org MrcsTang
```

### 更新本地仓库远程地址

```bash
# 更新远程仓库地址
git remote set-url origin git@github.com:MrcsTang/MrcsTang.github.io.git

# 验证更新
git remote -v
```

---

## 步骤 3: 上传图片文件

### 1. 创建图片目录结构

```bash
# 在仓库根目录创建 images 文件夹及其子文件夹
mkdir images
mkdir images\graph
mkdir images\linear-list
mkdir images\network
mkdir images\searching-and-sorting
mkdir images\stack-and-queue
mkdir images\tree-and-binary-tree
mkdir images\numerical-computation
```

### 2. 复制图片文件

```bash
# 复制 Graph 文件夹中的图片
copy Graph\*.png images\graph\

# 复制其他文件夹的图片
copy LinearList\*.png images\linear-list\
copy Network\*.png images\network\
copy SearchingAndSorting\*.png images\searching-and-sorting\
copy StackAndQueue\*.png images\stack-and-queue\
copy TreeAndBinaryTree\*.png images\tree-and-binary-tree\
copy NumericalComputation\*.png images\numerical-computation\
```

### 3. 提交并推送图片

```bash
# 添加所有更改
git add -A

# 提交更改
git commit -m "添加图片文件"

# 推送到 GitHub
git push origin master
```

### 完整脚本

```powershell
# 创建目录结构
mkdir images -Force
mkdir images\graph, images\linear-list, images\network, images\searching-and-sorting, images\stack-and-queue, images\tree-and-binary-tree, images\numerical-computation -Force

# 复制图片文件
Copy-Item Graph\*.png images\graph\ -Force
Copy-Item LinearList\*.png images\linear-list\ -Force
Copy-Item Network\*.png images\network\ -Force
Copy-Item SearchingAndSorting\*.png images\searching-and-sorting\ -Force
Copy-Item StackAndQueue\*.png images\stack-and-queue\ -Force
Copy-Item TreeAndBinaryTree\*.png images\tree-and-binary-tree\ -Force
Copy-Item NumericalComputation\*.png images\numerical-computation\ -Force

# 提交更改
git add -A
git commit -m "添加图片文件"
git push origin master
```

---

## 步骤 4: 配置 GitHub Pages

**此步骤必须在 GitHub 网页上完成**。

```powershell
# 直接在浏览器中打开 GitHub Pages 设置页面
start https://github.com/MrcsTang/MrcsTang.github.io/settings/pages
```

操作步骤：
1. 在 Source 部分选择 "Deploy from a branch"
2. 选择 branch 为 "master" (或 "main")
3. 点击 Save

---

## 步骤 5: 本地预览

### 1. 安装 Ruby 和 Bundler

```bash
# 验证 Ruby 安装
ruby --version

# 验证 Bundler 安装
bundler --version

# 如果未安装 Bundler
gem install bundler
```

### 2. 安装 Jekyll 依赖

```bash
# 安装依赖
bundle install
```

**注意**: 如果遇到错误，可能需要安装额外的依赖：

```powershell
# 安装 Development Kit (如果使用 RubyInstaller)
ridk enable

# 安装 make 工具 (用于编译扩展)
choco install make
```

### 3. 启动本地服务器

```bash
# 启动本地服务器
bundle exec jekyll serve

# 或者使用自定义配置启动
bundle exec jekyll serve --livereload --port 4000
```

### 4. 访问本地站点

打开浏览器访问：http://localhost:4000

---

## 常用命令速查

### Git 操作

```bash
# 查看状态
git status

# 查看差异
git diff

# 查看提交历史
git log --oneline

# 拉取最新更改
git pull origin master

# 强制推送到远程 (谨慎使用)
git push -f origin master
```

### Jekyll 操作

```bash
# 构建站点
jekyll build

# 构建并监视文件变化
jekyll build --watch

# 清理缓存
jekyll clean

# 使用不同配置
jekyll serve --config _config.yml,_config_dev.yml
```

---

## 故障排除

### 1. Git 认证问题

```bash
# 测试 SSH 连接
ssh -T git@github.com

# 如果使用 HTTPS，更新凭据
git config --global credential.helper wincred
```

### 2. Bundle 安装问题

```bash
# 清除缓存
bundle clean --force

# 重新安装
bundle install --verbose

# 更新 Gem
gem update bundler
```

### 3. Jekyll 构建问题

```bash
# 检查 Ruby 版本
ruby -v

# 检查 Jekyll 版本
jekyll -v

# 重新安装 Jekyll
gem uninstall jekyll
gem install jekyll

# 安装缺失的依赖
gem install minima jekyll-feed jekyll-seo-tag jekyll-archives
```

---

## 完成后的操作

1. **验证站点**: 访问 https://mrcstang.github.io 确认站点正常
2. **检查图片**: 确认所有图片正确显示
3. **更新配置**: 根据需要编辑 `_config.yml` 自定义站点信息

---

## 完整一键脚本

将以下内容保存为 `setup.ps1` 并在 PowerShell 中执行：

```powershell
#!/usr/bin/env pwsh

Write-Host "=== Windows 博客设置脚本 ===" -ForegroundColor Green

# 切换到仓库目录
Set-Location -Path (Get-Item -Path ".\").FullName

# 1. 删除模板文件
Write-Host "1. 删除模板示例文件..." -ForegroundColor Yellow
Remove-Item -Path "_posts\2012-08-14-blog-post-1.md" -ErrorAction SilentlyContinue
Remove-Item -Path "_posts\2013-08-14-blog-post-2.md" -ErrorAction SilentlyContinue
Remove-Item -Path "_posts\2014-08-14-blog-post-3.md" -ErrorAction SilentlyContinue
Remove-Item -Path "_posts\2015-08-14-blog-post-4.md" -ErrorAction SilentlyContinue
Remove-Item -Path "_posts\2199-01-01-future-post.md" -ErrorAction SilentlyContinue
Write-Host "   完成" -ForegroundColor Green

# 2. 创建图片目录
Write-Host "2. 创建图片目录结构..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "images\graph"
New-Item -ItemType Directory -Force -Path "images\linear-list"
New-Item -ItemType Directory -Force -Path "images\network"
New-Item -ItemType Directory -Force -Path "images\searching-and-sorting"
New-Item -ItemType Directory -Force -Path "images\stack-and-queue"
New-Item -ItemType Directory -Force -Path "images\tree-and-binary-tree"
New-Item -ItemType Directory -Force -Path "images\numerical-computation"
Write-Host "   完成" -ForegroundColor Green

# 3. 复制图片
Write-Host "3. 复制图片文件..." -ForegroundColor Yellow
Copy-Item "Graph\*.png" "images\graph\" -Force
Copy-Item "LinearList\*.png" "images\linear-list\" -Force
Copy-Item "Network\*.png" "images\network\" -Force
Copy-Item "SearchingAndSorting\*.png" "images\searching-and-sorting\" -Force
Copy-Item "StackAndQueue\*.png" "images\stack-and-queue\" -Force
Copy-Item "TreeAndBinaryTree\*.png" "images\tree-and-binary-tree\" -Force
Copy-Item "NumericalComputation\*.png" "images\numerical-computation\" -Force
Write-Host "   完成" -ForegroundColor Green

# 4. 提交更改
Write-Host "4. 提交更改..." -ForegroundColor Yellow
git add -A
git commit -m "删除模板文件并添加图片"
Write-Host "   完成" -ForegroundColor Green

# 5. 推送
Write-Host "5. 推送到 GitHub..." -ForegroundColor Yellow
git push origin master
Write-Host "   完成" -ForegroundColor Green

Write-Host "=== 设置完成 ===" -ForegroundColor Green
Write-Host "请访问 https://github.com/MrcsTang/MrcsTang.github.io/settings/pages 配置 GitHub Pages" -ForegroundColor Cyan
```

然后执行：
```powershell
.\setup.ps1
```
