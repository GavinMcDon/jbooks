#import os
#import sys
#import warnings

import tensorflow as tf;
#import openai as oa;
#from icecream import ic


print("Num GPUs Available: " + str(len(tf.config.experimental.list_physical_devices('GPU'))))

print("Num CPUs Available: " + str(len(tf.config.experimental.list_physical_devices('CPU'))))
