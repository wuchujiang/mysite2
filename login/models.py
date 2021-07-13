from django.db import models

# Create your models here.

'''
创建学生模型
'''

class Student(models.Model):
    # 学号
    studentNum = models.CharField('学号',primary_key=True, max_length=15)

    # 姓名
    name = models.CharField('姓名', max_length=20)

    # 年龄
    age = models.IntegerField('年龄', null=False)

    # 性别
    sex = models.BooleanField('性别', default=True)

    # 手机
    mobile = models.CharField('手机', unique=True, max_length=15)

    # 创建时间
    createTime = models.DateTimeField(auto_now_add=True)

    # 修改时间
    modifyTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Student'


"""
学生社团信息
"""
class StudentUnion(models.Model):

    # 自增主键
    id = models.IntegerField(primary_key=True)

    # 社团名称
    unionName = models.CharField('社团名称', max_length=20)

    # 社团人数
    unionNum = models.IntegerField('人数', default=0)

    # 社团负责人
    unionRoot = models.OneToOneField(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student_union'

"""
OneToOneField： 一对一
ForeignKey: 一对多
ManyToManyField： 多对多(没有ondelete 属性)
"""

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)
    anthors = models.ManyToManyField('Author')

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    gender_choices = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)

class Dep(models.Model):
    title = models.CharField(max_length=32)




