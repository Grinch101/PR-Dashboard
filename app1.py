import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
import pandas as pd
import dash_table
import plotly.figure_factory as ff
import numpy as np
import time
 
  
Update = str(pd.Timestamp.today().date())

########
## Look at global data:
#######


# ### COVID ################################################
# # Global_Death1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
# Global_Death1 = pd.read_csv('time_series_covid19_deaths_global.csv')


# # Global_Confirmed1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
# Global_Confirmed1 = pd.read_csv("time_series_covid19_confirmed_global.csv")


# Countries_Confirmed = pd.DataFrame(Global_Confirmed1.groupby(by = 'Country/Region').sum())
# Countries_Death = pd.DataFrame(Global_Death1.groupby(by = 'Country/Region').sum())

# Countries_Confirmed.drop(['Lat',"Long"],axis=1,inplace=True)
# Countries_Death.drop(['Lat',"Long"],axis=1,inplace=True)

# Countries_Confirmed = Countries_Confirmed.transpose()
# Countries_Death = Countries_Death.transpose()

# # Countries_Confirmed.sort_index(inplace=True)
# # Countries_Death.sort_index(inplace=True)

# Countries = Countries_Death.join(Countries_Confirmed, lsuffix='_Death')

# #Countries.sort_index(inplace=True,axis=1)


# Countries.reset_index(inplace=True)
# Countries['Time'] = pd.to_datetime(Countries["index"])
# Countries.set_index('Time',inplace=True)

# Countries.drop('index' , axis=1 , inplace=True)
# Country_names = list(Countries_Confirmed.columns)
# for i in Country_names:

#     Countries[f"{i}_Rate"] = Countries[f'{i}_Death'] / Countries[f'{i}']
    
    
# Countries.sort_index(inplace=True, axis=1)
# Countries.fillna(0,inplace=True)
# country_names = list(Countries_Confirmed.columns)

# Country_cols = pd.MultiIndex.from_product([country_names, ['Confirmed', 'Death','Rate']],
#                                        names=["Region","Values"])

# Countries.columns = Country_cols
# #Countries.sort_index(inplace=True,axis=1)
# #del Countries_Confirmed
# #del Countries_Death
# #del Country_cols
# Countries.rename(mapper={'US':"United States"},axis=1,inplace=True)

# #Countries.tail(4)


# #import pandas as pd


# # df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
# # df = pd.read_csv("time_series_covid19_confirmed_global.csv")

# df = Global_Confirmed1
# df = df.groupby('Country/Region').sum()

# df = df.reset_index()

# date_lists=[]
# for i in df.columns:
#     if i not in [ 'Country/Region', 'Lat', 'Long']:
#         date_lists.append(i)

# mylist=[]        
# for i in date_lists:

#     dftemp = df[[ 'Country/Region', 'Lat', 'Long']].copy()
#     dftemp["Confirmed"] = df[i].copy()
#     dftemp["Date"] = pd.to_datetime(i,dayfirst=False,format='%m/%d/%y')
#     mylist.append(dftemp)
    
# df_glob_conf= pd.concat(mylist)
# df_glob_conf= df_glob_conf.sort_values(by=['Country/Region','Date'])


# # df =pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
# df = Global_Death1
# # df = pd.read_csv("time_series_covid19_deaths_global.csv")
# df = df.groupby('Country/Region').sum()

# df = df.reset_index()
# date_lists=[]
# for i in df.columns:
#     if i not in ['Country/Region', 'Lat', 'Long']:
#         date_lists.append(i)

# mylist=[]        
# for i in date_lists:

#     dftemp = df[['Country/Region', 'Lat', 'Long']].copy()
#     dftemp["Death"] = df[i].copy()
#     dftemp["Date"] = pd.to_datetime(i,dayfirst=False,format='%m/%d/%y')
#     mylist.append(dftemp)
    
# df_glob_death= pd.concat(mylist)
# df_glob_death= df_glob_death.sort_values(by=['Country/Region','Date'])


# df_globe = df_glob_conf.merge(df_glob_death)
# # df_globe = df_globe.drop("Province/State",axis=1)
# df_globe["Country/Region"] = df_globe["Country/Region"].replace("US",'United States')
# df_pop = pd.read_csv('population_by_country_2020.csv')
# # df_pop = pd.read_csv('https://raw.githubusercontent.com/Grinch101/population-by-country/master/population_by_country_2020.csv')

# df_pop.set_index('Country (or dependency)',inplace=True)
# pop_dic = df_pop.to_dict()['Population (2020)']
# df_globe['Population'] = df_globe['Country/Region'].map(pop_dic)
# df_globe["Country/Region"] = df_globe["Country/Region"].replace("US",'United States')

# # del df_pop
# # del df_glob_conf
# # del df_glob_death

# #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
# df = pd.read_csv('2014_world_gdp_with_codes.csزیv')

# df.drop('GDP (BILLIONS)',axis=1,inplace=True) # we need countrycodes ... 
# df.set_index('COUNTRY',inplace=True)
# country_codes = df.to_dict()['CODE']


