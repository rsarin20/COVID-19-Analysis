# -*- coding: utf-8 -*-
"""Exploration of COVID19 data (May Edition)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yKPeR-avv7ChIgyUMa6fhTzpUbun3HnU

# **Exploration of COVID19 using Plotly and Seaborn**

Origin: https://ourworldindata.org/coronavirus (first exploration - 20th April)

Data: https://github.com/owid/covid-19-data/tree/master/public/data, https://github.com/owid

Plotly Guide: https://plotly.com/python/plotly-express/

Seaborn Guide: https://seaborn.pydata.org/examples/index.html

# **Basic data checks**
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
covid = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

covid.head()

covid.dtypes

print(covid.location.unique())
print(covid.columns)

covid_top = covid[covid.location.isin(['India','Spain','Italy','Germany','Switzerland','United Kingdom','South Korea','Singapore','United States','Mexico','Brazil','Russia','Ireland','France','Sweden','Norway','Greece','Canada','China','Turkey','Japan'])]

"""# **Plotly Charts and Fun**"""

pip install plotly

import plotly.express as px

fig = px.scatter(covid_top,
              x = covid_top.location, 
              y = (covid_top.total_deaths/covid_top.total_cases), 
              color = covid_top.location,
              template = 'plotly_dark',
              size_max = 5, 
              # render_mode = 'webgl'
              )
fig.show()

fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/case_fatality_covid.html")

fig = px.bar_polar(covid_top[covid_top.date > '2020-02-25'],
                   r="total_cases_per_million", theta="location", color="location", template="plotly_dark"
                  #  animation_frame = 'date'
                   )
                  #  color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()

fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/cases_per_million_covid_spider.html")

fig = px.bar(covid_top[covid_top.date > '2020-02-25'],
             x = 'date', y= 'new_deaths',
             color = 'location',
             template='seaborn')

fig.show()

fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/new_cases_perday_covid.html")

fig = px.bar(covid_top[covid_top.date > '2020-02-25'],
             x = 'date', y= 'new_cases',
             color = 'location',
             template='seaborn')

fig.show()

fig = px.bar(covid_top[covid_top.date > '2020-02-25'],
             x = 'date', y= 'total_cases',
             color = 'location',
             template='plotly_dark')

fig.show()
fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/total_cases_perday_covid.html")

import plotly.express as px

fig = px.line(covid_top[covid_top.date > '2020-02-28'],
              x = 'date', 
              y = 'total_tests_per_thousand', 
              color = 'location',
              template = 'plotly_dark', 
              facet_col='location'
              )
fig.show()

import plotly.express as px

fig = px.line(covid_top[covid_top.date > '2020-02-28'],
              x = 'date', 
              y = 'total_cases_per_million', 
              color = 'location',
              template = 'plotly_dark'
              )
fig.show()

import plotly.express as px

fig = px.scatter(covid_top,
              x = covid_top.total_deaths_per_million, 
              y = covid_top.total_tests_per_thousand, 
              color = covid_top.location,
              template = 'plotly_dark',
              size_max = 5, render_mode = 'webgl')
fig.show()
fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/cases_tests_density_scatter_covid.html")

import plotly.express as px

fig = px.scatter(covid_top,
              x = covid_top.total_cases_per_million, 
              y = covid_top.total_deaths_per_million, 
              color = covid_top.location,
              template = 'plotly_dark',
              size_max = 5, render_mode = 'webgl')
fig.show()
fig.write_html("/content/drive/My Drive/Colab Notebooks/COVID/cases_deaths_density_scatter_covid.html")

# COVID-19 spread across Europe

import plotly.express as px

fig = px.choropleth(covid, 
                    locations="location", locationmode='country names', 
                    color="total_cases",
                    hover_name="location", 
                    # animation_frame="date", 
                    range_color=[0,230000],
                    width=1000, height=1000,
                    projection='eckert4',
                    # template='plotly-dark',
                    color_continuous_scale=px.colors.sequential.Agsunset,
                    scope='europe',
                    # 'equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 
                    # 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', or 'sinusoidal'
                    title="/t How COVID-19 spead across the World"
                    )
fig.show()

"""# **Seaborn Charts**"""

import seaborn as sns
sns.set(style="whitegrid")

a = (25, 12)
fig, ax = plt.subplots(figsize=a)

sns.boxenplot(x="location", y="total_cases",
              color="b",
              scale="linear", data=covid_top[covid_top.location != 'United States'],
              ax=ax
              )

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# covid_sns = sns.load_dataset(covid_top[covid_top.date > '2020-02-28'])
covid_sns = covid_top[covid_top.date > '2020-02-28'][covid_top.location != 'United States'].pivot("location", "date", "new_cases")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(25, 12))
sns.heatmap(covid_sns, 
            # annot=True, 
            # fmt="d", 
            linewidths=.5, ax=ax)

# Create the data
# rs = np.random.RandomState(1979)
x = covid_top[covid_top.date > '2020-03-28'][covid_top.location.isin(['Spain','Italy','Germany','United Kingdom','Russia','France','Turkey'])].new_cases
g = covid_top[covid_top.date > '2020-03-28'][covid_top.location.isin(['Spain','Italy','Germany','United Kingdom','Russia','France','Turkey'])].location
df = pd.DataFrame(dict(x=x, g=g))
# m = df.g.map(ord)
# df["x"] += m

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=1.5, palette=pal)

# Draw the densities in a few steps
g.map(sns.kdeplot, "x", clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw=.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)


# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "x")

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)