# odoo 技术文档 [开发文档]


翻译为中文
===============

工作步骤为

* 翻译 locale/zh_CN/*.po 文件
 
* 或者在 transifex 平台翻译 https://www.transifex.com/odoo-cn/odoo-documentation-technical/dashboard/

* 从 transifex 下载翻译
    tx pull -l zh_CN 

* 生成中文文档
  
    bash build.sh
    
完成以上步骤，就能得到中文版的用户文档