# df_globe['CODE'] = df_globe['Country/Region'].map(country_codes)
# df_globe['Death'] = abs(df_globe['Death'])
# df_globe['Confirmed'] = abs(df_globe['Confirmed'])


# #lat_long = pd.read_csv("time_series_covid19_deaths_global.csv")
# #lat_long = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
# lat_long = Global_Death1
# lat_long = lat_long.set_index('Country/Region')

# lat_long_dict = lat_long.to_dict()


# df_globe['Lat'] = df_globe['Country/Region'].map(lat_long_dict['Lat'])
# df_globe['Long'] = df_globe['Country/Region'].map(lat_long_dict['Long'])


colors = {'Wait time': 'rgb(240,240,240)',   # middle gray
                'AOR':'#d62728',             # brick red
              'Ghost':'rgb(255,125,0)',      # curry yellow-green
         'Additional':'#6600cc',        # blue-teal
   'Eligibility Pass':'rgb(0,255,255)',      # chestnut brown
     'Eligibility RR':'rgb(0,220,220)', 
    'Eligibility Met':'rgb(20,230,230)',
   "Security Started":'rgb(0,255,0)',        # cooked asparagus green
   'Criminality Pass':'rgb(204,255,153)',    # safety orange.
#                 'PPR':'rgb(212,175,55)',     # Metalic Gold
                'PPR': 'rgb(0,0,0)'
         }


df = pd.read_csv('EE or CEC.csv')

#df = pd.read_excel('https://github.com/Grinch101/PR/blob/master/EE%20or%20CEC.xlsx?raw=true')
df.fillna(999,inplace=True)
df = df[df["Task"] != 0]
df = df[df["Task"] != '0']
df = df[df["Task"] != 999]
df = df[df["Task"] != '999']
df = df[['Task','Start','Finish','Resource','Visa Office']]


df = df.reset_index()
df.drop('index',axis=1,inplace=True)
df['Description'] = df['Resource']

df.sort_values('Start',ascending=True,inplace=True)

df = df.set_index('Task')
df = df.reset_index()

df_annot=df[(df['Resource']=='Eligibility Pass') | (df['Resource']=='Security Started') | (df['Resource']=='Criminality Pass')]
df['annotation'] = 0
df_annot['annotation'] = 'Note'

df = pd.concat([df,df_annot],axis=0)
df.fillna(999)

# df['Start'] = df['Start'].apply(lambda x: x.date())
# df['Finish'] = df['Finish'].apply(lambda x: x.date())
df['Task'] = df['Task'].apply(lambda x: str(x).split(" ")[0])
df['Finish'] = df['Finish'].apply(lambda x: pd.Timestamp(x))
df['Start'] = df['Start'].apply(lambda x: pd.Timestamp(x))
df['Visa Office'].fillna('?',inplace=True)
df['Visa Office'].replace(0,'?',inplace=True)
df['Visa Office'].replace('0','?',inplace=True)
df['Visa Office'].replace(' ','?',inplace=True)
df['Visa Office'].replace(999,'?',inplace=True)

df.sort_values('Start',ascending=True,inplace=True)


df_pivot = pd.pivot_table(data=df[["Task","Start","Resource","Visa Office","Description"]],values=['Start'],columns=['Resource'],index='Task',aggfunc='min')
df_pivot2 = pd.pivot_table(data=df[["Task","Start","Resource","Visa Office","Description"]],values=['Visa Office'],columns=['Description'],index='Task',aggfunc='min')

df_pivot2 = pd.DataFrame(df_pivot2.xs(('Visa Office','AOR'),axis=1))

df_pivot = df_pivot.join(df_pivot2,on='Task')

df_pivot.columns = ['AOR','Additional','Criminality Pass','Eligibility Met','Eligibility Pass','Eligibility RR','Ghost','PPR','Security Started','Wait time','Visa Office']
df_pivot.reset_index(inplace=True)
df_pivot.columns= ['ID','AOR','Additional','Criminality Pass','Eligibility Met','Eligibility Pass','Eligibility RR','Ghost','PPR','Security Started','Wait time','Visa Office']
df_pivot.drop(['Wait time'],inplace=True,axis=1)
df_pivot = df_pivot[['ID',"AOR","Ghost","Additional","Criminality Pass",'Eligibility Met',"Eligibility Pass","Eligibility RR","Security Started","Visa Office","PPR"]]


# df_pivot['PPR']=df_pivot['PPR'].apply(lambda x: str(x).split(" ")[0])
# df_pivot['AOR']=df_pivot['AOR'].apply(lambda x: str(x).split(" ")[0])

df_pivot['Wait on PPR'] = df_pivot['PPR'] - df_pivot['AOR']

# df_pivot['Wait on PPR']=df_pivot['Wait on PPR'].apply(lambda x: str(x).split(" ")[0])

df_pivot = df_pivot.sort_values(by='Wait on PPR')
df_pivot.set_index('ID',inplace=True)
df_pivot.reset_index(inplace=True)
# df_pivot['Wait on PPR'] = df_pivot['Wait on PPR'].apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')


