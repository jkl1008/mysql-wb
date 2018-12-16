from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Site(Base):
    # 表的名字:
    __tablename__ = 'sites'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(255))
    url = Column(String(255))
    

# 初始化数据库连接，'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/test_db')


# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建新User对象:
new_site = Site(id= '24',name='baidu02',url = 'https://www.baidu.com')

# 添加到session,往数据库添加数据
session.add(new_site)

# 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()



#以下是查询数据

# 创建Session:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
site = session.query(Site).filter(Site.id=='5').one()

# 打印类型和对象的name属性:
print('type:', type(site))
print('name:', site.name)

# 关闭Session:
session.close()






