import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=['date'])

# Clean data
df = df[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]

def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(15, 5))
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")
  sns.lineplot(data=df, legend=False)

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['Years'] = df.index.year
  df_bar['Months'] = df.index.month_name()
  df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Months'])['value'].mean()).rename(columns={'value' : 'Average Page Views'}).reset_index()

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(10, 8))
  month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  sns.barplot(x='Years', y='Average Page Views', hue='Months', hue_order=month_order ,data=df_bar)

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 10))

  # Yearly boxplot
  sns.boxplot(data=df_box, x="year", y="value", ax=ax1)
  ax1.set_title("Year-wise Box Plot (Trend)")
  ax1.set_xlabel("Year")
  ax1.set_ylabel("Page Views")

  # Monthly boxplot
  month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=ax2)
  ax2.set_title("Month-wise Box Plot (Seasonality)")
  ax2.set_xlabel("Month")
  ax2.set_ylabel("Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