del df_pivot2
df_pivot['Visa Office'] = df_pivot['Visa Office'].fillna(999)

df_pivot['Visa Office'].unique()
df_pivot['Visa Office'].replace(999,'?',inplace=True)


# create main Gantt Chart


gantt_main = ff.create_gantt(df,group_tasks= True,colors = colors, 
                      index_col="Resource",bar_width=0.4,
                      show_colorbar=True,show_hover_fill = False,showgrid_x=True, showgrid_y=True)

gantt_main.update_layout(
                    title = f'Gantt Chart for ALL applications (EE, FSW and CEC) - Updated on {Update} ',
#                     width = 1200,
                    height=1700,
                    hovermode="closest")

gantt_main.update_layout(xaxis = {"title": 'Date',
 #                          'range':("2019-11-01", "2020-04-30"),
                          },
                 yaxis = {"title": "Applicants"},
#                 annotations=[
#         dict(
#             x=str(df[df['annotation']=='Note'].iloc[i]['Start']).split()[0],
#             y=fig['layout']['yaxis']['ticktext'].index(df[df['annotation']=='Note'].iloc[i]['Task']),
# #             xref="x",
# #             yref='paper',
#             text= "Note/Webform",
#             showarrow=True,
#             arrowhead=5,
#             ax=0,
#             ay=-40 * -(i+1)
#         ) for i in range(len(df[df['annotation']=='Note']))
#     ]
                 
                 )

# Add range slider

# fig.update_layout(
#     xaxis=dict(
#         rangeselector=dict(),
#         rangeslider=dict(visible=True ),
#         type="date")
# )                       



###### Create Gantt Chart for PPR applicants only:


list1 = []
for i in df['Task'].unique():
    if 'PPR' in df[df['Task']==i]['Resource'].unique():
        list1.append(df[df['Task']==i])

df_ppr = pd.concat(list1)
# df_ppr # for ppr only


gantt2 = ff.create_gantt(df_ppr,group_tasks= True,colors = colors, 
                      index_col="Resource",bar_width=0.4,
                      show_colorbar=True,show_hover_fill = False,showgrid_x=True, showgrid_y=True)

gantt2.update_layout(
                    title = f'Gantt Chart for issued PPRs  (EE, FSW and CEC) - Updated on {Update}',
#                     width = 1200,
                    height=1300,
                    hovermode="closest")

gantt2.update_layout(xaxis = {"title": 'Date',
 #                          'range':("2019-11-01", "2020-04-30"),
                          },
                 yaxis = {"title": "Applicants"},
#                 annotations=[
#         dict(
#             x=str(df_ppr[df_ppr['annotation']=='Note'].iloc[i]['Start']).split()[0],
#             y=fig['layout']['yaxis']['ticktext'].index(df_ppr[df_ppr['annotation']=='Note'].iloc[i]['Task']),
# #             xref="x",
# #             yref='paper',
#             text= "Note/Webform",
#             showarrow=True,
#             arrowhead=5,
#             ax=0,
#             ay=-40 * -(i+1)
#         ) for i in range(len(df_ppr[df_ppr['annotation']=='Note']))
#     ]
                 
                 )



# gantt2.update_layout( ## Add range slider
#     xaxis=dict(
#         rangeselector=dict(),
#         rangeslider=dict(visible=True ),
#         type="date")
# )        


######## Gantt for in-progress Applications
A= list(df['Task'].unique()) # people who got PPR
for i in list(df_ppr['Task'].unique()):
    A.remove(i) # people who didn't get PPR yet
    
list2 = []
for i in A:
    list2.append(df[df['Task']==i])
    
df_in_process = pd.concat(list2) # df for these people
## df for in progress applicants


gantt3 = ff.create_gantt(df_in_process,group_tasks= True,colors = colors, 
                      index_col="Resource",bar_width=0.4,
                      show_colorbar=True,show_hover_fill = False,showgrid_x=True, showgrid_y=True)

gantt3.update_layout(
                    title = f'Gantt Chart for in-progress applications only  (EE, FSW and CEC) - Updated on {Update}',
#                     width = 1200,
                    height=1100,
                    hovermode="closest")

gantt3.update_layout(xaxis = {"title": 'Date',
 #                          'range':("2019-11-01", "2020-04-30"),
                          },
                 yaxis = {"title": "Applicants"},
#                 annotations=[
#         dict(
#             x=str(df_in_process[df_in_process['annotation']=='Note'].iloc[i]['Start']).split()[0],
#             y=fig['layout']['yaxis']['ticktext'].index(df_in_process[df_in_process['annotation']=='Note'].iloc[i]['Task']),
# #             xref="x",
# #             yref='paper',
#             text= "Note/Webform",
#             showarrow=True,
#             arrowhead=5,
#             ax=0,
#             ay=-40 * -(i+1)
#         ) for i in range(len(df_in_process[df_in_process['annotation']=='Note']))
#     ]
                 
                 )

# gantt3.update_layout( ## Range Slider
#     xaxis=dict(
#         rangeselector=dict(),
#         rangeslider=dict(visible=True ),
#         type="date")
# )        


