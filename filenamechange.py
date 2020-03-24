# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:35:51 2020

@author: AD
"""

#code for homogenizing filenames
import os
import fnmatch

fpath = 'C:/Users/alaka/Desktop/kymo/'
filenames = fnmatch.filter(os.listdir(fpath), '*')
for x in filenames:
    if x[x.index('kymo')-1]=='_':continue
    print 'old name is ', x
    newname=x[:x.index('kymo')]+'_'+x[x.index('kymo'):]
    print 'new name is ', newname
#    newname=x.replace('-','_')
    os.rename(fpath+x,fpath+newname)
    