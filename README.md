# 驾校基站稳定性测试工具
---

## 一. 说明

1. 使用的第三方库: numpy, pandas, matplotlib, pyqt5

2. 程序不定期更新, 恕不另行通知

3. 使用说明请下载 <<驾校基站稳定性测试工具使用说明.docx>>



----
## 二. 笔记
- pyinstaller -F *.py, 可以通过黑屏控制台查看错误日志

- 打包时,自定义包会导致打包成功但是程序无法运行的问题, 需要将自定义包都放在同一目录下, 或者增加路径

- 隐性导入无法打包, 可修改 *.spec文件中的 hiddenimports=[&],&替换为隐性导入的包名称, 

- 或者直接在 *.spec文件中 增加 import 缺的包, 编译时使用 pyinstaller *.spec

 

 
