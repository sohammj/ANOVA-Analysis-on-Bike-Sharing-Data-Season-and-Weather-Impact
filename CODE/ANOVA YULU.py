
import pandas as pd
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import f
#Importing the dataset
yuludf=pd.read_csv("C:\\Users\\simra\\OneDrive\\Desktop\\NM\\yulu_bike_sharing_dataset.csv")
#Printing columns of the dataset to analyse which can be counted as factors
yuludf.columns
yuludf.info()

#For Season
#Defining Null and Alternative Hypothesis
#Null Hypothesis(H0): There is no significant difference due to Season in Count of Vehicles Rented
#Alternative Hypothesis(H1): There is significant difference due to Season(At least one pair)
unique_seasons = yuludf['season'].unique() #Getting unique values aka Distinct classes
count_data_by_season = []
for season in unique_seasons:
    counts = yuludf[yuludf['season'] == season]['count']
    count_data_by_season.append(counts)
#Creating list of every datapoint(Count) under each class(for each season)

#Printing ANOVA Table
model = ols('count ~ season', data=yuludf).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#F tab value
f_tabulated = f.ppf(0.95,3,10884)
print("F-tabulated value:", f_tabulated)

#F cal
f_statistic, p_value = f_oneway(*count_data_by_season)
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

# =============================================================================
# #Output:
#                 sum_sq       df           F        PR(>F)
# season    9.540914e+06      1.0  298.716206  4.758934e-66
# Residual  3.476320e+08  10884.0         NaN           NaN
# F-tabulated value: 2.6057248787213583
# F-Statistic: 236.94671081032106
# P-Value: 6.164843386499654e-149
# =============================================================================
#Decision Criterion: Reject H0 in favour of H1 at Alpha LOS iff Fcal>=Ftab
#Conclusion: We reject H0 in favour of H1 at LOS 0.05 Since Fcal> Ftab. 
#Therefore we can say that there is some significant difference due to season in count of rented vehicles. 
#To further analyse which pairs of seasons cause this variation, we must apply t test. 



#For Weather
#Defining Null and Alternative Hypothesis
#Null Hypothesis(H0): There is no significant difference due to Weather in Count of Vehicles Rented
#Alternative Hypothesis(H1): There is significant difference due to Weather(At least one pair)
uniqueweather = yuludf['weather'].unique() #Getting unique values aka Distinct classes
countbyweather = []
for weather in uniqueweather:
    counts = yuludf[yuludf['weather'] == weather]['count']
    countbyweather.append(counts)
#Creating list of every datapoint(Count) under each class(for each season)

#Printing ANOVA Table
model = ols('count ~ weather', data=yuludf).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

#F tab value
f_tabulated = f.ppf(0.95,1,10884)
print("F-tabulated value:", f_tabulated)

#F cal
f_statistic, p_value = f_oneway(*countbyweather)
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

# =============================================================================
# #Output:
#                 sum_sq       df           F        PR(>F)
# weather   5.911983e+06      1.0  183.185839  2.111106e-41
# Residual  3.512609e+08  10884.0         NaN           NaN
# F-tabulated value: 3.842313347173134
# F-Statistic: 65.53024112793271
# P-Value: 5.482069475935669e-42
# =============================================================================
#Decision Criterion: Reject H0 in favour of H1 at Alpha LOS iff Fcal>=Ftab
#Conclusion: We reject H0 in favour of H1 at LOS 0.05 Since Fcal> Ftab. 
#Therefore we can say that there is some significant difference due to weather in count of rented vehicles. 
#To further analyse which pairs of weather cause this variation, we must apply t test. 
