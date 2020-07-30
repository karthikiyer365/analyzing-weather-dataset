# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 

def categorical(df):
    """ Extract names of categorical column
    This function accepts a dataframe and returns categorical list,
    containing the names of categorical columns(categorical_var).
    """
    categorical_var= df.select_dtypes(include='object').columns.tolist()
    return categorical_var


def numerical(df):
    """ Extract names of numerical column
    This function accepts a dataframe and returns numerical list,
    containing the names of numerical columns(numerical_var).
    """
    numerical_var = df.select_dtypes(include='number').columns.tolist()
    return numerical_var


def clear(df,col,val):
    """ Check distribution of variable
    This function accepts a dataframe,column(feature) and value which returns count of the value,
    containing the value counts of a variable(value_counts)
    """
    value_counts = df[col].value_counts()[val]
    return value_counts


def instances_based_condition(df,col1,val1,col2,val2):
    """ Instances based on the condition
    This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
    based on the condition.
    """

    instance = df[(df[col1] > val1) & (df[col2]== val2)]
    return instance


def agg_values_ina_month(df,date_col,agg_col, agg):
    """  Aggregate values according to month
    This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
    table with different aggregated value of the feature with an index of the month.
    """
    df[date_col] = pd.to_datetime(df[date_col])
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    aggregated_value = df.pivot_table(values=[agg_col], index=df[date_col].dt.month,aggfunc={agg_col:aggregate[agg]})
    return aggregated_value


# Code to group values based on the feature
def group_values(df,col1,agg1):
    """ Agrregate values by grouping
    This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the datframe based on the column.
   """
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    grouping = df.groupby(col1).agg(aggregate[agg1])
    return grouping


# function for conversion 
def convert(df,celsius):
    """ Convert temperatures from celsius to fahrenhheit
    This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
    celsius to fahrenhheit.
    """
    centigrade_temps = df[celsius]
    converted_temp =  1.8*centigrade_temps + 32
    return converted_temp



# Load the weather_2012 data csv file and store it in weather variable.
weather = pd.read_csv(path)
weather.head()


# Check the categorical and numerical variables. You can check it by calling categorical and numerical function. 
print(categorical(weather))
print(numerical(weather))


#Checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column.
#You can check it by calling the function clear with respective parameters.
print(clear(weather,"Weather",'Clear'))
print(clear(weather,"Wind Spd (km/h)", 4))


#Check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25.
#Check it by calling the function instances_based_condition with respective parameters.
wind_speed_35_vis_25 = instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)


#Calculate the mean temperature recorded by month from temperature data. Generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#Call the function agg_values_ina_month with respective parameters. 
agg_values_ina_month(weather,'Date/Time','Dew Point Temp (C)','mean')


# To groupby based on a column like on Weather column and then aggregate the mean values of each column for different types of weather using mean. 
#Call the function group_values.

mean_weather = group_values(weather,"Weather",'mean')


# Convert celsius temperature into fahrehheit temperatures from temperature data by calling the function convert.
weather_fahrehheit = convert(weather,"Temp (C)")