for i in [ 'AOR', 'Ghost', 'Additional', 'Criminality Pass',
       'Eligibility Pass', 'Eligibility RR', 'Security Started',
       'PPR']:
    df_pivot[i] = df_pivot[i].apply(lambda x: x.date())


###### New DataFrame:
# find last update:

list_per = {}

for i in df_pivot['ID'].unique():

    A = df_pivot[df_pivot['ID']==i][["AOR","Ghost","Additional","Criminality Pass","Eligibility Pass","Eligibility RR","Security Started","PPR"]].fillna(pd.to_datetime(0).date())
    B = A.reset_index().drop('index',axis=1)
    C = B.transpose().reset_index()
    D = C.set_index(0)
    E = D.index.max()
    max_title = D.loc[E].values[0]
    list_per[i]=max_title

    
df_pivot['Last Status'] = df_pivot['ID']


list_per['NedaS'] = "Criminality Pass" #problematic values
list_per['Mona'] = 'Eligibility Pass'

df_pivot['Last Status'] = df_pivot['Last Status'].map(list_per)

#df_pivot.to_csv('TEST.csv')
#### Change dataframe for SUNBURST

df_sun = df_pivot.copy()
df_sun = df_sun[['ID','AOR','Visa Office','Wait on PPR',"Last Status"]]
df_sun['Wait on PPR'] = df_sun['Wait on PPR'].apply(lambda x : str(x).split(" ")[0])
df_sun['Wait on PPR'] = df_sun['Wait on PPR'].replace('NaT',0)
df_sun['Wait on PPR'] = df_sun['Wait on PPR'].apply(lambda x : int(x))
df_sun['AOR'] = df_sun['AOR'].apply(lambda x: pd.Timestamp(x))

map_wait = {}
for i in df_sun['ID'].unique():

    if df_sun[df_sun['ID']==i]['Wait on PPR'].values[0] == 0:
        wait_time =  pd.Timestamp.today().date() - pd.Timestamp(df_sun[df_sun['ID']==i]['AOR'].values[0]).date()
        map_wait[i] = wait_time
        
        
df_sun['Wait'] = df_sun['ID'].map(map_wait)
df_sun['Wait'] = df_sun['Wait'].apply(lambda x : str(x).split(" ")[0])
df_sun['Wait'] = df_sun['Wait'].replace('NaT',0)
df_sun['Wait'] = df_sun['Wait'].apply(lambda x : int(x))


df_sun['Wait'] = df_sun['Wait'] + df_sun['Wait on PPR']

df_sun.drop('Wait on PPR',axis=1,inplace=True)

mapper = {'AOR':'In-Progress',
'Additional':'In-Progress',
'Ghost':'In-Progress',
 'Eligibility Pass':'In-Progress',
"Eligibility RR":'In-Progress',
"Eligibility Met":'In-Progress',      
'Security Started':'In-Progress',
'Criminality Pass':'In-Progress',
'PPR':'PPR'}




df_sun['Last Status'] = df_sun['Last Status'].apply(lambda x: str(x))
df_sun['Current Status'] = df_sun['Last Status'].map(mapper)
df_sun = df_sun[['ID','Visa Office','Wait','Current Status','AOR']]


###### Plot Sunburst (universal): sun_u


#df_sun['Visa Office'].replace('?'," ",inplace=True)
import plotly.express as px
df_sun['Days'] = "days <br>Visa Office: "+df_sun['Visa Office'].astype(str)+'<br>'+df_sun['Current Status']
sun_u= px.sunburst(df_sun, path=['Current Status','Visa Office', 'ID'], values='Wait',
                  color='Wait',
                  color_continuous_scale='reds',
                  color_continuous_midpoint=0,
                  hover_name='Days',
                 )

sun_u.data[0]['hovertemplate'] = ""

sun_u.update(layout_coloraxis_showscale=False)
sun_u.update_layout(
#     width=800,
    height=700
)
sun_u.update_layout(margin=dict(t=65, b=50, r=80 ,l=80))
sun_u.update_layout(

    title="Universal Chart",
    titlefont= {"size": 36})

sun_u.update_traces(
        branchvalues='total',
        insidetextorientation='radial', 
    
    )


################################### Sunburst for PPR holders

## ############################# Sunburst for people waiting


####### plot sunburst (visa Offices): sun_vo


 ###### plot sunburst (situation of people): sun_s



################# Histogram for PPR (box plot): box

from plotly.subplots import make_subplots

###############

color1 = ['#17becf',
 '#bcbd22',
 '#7f7f7f',
 '#e377c2',
 '#8c564b',
 '#9467bd',
 '#d62728',
 '#2ca02c',
 '#ff7f0e',
 '#1f77b4']

color2 = ['#17becf',
 '#bcbd22',
 '#7f7f7f',
 '#e377c2',
 '#8c564b',
 '#9467bd',
 '#d62728',
 '#2ca02c',
 '#ff7f0e',
 '#1f77b4']
