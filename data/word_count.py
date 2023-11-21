from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("SimpleApp").master("spark://spark-master:7077").getOrCreate()

    text_file = spark.sparkContext.textFile("/opt/spark-data/sample.txt")
    counts = text_file.flatMap(lambda line: line.split(" "))\
                .map(lambda word: (word,1)) \
                .reduceByKey(lambda a,b: a+b)
    output = counts.collect()

    for (word, count) in output:
        print(f"{word}: {count}")

    spark.stop()

if __name__ == "__main__":
    main()