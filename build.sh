# !/bin/bash
tx pull -l zh_CN
sphinx-intl build  -p _build/locale/  --locale-dir=locale/  -l zh_CN
make -e SPHINXOPTS="-D language='zh_CN' -D locale_dirs=locale/"  html