df_temp2 = df_sun
vo_list = sorted(list(df['Visa Office'].unique() ))


box = make_subplots(rows=1,cols=2,
#                    shared_yaxes=True,
                   subplot_titles=['Finished Applications','In-Progress Applications'])

for i in vo_list:
    box.add_trace( go.Box(y=df_temp2[(df_temp2['Current Status']=='PPR') & (df_temp2['Visa Office']==i)]['Wait'],
               name=i,
               jitter=0.3,boxpoints='all',
               fillcolor =color1.pop() ,
               marker=dict(
                size=3,
                color='rgb(0, 0, 0)' ),
               text=df_temp2[(df_temp2['Current Status']=='PPR') & (df_temp2['Visa Office']==i)]['ID'])   ,row=1,col=1)

for i in vo_list:
    box.add_trace( go.Box(y=df_temp2[(df_temp2['Current Status']=='In-Progress') & (df_temp2['Visa Office']==i)]['Wait'],
               name=i,
               jitter=0.3,boxpoints='all',
               fillcolor =color2.pop() ,
               marker=dict(
                size=3,
                color='rgb(0, 0, 0)' ),
               text=df_temp2[(df_temp2['Current Status']=='In-Progress') & (df_temp2['Visa Office']==i)]['ID'])   ,row=1,col=2)



box.update_layout(showlegend=False)    
box.update_layout(
#             width=800,
            height=600,
            title = 'Performances of Visa Offices',
#                 xaxis=dict(title='Visa Offices'),
                yaxis=dict(title='Number of Days')
    
)





################## small statistcal tables:
df_temp2 = df_sun.set_index('ID')
wait_time = df_temp2[df_temp2['Current Status']=='In-Progress']['Wait']
ppr_time = df_temp2[df_temp2['Current Status']=='PPR']['Wait']

##### box plot : box2
import plotly.graph_objects as go

box2 = go.Figure()

box2.add_trace(go.Box(y=ppr_time,name='Distribution of PPR length',
                     jitter=0.3,boxpoints='all',
                     text=ppr_time.index
                    )
             )


box2.add_trace(go.Box(y=wait_time,name='Distribution of In-Progress time',
                     jitter=0.4,boxpoints='all',
                     text=wait_time.index
                    )
             )



box2.update_layout(showlegend=False)    
box2.update_layout(
#     width=600,
            height=600,
            title = 'Wait time distribution based on current status of applications',
                xaxis=dict(title=''),
                yaxis=dict(title='Number of Days Waiting')
    
)

box2.update_layout(
    shapes=[
        # 1st highlight during Feb 4 - Feb 6
        dict(
            type="rect",
            # x-reference is assigned to the x-values
            xref="paper",
            # y-reference is assigned to the plot paper [0,1]
            yref="y",
            x0=0,
            y0=0,
            x1=1,
            y1=180,
            fillcolor="green",
            opacity=0.2,
            layer="below",
            line_width=0,
        ),

    ],
    annotations=[
        dict(
            text="End of 6 Months<br>'Standard Processing Time' ",
            showarrow=True,
            arrowhead=5,
            xref="paper",
            yref='y',
            x=1,
            y=180,
            ax = 1,
            ay=-200,
            
        )
    ]
)
box2.update_layout(margin=dict(t=65, b=50, r=280 ,l=280))
box2.update_layout(
    title="Timeline Distribution",
    titlefont= {"size": 36})




####### make df_pivot ready for Table

BB = df_pivot[df_pivot['Last Status']=='PPR']
BB['Wait'] = BB['Wait on PPR']
BB.sort_values('Wait on PPR',axis=0,inplace=True)
AA = df_pivot[df_pivot['Last Status']!='PPR']
AA['Wait'] = pd.Timestamp.today().date() - AA['AOR']
AA.sort_values('Wait',axis=0,inplace=True,ascending=False)
AA['Wait']=AA['Wait'].apply(lambda x: 'Has been waiting '+str(x).split(" ")[0]+" days so far") 
BB['Wait']=BB['Wait'].apply(lambda x:  'Waited '+str(x).split(" ")[0]+" days")

CC = pd.concat([BB,AA])
CC.drop('Wait on PPR',axis=1,inplace=True)
CC.sort_values(by='PPR',ascending=False,inplace=True)
CC.reset_index(inplace=True)
CC.drop('index',axis=1,inplace=True)
CC.reset_index(inplace=True)
CC['index'] = CC['index'] + 1
df_table = CC
df_table


############# story telling


##################### Normal Curve


########################


# # tempz = make_subplots(cols=1,rows=2,shared_xaxes=True,vertical_spacing=0.001)
# #+++++++++++++++++++++++
# time.sleep(1)

# #     feature = ['Confirmed','Death']
# feature = ['Confirmed']
# country =['Canada']

# mode='group'

# tempz = make_subplots(cols=1,rows=2,shared_xaxes=True,vertical_spacing=0.001)

