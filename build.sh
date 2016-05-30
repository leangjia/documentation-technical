# !/bin/bash
tx pull -l zh_CN --mode developer
make -e SPHINXOPTS="-D language='zh_CN' -D locale_dirs=locale/"  html
