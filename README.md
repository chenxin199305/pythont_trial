# pythont_trial

本仓库代码用于测试一些 python3.13 free-threading 的特性。

## 环境安装

1. 安装 Miniconda
    - [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 是一个轻量级的 Anaconda 发行版，包含了 conda 和 Python 的最小安装包。
    - 安装 Miniconda 后，可以使用 conda 命令来管理 Python 环境和包。

2. 安装 conda 环境

   ```bash
   conda create -n pythont python=3.13 python-freethreading -c conda-forge
   ```

3. 激活 conda 环境

   ```bash
   conda activate pythont
   ```

4. 安装 JIT 特性

    ```bash
    conda install python-jit
    ```