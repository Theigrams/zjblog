---
layout: post
comments: true
title: "How do I build this blog?"
date: 2021-07-21 12:00:00
tags: blog html
---

> 本文主要介绍了这个博客的搭建过程。

<!--more-->

{:class="table-of-content"}
* TOC
{:toc}


## 前言

为什么要辛辛苦苦自己搭建一个博客呢，主要还是考虑到兼顾美观和实用性。

我的写作流程主要如下：

1. 第一步是写作，使用的书写软件有

   - notion
   - 语雀
   - wolai
   - typora
   - vscode

   其中写作体验最好的是`wolai` 和 `typora`。

2. 写完之后整理修改，然后发布。从笔记的角度来看，notion和wolai无疑都是很好的，但如果从阅读的角度来看，它们又差了点意思。语雀以知识库的形式储存文章，润物细无声地将知识结构化，这给人的阅读体验就非常棒。

但语雀最大的缺点在于写作体验太差，界面样式太丑。对于第一个问题，我一般在typora上书写，然后复制到语雀上发布，缺点是修改和备份比较麻烦；对于第二个问题，我使用[Stylus 插件](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne?hl=zh)，自己写了一个css样式如下，具体可以看我的博客：[语雀样式美化](https://www.yuque.com/hhjs/zj/hiyw4z)，修改之后显示效果倒也还行。

然而语雀更大的问题在于对数学公式的支持太差，除了输入很不方便以外，在windows上的显示也很差劲，无论是web端还是桌面端，公式与正常文字永远都对不齐。由于公式都是用SVG显示，导致我想自己修改也无能为力（也许可以通过修改css实现），这对于数学系的我来说无疑是一个暴击。



最后思来想去，还是用GitHub+markdown的形式比较好，修改和同步都非常方便，在此基础上自动生成博客也方便浏览，最重要的是不用操心图床，域名和服务器的问题。

- Hexo：我之前使用Hexo搭建了博客，但Hexo每次发布之前要输一堆指令，用CL自动化又颇为麻烦，中间徒增一些不稳定因素。
- Hugo：Hugo是一个不错的选择，但暂时还不太熟悉。
- Mkdocs：[OI Wiki](https://oi-wiki.org/) 就是用其搭建的，但这种形式对内容的结构化要求非常高，一些日常笔记放上去会显得不伦不类。
- Jekyll：综合来说这个是最满足要求的，优点是历史悠久比较完善，主题也丰富。缺点是速度比较慢。但最重要的是与GitHub Page无缝衔接，用起来就很舒服。



选择完之后，就是博客的搭建过程。对于主题的选择，我比较喜欢 [Lil'Log](https://lilianweng.github.io/lil-log/) 的样式，因此 fork 下来之后就直接上手修改。



## 博客搭建

### 安装Jekyll

参考：

- [[Jekyll] macOS 安装 Jekyll - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/350462079)
- [Jekyll on macOS  Jekyll • Simple, blog-aware, static sites (jekyllrb.com)](https://jekyllrb.com/docs/installation/macos/)


第一步，安装ruby

```Bash
brew install ruby
```

安装完之后，会有如下提示，因为mac已经预装了2.6 版本的ruby。

![image]({{ '/assets/images/image.png' | relative_url }})

因此，我们要将默认的ruby路径改为新版本的，在重启终端之后，可以看到ruby路径已改变。

```Bash
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.0.0/bin:$PATH"' >> ~/.zshrc
```


![image1]({{ '/assets/images/image1.png' | relative_url }})

第二步，安装jekyll：

```Bash
gem install --user-install bundler jekyll
```


将Jekyll添加到路径，注意这里是 `3.0.0` 而不是 `3.0.2`。

```Bash
echo 'export PATH="$HOME/.gem/ruby/3.0.0/bin:$PATH"' >> ~/.zshrc
```



### 运行Jekyll

```Bash
jekyll new myblog
cd myblog
bundle exec jekyll serve
```

![image2]({{ '/assets/images/image2.png' | relative_url }})

这样 Jekyll 就在本地环境上跑起来了，接下来是进行一些个性化修改，修改过程比较繁琐，这里就略去不提，可以参考以下链接：

[ jekyll markdown语法 - 搜索结果 - 知乎 (zhihu.com)](https://www.zhihu.com/search?type=content&q=jekyll markdown语法)

[博客搭建(四) 使用Jekyll写博客 (watchzerg.github.io)](http://watchzerg.github.io/2015/03/20/jekyll-write-blog.html)



## 效果测试

### 表格

| AI 框架    | 使用人数 | 特性           |
| ---------- | -------- | -------------- |
| tensorflow | 多       | 多在工业界使用 |
| pytorch    | 多       | 学术圈常用     |
| paddle     | 少       | 可以白嫖服务器 |



### 语法高亮

这是 `行内代码`，this is `inline code`.



```python
import torch as tf
print(a)
```



```c++
#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

int main()
{
    int n[10];
    for (int i = 1; i <= 10; i++)
    {
        n[i] = i + 100;
    }
    cout << "Element" << setw(13) << "Value" << endl;
    for (int j = 0; j <= 10; j++)
    {
        cout << setw(7) << j << setw(13) << n[j] << endl;
    }
    return 0;
}
```



### 公式
Using Bayes' rule, we have:

$$
\begin{aligned}
q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0) 
&= q(\mathbf{x}_t \vert \mathbf{x}_{t-1}, \mathbf{x}_0) \frac{ q(\mathbf{x}_{t-1} \vert \mathbf{x}_0) }{ q(\mathbf{x}_t \vert \mathbf{x}_0) } \\
&\propto \exp \Big(-\frac{1}{2} \big(\frac{(\mathbf{x}_t - \sqrt{\alpha_t} \mathbf{x}_{t-1})^2}{\beta_t} + \frac{(\mathbf{x}_{t-1} - \sqrt{\bar{\alpha}_{t-1}} \mathbf{x}_0)^2}{1-\bar{\alpha}_{t-1}} - \frac{(\mathbf{x}_t - \sqrt{\bar{\alpha}_t} \mathbf{x}_0)^2}{1-\bar{\alpha}_t} \big) \Big) \\
&= \exp\Big( -\frac{1}{2} \big( \color{red}{(\frac{\alpha_t}{\beta_t} + \frac{1}{1 - \bar{\alpha}_{t-1}})} \mathbf{x}_{t-1}^2 - \color{blue}{(\frac{2\sqrt{\alpha_t}}{\beta_t} \mathbf{x}_t + \frac{2\sqrt{\bar{\alpha}_t}}{1 - \bar{\alpha}_t} \mathbf{x}_0)} \mathbf{x}_{t-1} + C(\mathbf{x}_t, \mathbf{x}_0) \big) \Big)
\end{aligned}
$$







## 其他问题

### 插入图片

Jekyll 不能在 `_posts` 里新建文件夹，这也意味着插入图片会变得比较困难，参考该链接下的回答：[Jekyll博客中如何用相对路径来加载图片？ - 知乎](https://www.zhihu.com/question/31123165)，最好的方式是使用图床，但考虑到图床的不稳定性，也挺麻烦。我采用的方式是先将在typora中设置将图片保存到 `../assets/images` 文件夹下，然后发布时统一将其替换成 `{{ '/assets/images/diffusion-beta.png' | relative_url }}`，使用正则表达式：

```
\(\.\./assets/images/(.*)\)

({{ '/assets/images/$1' | relative_url }})
```



### 插入目录

使用如下代码：

```
{:class="table-of-content"}
* TOC
{:toc}
```



