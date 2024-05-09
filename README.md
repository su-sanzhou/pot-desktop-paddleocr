<img width="200px" src="public/icon.svg" align="left"/>

# Pot (派了个萌的翻译器)

> 🌈 一个跨平台的划词翻译软件，将linux下面的系统ocr功能从tesseract改成了paddleocr ([QQ 频道](https://pd.qq.com/s/akns94e1r))

![License](https://img.shields.io/github/license/pot-app/pot-desktop.svg)
![Tauri](https://img.shields.io/badge/Tauri-1.5.0-blue?logo=tauri)
![JavaScript](https://img.shields.io/badge/-JavaScript-yellow?logo=javascript&logoColor=white)
![Rust](https://img.shields.io/badge/-Rust-orange?logo=rust&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-yellow?logo=linux&logoColor=white)

<br/>
<hr/>
<div align="center">

<h3>中文 | <a href='./README_EN.md'>English</a></h3>
</div>

# 1.介绍
- 本fork版本将linux下面自带的tesseract引擎换成了paddleocr离线版引擎，因为原来的插件版paddleocr仅支持windows。
- 所以需要安装2个东西，一个是paddle ocr引擎，一个是修改版的pot，其中paddle ocr引擎安装附后，修改的pot版本仅有deb格式，可以从release下载，国内也可以从此下载，应该还是比较快的。
- 如果有更新提醒，记得不要更新，因为更新后就变成原来的tesseract版本了

# 2.安装
## 2.1 安装paddle ocr离线引擎
- 仅验证了debian 12、python3.11.2
```
sudo apt install python3 python3-venv python3-pip
sudo mkdir -v /opt/paddleocr
cd /opt/paddleocr
sudo python3 -m venv .
cd bin
sudo -s #进入root用户
source activate
cd ..
#后面的requirements.txt、pot_ocr.py、pot_ocr.sh、paddleocr.py均在这个库的paddleocr目录下
pip3 install -r requirements.txt -i https://mirror.baidu.com/pypi/simple
exit #退出root 用户
sudo cp -rv pot_ocr.py /opt/paddleocr/ #pot_ocr.py文件在本仓库根目录
chmod a+x pot_ocr.sh
sudo cp -rv pot_ocr.sh /usr/bin/ #pot_ocr.sh也在本仓库根目录
sudo cp -rv paddleocr.py /opt/paddleocr/lib/python3.11/site-packages/paddleocr/ #这个解决了后面发现的bug
```
## 2.2 安装pot
### 2.2.1 安装编译好的deb
- 下载deb包，然后sudo dpkg -i pot_2.7.10_x86-64.deb
### 2.2.2 手动编译
- 安装rust编译环境(Rust >= 1.70.0)
```
curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh
```

- 安装nodejs编译环境(Node.js >= 18.0.0)

```
sudo apt-get install npm
#修改镜像
npm config set registry http://mirrors.cloud.tencent.com/npm/
sudo npm config set registry http://mirrors.cloud.tencent.com/npm/
#安装n包，管理node版本
sudo npm install -g n
#设置n的镜像
export N_NODE_MIRROR=https://mirrors.cloud.tencent.com/nodejs-release/
#获取n最新支持的lts版本
n --lts
#安装Node js的20.13.0版本
sudo n install 20.13.0
```

- 安装pnpm编译环境(pnpm >= 8.5.0)
```
sudo npm install pnpm -g #安装pnpm
pnpm config set registry http://mirrors.cloud.tencent.com/npm/  #设置腾讯镜像

```

- 编译
```
cd pot-desktop-paddleocr
pnpm install
sudo apt-get install -y libgtk-3-dev libwebkit2gtk-4.0-dev libayatana-appindicator3-dev librsvg2-dev patchelf libxdo-dev libxcb1 libxrandr2 libdbus-1-3
pnpm tauri build
``` 
如果正常，应该在pot-desktop-paddleocr/src-tauri/target/release/bundle/deb/下生成了deb文件,就可以
这样安装sudo dpkg -i src-tauri/target/release/bundle/deb/pot_2.7.10_amd64.deb

# 3.发现的bug及解决办法
- bug 如下
```
Traceback (most recent call last):
  File "/opt/paddleocr/pot_ocr.py", line 1, in <module>
    from paddleocr import PaddleOCR,paddleocr
  File "/opt/paddleocr/lib/python3.11/site-packages/paddleocr/__init__.py", line 14, in <module>
    from .paddleocr import *
  File "/opt/paddleocr/lib/python3.11/site-packages/paddleocr/paddleocr.py", line 575, in <module>
    class PaddleOCR(predict_system.TextSystem):
                    ^^^^^^^^^^^^^^
NameError: name 'predict_system' is not defined
```
- 解决办法
参照[这个paddle ocr的pr](https://github.com/PaddlePaddle/PaddleOCR/pull/11847/commits/7585b2e78ab25517dfd9ada6b31bb60fdecfac80)修改/opt/paddleocr/lib/python3.11/site-packages/paddleocr/paddleocr.py即可
# 4.使用及其他
使用方式与原版pot一样，目前仅支持简体中文、繁体中文、英文。


# 5.todo
- 其他语言支持
- 删除deb打包依赖的tesseract-ocr

