#! /bin/bash

sphinx-intl update -p _build/locale/  --locale-dir=locale/  -l zh_CN

sphinx-intl update-txconfig-resources --pot-dir _build/locale/  --locale-dir=locale/ --transifex-project-name  odoo-documentation-technical
