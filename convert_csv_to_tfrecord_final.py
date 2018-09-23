# convert_csv_to_tfrecord_final.py
import pandas
import tensorflow as tf

# specify the images folder path here
path_to_images = "D:/Anirudh/Python/Mini_Project/tens/train_images/"

# place test and train_labels.csv file in the same folder
# comment one of these 2 lines 
df = pandas.read_csv("D:/Anirudh/Python/Mini_Project/tens/data/train_labels.csv")
#df = pandas.read_csv("D:/Anirudh/Python/Mini_Project/tens/data/test_labels.csv")

def bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

writer = tf.python_io.TFRecordWriter("train.record")
for i in range(len(df)):
    with tf.gfile.Open(path_to_images + df["filename"][i], "rb") as f: 
	    encoded_image = f.read()
    # print(encoded_image)
    example = tf.train.Example(features=tf.train.Features(feature={
        'filename': bytes_feature(encoded_image),
        'width': int64_feature(df['width'][i]),
        'height': int64_feature(df['height'][i]),
        # 'class': bytes_feature(df['class'][i]),
		'class':int64_feature(1),
        'xmin': int64_feature(df['xmin'][i]),
        'ymin': int64_feature(df['ymin'][i]),
        'xmax': int64_feature(df['xmax'][i]),
        'ymax': int64_feature(df['ymax'][i])
    }))
    writer.write(example.SerializeToString())
writer.close()