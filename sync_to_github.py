#!/usr/bin/env python3
"""
批量上传博客文章到 GitHub 仓库
"""
import os
import base64
import json
from pathlib import Path

# 博客文章映射：原始文件 -> 新文件名(带日期)
POSTS = {
    "LinearList.md": ("2025-03-17-linear-list.md", "2025-03-17"),
    "StackAndQueue.md": ("2025-03-17-stack-and-queue.md", "2025-03-17"),
    "TreeAndBinaryTree.md": ("2025-03-29-tree-and-binary-tree.md", "2025-03-29"),
    "Graph.md": ("2025-04-17-graph.md", "2025-04-17"),
    "SearchingAndSorting.md": ("2025-05-15-searching-and-sorting.md", "2025-05-15"),
    "Network.md": ("2025-05-08-network.md", "2025-05-08"),
    "NumericalComputation.md": ("2025-05-22-numerical-computation.md", "2025-05-22"),
}

def convert_front_matter(content: str, title: str, date: str, filename: str) -> str:
    """转换 front matter 为 academicpages 格式"""
    # 移除旧的 front matter
    lines = content.split('\n')
    if lines[0] == '---':
        # 找到下一个 ---
        idx = lines[1:].index('---') + 1
        content = '\n'.join(lines[idx+1:])
    
    # 转换图片路径
    content = content.replace('](LinearList/', '](/images/linear-list/')
    content = content.replace('](StackAndQueue/', '](/images/stack-and-queue/')
    content = content.replace('](Graph/', '](/images/graph/')
    content = content.replace('](Network/', '](/images/network/')
    content = content.replace('](SearchingAndSorting/', '](/images/searching-and-sorting/')
    content = content.replace('](TreeAndBinaryTree/', '](/images/tree-and-binary-tree/')
    content = content.replace('](NumericalComputation/', '](/images/numerical-computation/')
    
    # 构建新的 front matter
    slug = filename.replace('.md', '').replace(' ', '-').lower()
    new_front_matter = f"""---
title: '{title}'
date: {date}
permalink: /posts/{date[:4]}/{date[5:7]}/{slug}/
tags:
  - 数据结构与算法
categories:
  - 数据结构与算法
---

"""
    return new_front_matter + content

def main():
    for original_file, (new_file, date) in POSTS.items():
        filepath = Path(original_file)
        if not filepath.exists():
            print(f"跳过: {original_file} 不存在")
            continue
            
        content = filepath.read_text(encoding='utf-8')
        title = filepath.stem
        
        # 转换
        new_content = convert_front_matter(content, title, date, new_file)
        
        # 保存到 _posts 目录
        posts_dir = Path("_posts")
        posts_dir.mkdir(exist_ok=True)
        output_path = posts_dir / new_file
        output_path.write_text(new_content, encoding='utf-8')
        print(f"已转换: {original_file} -> {new_file}")

if __name__ == "__main__":
    main()
