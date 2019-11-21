# Load libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import os

# The following section is just for our online class
mpl.use('Agg')
if os.path.exists('graph.png'):
  os.remove('graph.png')

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv('iris.csv', names=names)