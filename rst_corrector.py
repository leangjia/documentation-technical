# _*_ coding: utf-8 _*_
#!/usr/bin/env python


import sys
import re
import os

def fun(source, sub):
    s = source.replace(sub, "}}L", 1)
    if s == source:
        s = s.replace("}}L", " " + sub).replace("{{R", sub + " ")
        return s
    s = s.replace(sub, "{{R", 1)
    return fun(s, sub)


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print 'Filename needed.'
        return False

    po_filename = args[0]
    print po_filename
    new_po_filename = 'new/' + po_filename
    po_file = open(po_filename,'r')
    new_po_file = open(new_po_filename,'w')
    for line in po_file.readlines():
        if line.startswith('msgstr'):
            line = re.sub(r'\* \*', '**', line)
            line = re.sub(r'[ ]*\*\*[ ]*', '**', line)

            line = fun(line,'**')
            line = fun(line,':')
            line = fun(line,'`')
            line = fun(line, '``')
            line = fun(line, "'")

            line = re.sub(r'[ ]+', ' ', line)
            line = re.sub(r'：', ':', line)
            line = re.sub(r',', '，', line)
            # line = re.sub(r'.', '。', line)

            line = re.sub(r': `', ':`', line)
            line = re.sub(r'` `', '``', line)
            line = re.sub(r'\* \*', '**', line)


        new_po_file.writelines(line)

    new_po_file.close()
    po_file.close()


if __name__ == "__main__":
    try:
        os.mkdir('new')
    except:
        pass

    main()