# #     colors=['red','blue']
# #     for i in feature:
# #         for j in country:
# #             fig.add_trace(go.Bar(x = Countries.index, y = Countries[j][i],hovertext=f'{i}<br>in {j} ' ,
# #                                  name = f'Cumulative {i} in {j}',
# #                                 marker_color=colors.pop()),col=1,row=2      )
# #             fig.update_layout( barmode=mode )

# colors=['red','blue']
# # for i in feature:
# for j in country:
#     i = 'Confirmed'
#     tempz.add_trace(go.Bar(x = Countries.index, y = Countries.diff()[j][i],hovertext=f'{i}<br>in {j}' ,
#                          name = f'Daily {i} in {j}',
#                         marker_color=colors.pop()),col=1,row=1      )
#     tempz.update_layout( barmode=mode )

# for j in country:
#     tempz.add_trace(go.Scatter(x=Countries.index, y = Countries.diff()[j][i].rolling(window=7).mean(),
#                              mode='markers',
#                              marker=dict(color='black',
#                                          size=1),
#                         hovertext=f'Confirmed cases<br>in {j} ',
#                         name = f'weekly average of confirmed cases in {j}',
#                         ))


# for j in country:
#     i = 'Death'
#     tempz.add_trace(go.Bar(x = Countries.index, y = Countries.diff()[j][i],hovertext=f'{i}<br>in {j}' ,
#                          name = f'Daily {i} in {j}',
#                         marker_color=colors.pop()),col=1,row=2      )
#     tempz.update_layout( barmode=mode )

# for j in country:
#     tempz.add_trace(go.Scatter(x=Countries.index, y = Countries.diff()[j][i].rolling(window=7).mean(),
#                              mode='markers',
#                              marker=dict(color='black',
#                                          size=1),
#                         hovertext=f'Fatility cases<br>in {j} ',
#                         name = f'weekly average of fatality cases in {j}',
#                         ), col=1,row=2 )


# tempz.update_layout(
#     hovermode='x',
#     autosize=True,
#     showlegend=False,
#     margin=go.layout.Margin(
#     l=35, #left margin
#     r=0, #right margin
#     b=35, #bottom margin
#     t=55, #top margin
#     )
#     )


# tempz.update_layout(title_text=f"Confirmed cases (up) and Fatality cases (down) of COVID-19 in {country[0]}")


#+++++++++++++++++++++++
# feature = ['Confirmed','Death']
# colors=['red','blue']
# country=['Canada']
# mode='group'
# for i in feature:
#     for j in country:
#         tempz.add_trace(go.Bar(x = Countries.index, y = Countries[j][i],hovertext=f'{i}<br>in {j} ' ,
#                              name = f'Cumulative {i} in {j}',
#                             marker_color=colors.pop()),col=1,row=2      )
#         tempz.update_layout( barmode=mode )

# colors=['red','blue']
# for i in feature:
#     for j in country:
#         tempz.add_trace(go.Bar(x = Countries.index, y = Countries.diff()[j][i],hovertext=f'{i}<br>in {j}' ,
#                              name = f'Daily {i} in {j}',
#                             marker_color=colors.pop()),col=1,row=1      )
#         tempz.update_layout( barmode=mode )

# for j in country:
#     tempz.add_trace(go.Scatter(x=Countries.index, y = Countries.diff()[j]['Confirmed'].rolling(window=7).mean(),
#                              mode='markers',
#                              marker=dict(color='black',
#                                          size=3),
#                         hovertext=f'Confirmed cases<br>in {j} ',
#                         name = f'weekly average of confirmed cases in {j}',
#                         ))


# tempz.update_layout(
#         hovermode='x',
#         autosize=True,
#         showlegend=False,
#         margin=go.layout.Margin(
#         l=35, #left margin
#         r=0, #right margin
#         b=35, #bottom margin
#         t=55, #top margin
#         )
#         )


# tempz.update_layout(title_text=f"Daily (up) and Cumulative (down) cases of COVID-19 in {country[0]}")





########## Table
headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'
columnwidth = [1,3,3,3,3,3,3,3,3,3,2,3,3,6]*2

Table = go.Figure(data=[go.Table(
  columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12,13],
  columnwidth = columnwidth,
  header=dict(
    values=[" "]+[CC.columns[i] for i in range(1,len(CC.columns))],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[[CC.iloc[j:j+1][i] for j in range(len(CC))] for i in CC.columns],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor,rowEvenColor]*len(CC)],
    align = ['left'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])

Table.update_layout(
#     width=1800,
    height=3500, 
    margin=dict(t=30, b=10, r=10, l=10))


###### layout
app = dash.Dash()
app.title = 'PR Applications Progress'
server = app.server


