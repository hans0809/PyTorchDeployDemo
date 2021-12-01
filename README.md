# PyTorchDeployDemo

代码引用自PyTorch官方教程。

在此基础上，添加了图像保存到服务器的功能，并能够将待预测图像同时展示在了输出界面上。
![](res.png)

本想部署到heroku，结果压缩后内存超过了500兆(压缩前，torch库自己就占了800多兆)，免费版好像带不动了(限制500兆)。

![log.png](log.png)
