# Project Title - Module 10 Challenge - Surf's Up!

## Project Description

### Part 1: Analyse and Explore the Climate Data
Use Python & SQLAlchemy to produce a basic climate analysis and data exploration of the climate database.

### Requirements


**Hawaii_Measurements.csv**

**Hawaii_Stations.csv**

**climate_starter-checkpoint.ipynb**



#### Analysis

**Precipitation Analysis**

1. Find the most recent date in the dataset.
2. Using that date, create a query of the previous 12 months data to find the precipiation records for that period.
3. Select only the 'date' and 'prcp'.
4. Load query results into a Pandas DataFrame and set the index to the 'date' column.
5. Sort the DataFrame values by 'date'
6. Plot the results by using the DataFrame plot method.
7. Use Pandas to print the Summary statistics for the precipitation data.

**Station Analysis**

1. Design a query to calculate the total number of stations in the dataset.

2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

        List the stations and observation counts in descending order.

        Answer the following question: which station id has the greatest number of observations?

        Using the most-active station id, calculate the lowest, highest, and average temperatures.

3. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

        Filter by the station that has the greatest number of observations.

        Query the previous 12 months of TOBS data for that station.

        Plot the results as a histogram with bins=12, as the following image shows:

### Part 2: Design Your Climate App
Once the initial analysis has been completed, design a Flask API based on the queries you just developed.

        1. /
Create a homepage and list all the available routes        
        
        2. /api/v1.0/precipitation
Convert the query results to a dictionary by using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

        3. /api/v1.0/stations
Return a JSON list of stations from the dataset.

        4. /api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

        /api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.        

        








