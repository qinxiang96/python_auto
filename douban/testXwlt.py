#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   testXwlt.py
@Time    :   2025/01/05 18:00:58
@Author  :   qinxiang 
@Version :   1.0
@Site    :   https://github.com/qinxiang96
@Desc    :   None
'''

import xlwt
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')
workbook.save('student.xls')