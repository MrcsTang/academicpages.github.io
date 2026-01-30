# MrcsTang's Academic Portfolio - 设置说明

## 已完成的工作

✅ Fork academicpages 模板仓库
✅ 将 blog 文件夹内容转换为博客文章格式
✅ 上传了 7 篇博客文章：
   - 2025-03-17-linear-list.md (线性表)
   - 2025-03-17-stack-and-queue.md (栈和队列)
   - 2025-03-29-tree-and-binary-tree.md (树与二叉树)
   - 2025-04-17-graph.md (图)
   - 2025-05-08-network.md (计算机网络)
   - 2025-05-15-searching-and-sorting.md (查找与排序)
   - 2025-05-22-numerical-computation.md (数值计算)
✅ 更新站点配置文件 _config.yml

## 需要手动完成的步骤

### 1. 删除模板示例文件

在 GitHub 仓库中删除以下文件：
- `_posts/2012-08-14-blog-post-1.md`
- `_posts/2013-08-14-blog-post-2.md`
- `_posts/2014-08-14-blog-post-3.md`
- `_posts/2015-08-14-blog-post-4.md`
- `_posts/2199-01-01-future-post.md`

操作方法：
1. 访问 https://github.com/MrcsTang/academicpages.github.io
2. 进入 `_posts/` 文件夹
3. 点击文件，然后点击"删除"按钮

### 2. 重命名仓库

将仓库名从 `TTTb0521.github.io` 重命名为 `MrcsTang.github.io`

操作方法：
1. 访问 https://github.com/MrcsTang/TTTb0521.github.io
2. 点击 Settings 标签
3. 在 Repository name 字段中，将 `TTTb0521.github.io` 改为 `MrcsTang.github.io`
4. 点击 Rename

### 3. 上传图片文件（可选）

博客文章中引用了图片，需要上传以下文件夹中的图片到仓库的 `images/` 目录：
- `Graph/` → 上传到 `images/graph/`
- `LinearList/` → 上传到 `images/linear-list/`
- `Network/` → 上传到 `images/network/`
- `SearchingAndSorting/` → 上传到 `images/searching-and-sorting/`
- `StackAndQueue/` → 上传到 `images/stack-and-queue/`
- `TreeAndBinaryTree/` → 上传到 `images/tree-and-binary-tree/`
- `NumericalComputation/` → 上传到 `images/numerical-computation/`

操作方法：
1. 在仓库根目录创建 `images/` 文件夹
2. 创建对应的子文件夹
3. 上传图片文件

### 4. 配置 GitHub Pages

1. 访问 https://github.com/MrcsTang/MrcsTang.github.io/settings/pages
2. 在 Source 部分选择 "Deploy from a branch"
3. 选择 branch 为 "master" (或 "main")
4. 点击 Save

### 5. 站点访问

配置完成后，站点将在以下地址可用：
- https://mrcstang.github.io

## 自定义配置

如需进一步自定义站点，编辑 `_config.yml` 文件：
- 修改 `title`: 站点标题
- 修改 `name`: 作者姓名
- 修改 `bio`: 个人简介
- 修改 `location`: 所在地
- 修改 `email`: 邮箱地址
- 修改社交媒体链接

## 本地预览

如需本地预览站点：

```bash
# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve
```

然后访问 http://localhost:4000
