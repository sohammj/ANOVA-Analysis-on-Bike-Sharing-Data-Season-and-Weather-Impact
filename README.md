ANOVA Analysis on Bike Sharing Data: Season and Weather Impact
Project Overview
The ANOVA Analysis on Bike Sharing Data is a Python-based project that uses statistical analysis to understand how seasons and weather conditions influence the demand for bike-sharing services. This project applies Analysis of Variance (ANOVA) to test the impact of different seasons and weather conditions on the number of bikes rented. By analyzing the dataset, the project provides insights into the factors affecting bike-sharing demand, which can help service providers and urban planners optimize bike-sharing services.
Key Features
* ANOVA Statistical Testing: Implements one-way ANOVA tests to analyze the impact of season and weather on bike rentals.
* Data Preprocessing: Cleans and prepares the data for statistical analysis, including handling missing values and categorizing data.
* Hypothesis Testing: Evaluates the null and alternative hypotheses for the season and weather factors.
* Visualization: Visualizes the results of the ANOVA tests and provides clear data summaries.
* Reports: Generates statistical reports that include ANOVA tables, F-statistics, and p-values for season and weather impacts.
Dataset
This project uses the Yulu Bike Sharing dataset, which contains data on bike-sharing usage with the following key variables:
* season: The season in which the bike rental occurred (Spring, Summer, Fall, Winter).
* weather: Weather conditions during the bike rental (Clear, Cloudy, Rainy).
* count: The number of bikes rented during a specific time period.
Technologies Used
* Python: Used for statistical analysis and data manipulation.
* Pandas: For data handling and preprocessing.
* NumPy: For numerical calculations.
* Matplotlib: For data visualization.
* SciPy: For statistical testing (ANOVA).
* Statsmodels: For performing the ANOVA and regression analysis.
How to Use
Clone the repository:
git clone https://github.com/sohammj/ANOVA-Analysis-on-Bike-Sharing-Data-Season-and-Weather-Impact.git
cd ANOVA-Analysis-on-Bike-Sharing-Data-Season-and-Weather-Impact

Install required dependencies:
pip install -r requirements.txt


Run the analysis:
python CODE/ANOVA_YULU.py
Access the provided datasets and reports:
* DATA/yulu_bike_sharing_dataset.csv: Contains the bike-sharing data.
* PPT/Predicting Yulu Bike Demand with Statistical Analysis (ANOVA).pdf: A report summarizing the analysis and findings.

Hypothesis Testing:

Season Analysis:
* Null Hypothesis (H0): There is no significant difference in the number of bikes rented due to season.
* Alternative Hypothesis (H1): There is a significant difference in bike rentals due to season.
The ANOVA test shows that the number of bikes rented is significantly impacted by the season, with a p-value close to zero, leading us to reject the null hypothesis.

Weather Analysis:
* Null Hypothesis (H0): There is no significant difference in the number of bikes rented due to weather.
* Alternative Hypothesis (H1): There is a significant difference in bike rentals due to weather.
Similarly, the analysis shows a significant impact of weather on bike rentals, with the p-value indicating a strong rejection of the null hypothesis.

Future Enhancements:
* Multivariable Analysis: Extend the analysis to include additional factors such as holidays or public events that could affect bike rental patterns.
* Predictive Modeling: Implement machine learning models (e.g., regression, time series forecasting) to predict bike-sharing demand based on weather and seasonal data.
* Database Integration: Migrate the dataset to a relational database (like SQLite) for easier management and querying.
  
Acknowledgments:
* Faculty Advisor: Dr. Khinal Parmar
* Data Sources: Yulu Bike Sharing Dataset (Mock dataset for analysis).
