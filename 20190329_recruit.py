import pymysql
import urllib
import json
import time
import random


# 在sql中创建表
def create_table_mysql():
    db = pymysql.connect(host='localhost', user='root', password='mysqlkey', db='test_db', port=3306)

    # 创建游标对象cursor
    cursor = db.cursor()
    # 执行SQL，如果表存在就删除
    cursor.execute('DROP TABLE IF EXISTS zlzp_sjfx')
    # 创建表
    create_table_sql = """
            CREATE TABLE zlzp_sjfx(
                job_number CHAR(100) COMMENT '记录编号',
                job_type_big_num CHAR(100) COMMENT '职业大分类编号',
                job_type_big_name CHAR(100) COMMENT '职业大分类名称',
                job_type_medium_num CHAR(100) COMMENT '职业细分类编号',
                job_type_medium_name CHAR(100) COMMENT '职业细分类名称',
                company_num CHAR(100) COMMENT '公司编号',
                company_url CHAR(200) COMMENT '公司对应url',
                company_name CHAR(100) COMMENT '公司名称',
                company_size_num CHAR(100) COMMENT '公司规模编号',
                company_size CHAR(100) COMMENT '公司规模',
                company_type_num CHAR(100) COMMENT '公司类型编号',
                company_type CHAR(100) COMMENT '公司类型',
                job_url CHAR(200) COMMENT '职位对应url',
                working_exp_num CHAR(100) COMMENT '工作经验编号',
                working_exp CHAR(100) COMMENT '工作经验',
                edu_level_num CHAR(100) COMMENT '教育水平编号',
                edu_level CHAR(100) COMMENT '教育水平',
                job_salary CHAR(100) COMMENT '工资',
                job_type CHAR(100) COMMENT '工作类型',
                job_name CHAR(100) COMMENT '工作类型',
                job_location_lat CHAR(100) COMMENT '经度',
                job_location_lon CHAR(100) COMMENT '纬度',
                job_city CHAR(100) COMMENT '工作城市',
                job_updatetime CHAR(100) COMMENT '更新时间',
                job_createtime CHAR(100) COMMENT '创建时间',
                job_endtime CHAR(100) COMMENT '结束时间',
                job_welfare CHAR(100) COMMENT '工作福利'
            )"""

    try:
        # 创建表
        cursor.execute(create_table_sql)
        # 提交执行
        db.commit()
        print('table zlzp_sjfx create done')
    except:
        # 回滚
        db.rollback()
        print('table zlzp_sjfx create not done')

    return db, cursor


db, cursor = create_table_mysql()
time_0 = time.time()

for i in range(500):
    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.89067574&x-zp-page-request-id=866368d6313e41c38a6e600b1c5d8082-1545034860140-256948'.format(
        i * 90)
    if i == 0:
        url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&_v=0.89067574&x-zp-page-request-id=866368d6313e41c38a6e600b1c5d8082-1545034860140-256948'

    page = urllib.request.urlopen(url).read()
    data = json.loads(page)
    time.sleep(random.uniform(1.2, 2.1))

    add_sql = """
    INSERT INTO zlzp_sjfx
    (job_number, job_type_big_num, job_type_big_name,job_type_medium_num,job_type_medium_name,company_num,company_url,company_name,
    company_size_num,
    company_size,
    company_type_num,
    company_type,
    job_url,
    working_exp_num,
    working_exp,
    edu_level_num,
    edu_level,
    job_salary,
    job_type,
    job_name,
    job_location_lat,
    job_location_lon,
    job_city,
    job_updatetime,
    job_createtime,
    job_endtime,
    job_welfare)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for each_job in data['data']['results']:
        add_data = (
            each_job['number'],  # 编号
            each_job['jobType']['items'][0]['code'],  # 职业大分类编号
            each_job['jobType']['items'][0]['name'],  # 职业大分类名称
            each_job['jobType']['items'][1]['code'],  # 职业细分类编号
            each_job['jobType']['items'][1]['name'],  # 职业细分类名称
            each_job['company']['number'],  # 公司编号
            each_job['company']['url'],  # 公司对应url
            each_job['company']['name'],  # 公司名称
            each_job['company']['size']['code'],  # 公司规模编号
            each_job['company']['size']['name'],  # 公司规模
            each_job['company']['type']['code'],  # 公司类型编号
            each_job['company']['type']['name'],  # 公司类型
            each_job['positionURL'],  # 职位对应url
            each_job['workingExp']['code'],  # 工作经验编号
            each_job['workingExp']['name'],  # 工作经验
            each_job['eduLevel']['code'],  # 教育水平编号
            each_job['eduLevel']['name'],  # 教育水平
            each_job['salary'],  # 工资
            each_job['emplType'],  # 工作类型
            each_job['jobName'],  # 工作名称
            each_job['geo']['lat'],  # 经度
            each_job['geo']['lon'],  # 纬度
            each_job['city']['display'],  # 工作城市
            each_job['updateDate'],
            each_job['createDate'],
            each_job['endDate'],
            '/'.join(each_job['welfare'])  # 工作福利
        )

        cursor.execute(add_sql, add_data)

    try:
        db.commit()
        print('page', i, 'done!用时', time.time() - time_0)
    except:
        db.rollback()
        print('page', i, 'not done')

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()