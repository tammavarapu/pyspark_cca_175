pyspark --master yarn --conf spark.ui.port=12888

sc
exit()

mkdir /sparkdemo/pythondemo/
cd /sparkdemo/pythondemo/

# create file InitializeSparkJob.py
from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName('Initialize Job').setMaster('yarn-client').set('spark.ui.port','12888')
sc = SparkContext(conf = conf)


pyspark --master yarn --conf spark.ui.port=12888 InitializeSparkJob.py