app.layout = html.Div([

#         html.Div([
#           dcc.Markdown('''
# # Disclaimer

#             ''',style={'font-family':'calibri','textAlign':'center'}),
#           dcc.Markdown('''

# #### The presentation below is a statistical analysis of the PR application timelines submited to the government of Canada through Express Entry program. This study is a voluntary, unpaid job devoted to people who shared their timelines or were willing to use statistical insights provided by previous applicants.
# #### This study was done on a limited number of applicants and may not fully represent all the possible situations. No decisions shall be made based on the provided information.
# #### The credit for the study goes to people contributing to it by sharing their information, and any claim from anybody expressing that this was done under their supervision or due to their request is false.

# #### No immigration consultant or any group admin can take credit for the PR process or the study done on the timelines. All the participants in this study, chose not to have a lawyer or immigration consultant of any kind.

# #### At the end, I have to thank Ms Salami whose help in data gathering made this study much easier.

# #### For the best experience please use desktop version of your browser.

# #### Please feel free to contact me on [Telegram](https://t.me/Green_Santa) if you want to add your information to this study or for any relevant enquires.

#             ''',style={'font-family':'calibri','textAlign':'left','marginLeft':15,'marginRight':15}),
#           dcc.Markdown('''
            
# ##### *Masoud*
#             ''',style={'font-family':'calibri',
#             'textAlign':'left',
#             'marginLeft':15,'marginRight':15})],


#           style={'margin': 'auto',
#   'width': '50%','marginBottom':60,'border':'3px black solid','padding':'10px'})
        # ,
       # html.Div("",style={'border':'1px blue solid'}),
                  
##################################
## TEMP Section:

# html.Div([html.H1('Temporary Section: COVID-19 Overview',style={'textAlign':'center','font-family':'calibri'}),
#     html.Div(dcc.Graph(id='A',
#                        config={"displaylogo": False,
#               'modeBarButtonsToRemove': ['pan2d','lasso2d']}
#              ),
#              style={'width':'48%','display':'inline-block' }),
    
#     html.Div(
# #         html.Pre(id='hover-data'),
        
#         dcc.Loading(dcc.Graph(id='barplot',figure=tempz,
#                        config={"displaylogo": False,
#               'modeBarButtonsToRemove': ['pan2d','lasso2d']} )),
        
#              style={'width':'48%','display':'inline-block' }),
    
     
#     html.Div(dcc.Slider(id='S',
#                 min=0,
#                 max=len(df_globe['Date'].unique())-1,
#                 step=1,
#             #     step=datetime.timedelta(days=1),
#             #     marks={i: '{}'.format(i) for i in range(0, 100)},
#                 value=len(df_globe['Date'].unique())-1,
#                 ),style={'width':'48%','display':'inline-block' }),
    
#     html.Pre(id='Screen')

#     ],
    
    
#     style={'width':'95%','font':'Calibri','color':'black', 'border':'1px black solid',
#         'marginLeft':4,'marginBottom':100}),

#########

        html.Div(dcc.Graph(
              id='Sunburst-U',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=sun_u),
              style = {'width': '95%',
                  'height':'100%',
                  'textAlign': 'center'}),
    
    
            

          html.Div(dcc.Graph(id='figure',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=gantt_main),
              style = {'backgroundColor': '#111111'}),

           
#                 html.Div(html.H2('Finished Applications ONLY: '),style={'textAlign':"left",
#                                                                        'border':'2px'}),

          html.Div(dcc.Graph(id='figure2',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=gantt2),style={'width':'95%',
                                             'display':'inline-block'}),

    

          html.Div(dcc.Graph(id='figure3',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=gantt3),style={'width':'95%',
                                             'display':'inline-block'}),
    
    
    html.Div(dcc.Graph(
              id='box2',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=box2),
              style = {'width': '95%',
                  'height':'100%',
                  'textAlign': 'center'}),

          dcc.Graph(id='Box',
              config={"displaylogo": False,
              'modeBarButtonsToRemove': ['pan2d','lasso2d']},
              figure=box),
                


    
          html.Div(dcc.Graph(figure=Table,
                                  config={"displaylogo": False,
#               'modeBarButtonsToRemove': ['pan2d','lasso2d']
                                         }),
                             style={'width': '95%',
                                    'height':'100%',
                                    'textAlign': 'center',
                                   'marginLeft':0,
                                   'marginRight':0})
            ])

#...

# @app.callback(Output('output-container-date-picker-single','children'),
#              [Input('my-date-picker-single','date')])
# def update_output(date):
#     string_prefix = 'You have selected: '
#     if date is not None:
#         date = dt.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
#         date_string = date.strftime('%A %B %d, %Y')
#         return string_prefix + date_string


####################

# @app.callback(Output('A','figure'),
#              [Input('S','value')])
# def world_choroleth(day):
    
#     i = day*datetime.timedelta(days=1) + df_globe["Date"].min()

