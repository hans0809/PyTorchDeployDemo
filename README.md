# PyTorchDeployDemo

代码引用自PyTorch官方教程。

在此基础上，添加了图像保存到服务器的功能，并能够将待预测图像展示在输出界面上。
![](res.png)

本想部署到heroku，结果压缩后内存超过了500兆(压缩前，torch库自己就占了800多兆)，免费版好像带不动了(限制500兆)。

![log.png](log.png)

更多介绍见公众号原文：

https://mp.weixin.qq.com/s?__biz=MzU0NzQwMzU1Mw==&mid=2247488308&idx=1&sn=04da5fe6ee51344ff484bad9b9952e5e&chksm=fb4fb17acc38386c1a92ccd09896cb254d8db2edfa58db3696dbb43c5b284c8e6c8a74ab40c2&token=2050082509&lang=zh_CN#rd
