# -*- coding: utf-8 -*-
from django.conf import settings
import MySQLdb

DATABASES = settings.DATABASES['default']


# 当进行插入操作时，affect_row=True查看影响行数
# 进行读取操作时，affect_row=False拿到读取结果

def sql_execute(sql, affect_row=False):
    database = MySQLdb.connect(host=DATABASES['HOST'], user=DATABASES['USER'], passwd=DATABASES['PASSWORD'],
                               db=DATABASES['NAME'], charset="utf8")
    cursor = database.cursor()
    cursor.execute(sql)
    if affect_row:
        ct = cursor.rowcount
    else:
        ct = cursor.fetchall()
    cursor.close()
    database.commit()
    database.close()
    return ct

#检测应该导入或注册的数据是否存在
def check_tables(check_list):
    pass


def get_insert_sql(data_dict, table='article'):
    sql_insert = 'insert into ' + table + '('
    sql_keys = ''
    sql_values = ''
    for key, value in data_dict.items():
        sql_keys += '`' + key + '`,'
        sql_values += '"' + value.replace('"', "'") + '",'
    sql_insert = sql_insert + sql_keys[:-1] + ') values (' + sql_values[:-1] + ')'
    return sql_insert


def get_update_sql(pk_id, data_dict, table='article'):
    sql_update = 'update ' + table + ' set '
    for key, value in data_dict.items():
        sql_update += '`' + str(key.encode('utf-8')) + '` = "' + str(value.encode('utf-8')).replace('"', "'") + '",'
    sql_update = sql_update[:-1]
    sql_update += ' where id =' + str(pk_id)
    return sql_update


def get_select_sql(data_list, table='article'):
    sql_select = 'select '
    for key in data_list:
        sql_select += +'`' + key + '`, '
    sql_select = sql_select[:-2]
    sql_select += ' from ' + table
    return sql_select

def get_delete_sql(del_id,table='article'):
    sql_delete= 'delete from'+ table+ 'where id='+str(del_id)
    return sql_delete