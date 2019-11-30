# PythonExcel
 python pandas ..

- pyinstaller -F *.py, 可以通过黑屏控制台查看错误日志

- 打包时,自定义包会导致打包成功但是程序无法运行的问题, 需要将自定义包都放在同一目录下, 或者增加路径

- 隐性导入无法打包, 可修改 *.spec文件中的 hiddenimports=[&],&替换为隐性导入的包名称, 

- **或者直接在 *.spec文件中 增加 import 缺的包, 编译时使用 pyinstaller *.spec**

 

 