#     df4 = df_globe[df_globe["Date"]==i]
#     today = i.date()
#     df4['text_death'] = f" at date: {today}  <br>" + df4['Death'].astype(str) +" Death cases <br>" +  df4['Confirmed'].astype(str) + " Confirmed cases"+ "<br>Population at 2020: " +df4['Population'].astype(str) 
#     df4['text_confirmed'] = f" at date: {today} <br>" +  df4['Confirmed'].astype(str) + " Confirmed cases" + "<br>Population at 2020: " +df4['Population'].astype(str) 
#     features = ['Confirmed','Death']
#     colors = ["Purple","brown"]
#     scale = 5000



    # data = [go.Choropleth(
    #     locations = df4['CODE'],
    #     z = df4['Population'],
    #     text = df4['Population'],
    #     colorscale = 'reds_r',
    #     zmax = 700000000,
    #     zmin = 20000000,
    #     autocolorscale=False,
    #     reversescale=True,
    #     marker_line_color='darkgray',
    #     marker_line_width=0.5,
    #     colorbar_title = 'Population',
    #     colorbar = None,
    #     showscale = False
    #     ,name='pop choropleth' )
    #         ,

    #      go.Scattergeo(    
    #     locationmode = 'country names',
    #     locations = df4["Country/Region"],
    #        lon = df4['Long'],
    #        lat = df4['Lat'],
    #         text = df4['text_confirmed'],
    #         marker = dict(
    #             size = df4['Confirmed']/scale,
    #             color = "purple",
    #             line_color='rgb(40,40,40)',
    #             line_width=1,
    #             sizemode = 'area'
    #         ),name='Confirmed'),

    #        go.Scattergeo(    
    #     locationmode = 'country names',
    #     locations = df4["Country/Region"],
    #        lon = df4['Long'],
    #        lat = df4['Lat'],
    #         text = df4['text_death'],
    #         marker = dict(
    #             size = df4['Death']/scale,
    #             color = "brown",
    #             line_color='rgb(40,40,40)',
    #             line_width=1,
    #             sizemode = 'area'
    #         ),name="Death")
    #       ]


    # fig = go.Figure(data=data) 
    # fig.update_layout(
    #         title='click on a country to see its trend',
    #         )
        
    # fig.update_layout(
    #     autosize=True,
    #     showlegend=False,
    #     margin=go.layout.Margin(
    #     l=35, #left margin
    #     r=0, #right margin
    #     b=35, #bottom margin
    #     t=55, #top margin
    #     )
    #     )  
        
    # return fig

# @app.callback(Output('Screen','children'),
#              [Input('S','value')])
# def screen(day):
    
#     i = day*datetime.timedelta(days=1) + df_globe["Date"].min()
#     i = i.date()
    
#     return "You have selected " +str(i)


 

 


# @app.callback(Output('barplot','figure'),
#               [Input('A','clickData') ])
# def callback_image(clickData=['Canada']):
    
#     time.sleep(1)
    
# #     feature = ['Confirmed','Death']
#     feature = ['Confirmed']
#     if clickData==['Canada']:
#         country =['Canada']
#     if clickData != ['Canada']:
#         country = [clickData['points'][0]['location']]

#     mode='group'

#     fig = make_subplots(cols=1,rows=2,shared_xaxes=True,vertical_spacing=0.001)

# #     colors=['red','blue']
# #     for i in feature:
# #         for j in country:
# #             fig.add_trace(go.Bar(x = Countries.index, y = Countries[j][i],hovertext=f'{i}<br>in {j} ' ,
# #                                  name = f'Cumulative {i} in {j}',
# #                                 marker_color=colors.pop()),col=1,row=2      )
# #             fig.update_layout( barmode=mode )

#     colors=['red','blue']
# # for i in feature:
#     for j in country:
#         i = 'Confirmed'
#         fig.add_trace(go.Bar(x = Countries.index, y = Countries.diff()[j][i],hovertext=f'{i}<br>in {j}' ,
#                              name = f'Daily {i} in {j}',
#                             marker_color=colors.pop()),col=1,row=1      )
#         fig.update_layout( barmode=mode )

#     for j in country:
#         fig.add_trace(go.Scatter(x=Countries.index, y = Countries.diff()[j][i].rolling(window=7).mean(),
#                                  mode='markers',
#                                  marker=dict(color='black',
#                                              size=1),
#                             hovertext=f'Confirmed cases<br>in {j} ',
#                             name = f'weekly average of confirmed cases in {j}',
#                             ))
        
        
#     for j in country:
#         i = 'Death'
#         fig.add_trace(go.Bar(x = Countries.index, y = Countries.diff()[j][i],hovertext=f'{i}<br>in {j}' ,
#                              name = f'Daily {i} in {j}',
#                             marker_color=colors.pop()),col=1,row=2      )
#         fig.update_layout( barmode=mode )

#     for j in country:
#         fig.add_trace(go.Scatter(x=Countries.index, y = Countries.diff()[j][i].rolling(window=7).mean(),
#                                  mode='markers',
#                                  marker=dict(color='black',
#                                              size=1),
#                             hovertext=f'Fatility cases<br>in {j} ',
#                             name = f'weekly average of fatality cases in {j}',
#                             ), col=1,row=2 )


#     fig.update_layout(
#         hovermode='x',
#         autosize=True,
#         showlegend=False,
#         margin=go.layout.Margin(
#         l=35, #left margin
#         r=0, #right margin
#         b=35, #bottom margin
#         t=55, #top margin
#         )
#         )


#     fig.update_layout(title_text=f"Confirmed cases (up) and Fatality cases (down) in {country[0]}")
#     return fig

if __name__ == "__main__":
    app.run_server()