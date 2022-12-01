from django.http import HttpResponse
from django.template import loader

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as snb
from sklearn.preprocessing import LabelEncoder

def index(request):
    template=loader.get_template('template0.html')
    df= pd.read_csv('diabetic_data.csv', delimiter=',')
    nRow, nCol = df.shape
    fig=plt.figure(figsize=(16,8))
    corr_matrix = df.corr()
    snb.heatmap(corr_matrix)
    plot_html=fig.to_html(full_html=False,default_height=500)
    context={'leprint':f'There are {nRow} rows and {nCol} columns',
    'plot_html':plot_html}
    return HttpResponse(template.render(context,request))