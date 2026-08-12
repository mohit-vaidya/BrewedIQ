import plotly.graph_objects as go
import plotly.express as px


#tab1
def daily_growth(data1):
    fig = go.Figure()
    fig.add_trace(
    go.Scatter(
        x = data1.index.astype(str),
        y = data1.values,
        name = 'lines+markers',
        mode = 'lines+markers',
        line_color='#4B3832'))

    fig.update_layout(
    title = 'Monthly Sales',
    xaxis_title = 'Month',
    yaxis_title = 'Total sales', height=800)
    return fig


def mov_avg(data2, mov_avg_data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data2.index.astype(str), y=data2.values, line_color='#4B3832', mode='lines+markers', name='lines+markers'))
    fig.add_trace(go.Scatter(x=mov_avg_data.index.astype(str), y=mov_avg_data.values, line_color="#A9A9A9", mode='lines+markers', name='lines+markers'))
    fig.update_layout(
    title = 'Sales vs Moving Average',
    xaxis_title = 'Week',
    yaxis_title = 'Value', height=400, width=1100)
    return fig

def  mont_growth(data3):
    fig = px.bar( x=data3.index.astype(str), y=data3.values, title= "Monthly Growth", height=400)
    return fig


#tab 2
def avg_sales_hours(data4):
    fig = go.Figure()
    for category in data4['product_category'].unique():
        cat_df = data4[data4['product_category'] == category]
        hourly_sales = cat_df.groupby([cat_df.transaction_date.dt.date, 'hour'])['Total_sales'].sum().reset_index()
        average_hourly_sales = hourly_sales.groupby('hour')['Total_sales'].mean()
    
        fig.add_trace(
            go.Scatter(
                x = average_hourly_sales.index,
                y = average_hourly_sales.values,
                mode = 'lines',  
                name = category)
                )

    fig.update_layout(
    title = "Average Sales by Hour of Day (Product Category Wise)",
    xaxis_title = "Hour of Day",
    yaxis_title = "Average Sales by Hour",
    legend_title = "Product Category", height=600, width=1100)
    return fig

def avg_daily_ana(data5):
    fig=go.Figure()
    fig=px.bar(x=data5.index,y=data5.values,title="Average Daily Sales")
    return fig

def avg_hourly_sales(data6):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
        x = data6.index.astype(str),
        y = data6.values,
        name = 'lines',
        mode = 'lines+markers'))

    fig.update_layout(
    title = 'hourly Sales',
    xaxis_title = 'hour',
    yaxis_title = 'Sales', height=600, width=1100)
    return fig

#tab 3 
def Product_category_dist_sales(data7):
    fig = px.bar(x=data7.index.astype(str) , y=data7.values , title= "Product Category Distribution (by Sales)")
    return fig

def Product_category_dist_transaction(data8):
    transaction_sales = data8.groupby('product_category')['transaction_qty'].sum().reset_index()
    fig = px.bar(x=data8.index.astype(str), y=data8.values, title= "Product Category Distribution (by transaction)", height=600)
    return fig

def Product_Type_Distribution(data9, value):
    fig = px.pie( data9, values=value, names="Product_type", 
    title="Product Category Distribution by Sales" ,color_discrete_sequence=px.colors.sequential.RdBu)
    return fig



def stores(data10, data11, data12):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data10.index.astype(str), y=data10.values, line_color='#4B3832', mode='lines+markers', name='Hells Kitchen'))
    fig.add_trace(go.Scatter(x=data11.index.astype(str), y=data11.values, line_color="#A9A9A9", mode='lines+markers', name='Lower Manhattan'))
    fig.add_trace(go.Scatter(x=data12.index.astype(str), y=data12.values, line_color="#C19A6B", mode='lines+markers', name='Astoria'))
    fig.update_layout(
    title = 'Store Visits Over Time',
    xaxis_title = 'Month',
    yaxis_title = 'Total Sales', height=600, width=1100)

    return fig

def hsaless(data13):
    fig = px.bar(x=data13.index.astype(str), y=data13.values , title= "Hell's Monthly Growth", height=600)
    return fig

def lmsaless(data14):
    fig = px.bar(x=data14.index.astype(str), y=data14.values , title= "Lower Manhattan	 Monthly Growth", height=600)
    return fig

def astosaless(data15):
    fig = px.bar(x=data15.index.astype(str), y=data15.values , title= "Astoria Monthly Growth", height=600)
    return fig