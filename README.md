智能数据工程实验报告
====================

- 学院：信息学院
- 专业：电子信息
- 姓名：潘森垒
- 学号：12020215212


> [作业要求](作业要求.md)


## 一、项目名称
基于Mysql关系数据库与gStore图数据库的数据查询对比实验

## 二、项目任务和问题
### 2.1 数据获取

* From Wikidata Dowload JSON.bz2
* 
### 2.2 数据预处理

* 读取前100条JSON_LINE便于数据分析
* 进行Data Laundry 以删除不需要的数据
* Json.dumps 对数据进行整理
* 
### 2.3 Mysql的设计

* 为Mysql设计E-R图
* 将数据存入Mysql
* 设计SQL语句对Mysql进行查询

### 2.4 gStore的设计

* 为gStore生成对应的三元组
* 将数据存入gStore
* 设计Sparql语句对Mysql进行查询

### 2.5 Mysql与gStore对比

* 对关系型数据库和图数据库进行对比

### 2.6 Gui的设计

* 使用C#设计了一款可以进行知识问答的APP

## 三、数据获取

Linux:
* wget https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2

Win10: 
* https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2

## 四、数据分析
* 读取前10000行作为数据源
* 在磁盘空间足够的情况下，可增加数据量大小
* 在方法上是一致的
* 毕竟学习的目的在于学习，而不是折磨

* 整理出10000条qitem进行语义理解
```
python line_10000_load.py --wikidata_path your_bz_path --store_path your_store_path
```

* 整理出所有的Property进行语义理解
```
python find_pid.py --pretreat_path your_bz_path --store_path your_store_path
```

* 通过在线json解析可以看出Q_item的格式如下

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/Qitem.png)
* 与此同时pitem的格式如下

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/Pitem.png)

* 每个P或Q下面有一个claims

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/claims.png)
* claims下包含mainsnak,qualifiers,references
* 然后这三个属性里分别包含如下

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/mainsnak.png)

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/qualifiers.png)

![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/references.png)
## 五、数据预处理

* 数据清洗
* 对qitem进行数据清洗
* 对pid进行数据清洗
* 生成易于理解的英文数据和中文数据

### 将JSON数据整理，得到如下的数据结构图
![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/structure.png)



## 六、Mysql设计
### 完成了数据分析预处理之后，在Mysql设计思路中，采用如下ER图结构。
![avater](https://github.com/Howdy-Personally/tips_of_wikidata/blob/main/db_struct.png)


## 七、gStore的设计


## 八、Mysql与gStore对比


## 九、Gui的设计


## 九、结论和讨论



