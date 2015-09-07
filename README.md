# odoo 技术文档 [开发文档]


翻译为中文
===============

工作步骤为

* 翻译 locale/zh_CN/*.po 文件

* 构建或更新 locale/zh_CN/*.mo 文件
  
    sphinx-intl  -p _build/locale/ --locale-dir=locale/  --language  zh_CN  build
    
* 生成中文文档
  
    make html
    
完成以上步骤，就能得到中文版的用户文档
