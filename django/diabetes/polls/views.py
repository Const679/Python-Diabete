from django.http import HttpResponse
from django.template import loader
import plotly.express as px
import pandas as pd

def index(request):
    template=loader.get_template('template0.html')
    df= pd.read_csv('diabetic_data.csv', delimiter=',')
    nRow, nCol = df.shape
    
    number_medication=pd.DataFrame(df["num_medications"]).groupby("num_medications")["num_medications"].count()
    bar = px.bar(number_medication)
    bar_html=bar.to_html(full_html=False,default_height=500,default_width=700)
    
    time_in_hospital=pd.DataFrame(df["time_in_hospital"]).groupby("time_in_hospital")["time_in_hospital"].count()
    pie = px.pie(time_in_hospital)
    pie_html=pie.to_html(full_html=False,default_height=500,default_width=700)
    
    
    
    context={'leprint':f'The dataframe contains {nRow} rows and {nCol} columns',
    'bar_html':bar_html,
    'pie_html':pie_html,
    }
    
    return HttpResponse(template.render(context,request))
    
    
    

def Table(request):
    df= pd.read_csv('diabetic_data.csv', delimiter=',')
    geeks_object = df.head().to_html()

    return HttpResponse(geeks_object)