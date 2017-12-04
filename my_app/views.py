# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from . import sysInit,excels,utils
# Create your views here.


__checklist=('tbl_stud_info','tbl_subj_info','tbl_suplr_info','tbl_rule_info','tbl_client_info',
             'tbl_vehicle_info','tbl_suplr_subj')

#可能要用的,
def return_response(return_dict):
    response=JsonResponse(**return_dict)
    response["Access-Control-Allow-Origin"] = '*'
    return  response

#从post里面取出数据
def get_valid_dict(src_dict,src_list):
    desc_dict={}
    for i in src_list:
        desc_dict[i]=src_dict.get(i,'null')
    return desc_dict

#将excel转db
def excel2db(request):
    desc_dict = get_valid_dict(request.POST, ['table_name', ])
    excels.excel_dc(desc_dict['table_name'])
    return JsonResponse()

#db导excel
def db2excel(request):
    desc_dict = get_valid_dict(request.POST, ['table_name', ])
    excels.excel_dr(desc_dict['table_name'])
    return JsonResponse()

#初始化一些表
def db_init(request):
    if utils.check_tables(__checklist)==False:
        return JsonResponse()
    sysInit.create_tables()
    return JsonResponse()





