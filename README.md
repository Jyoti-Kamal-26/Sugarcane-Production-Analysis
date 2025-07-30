# Sugarcane Production Analysis

## Project Overview
This project analyzes global sugarcane production data across different countries and continents. The analysis explores production patterns, yield efficiency, land usage, and regional distributions to provide insights into the global sugarcane industry.

## Dataset
- *File*: List of Countries by Sugarcane Production.csv
- *Scope*: Global sugarcane production data by country
- *Key Metrics*: Production volume, acreage, yield per hectare, production per person

## Libraries Used
python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## Data Structure
The dataset contains the following columns:
- Country: Country name
- Continent: Continental classification
- Production (Tons): Total sugarcane production in tons
- Production per Person (Kg): Per capita production in kilograms
- Acreage (Hectare): Total land area used for sugarcane cultivation
- Yield (Kg / Hectare): Production efficiency per hectare

## Data Preprocessing

### 1. Data Cleaning
- Removed dots (.) from numeric fields for proper formatting
- Replaced commas with dots for decimal notation in European format
- Renamed columns to remove spaces and special characters for easier handling:
  - Production (Tons) → Production(Tons)
  - Production per Person (Kg) → Production_per_Person(Kg)
  - Acreage (Hectare) → Acreage(Hectare)
  - Yield (Kg / Hectare) → Yield(Kg/Hectare)

### 2. Missing Data Handling
- Identified and removed rows with null values in the Acreage(Hectare) column
- Reset index after dropping null values
- Removed unnecessary index columns

### 3. Data Type Conversion
- Converted all numeric columns from string to float type for mathematical operations

## Analysis Overview

### Univariate Analysis

#### Continental Distribution
- *Objective*: Understand how many countries from each continent produce sugarcane
- *Method*: Value counts analysis of the Continent column
- *Visualization*: Bar chart showing country count by continent

#### Distribution Analysis
- *Objective*: Examine the distribution patterns of key metrics
- *Methods*: 
  - Distribution plots (histograms) for all numeric variables
  - Box plots to identify outliers
- *Variables Analyzed*: Production, Production per Person, Acreage, Yield

### Bivariate Analysis

#### Key Research Questions Addressed:

1. *Which country produces the maximum sugarcane?*
   - Created percentage contribution analysis
   - Visualized top 10 producing countries using bar charts and pie charts

2. *Which country has the highest cultivated land area?*
   - Sorted countries by acreage in descending order
   - Visualized top 10 countries with highest sugarcane acreage

3. *Which country has the highest yield per hectare?*
   - Analyzed production efficiency across countries
   - Identified most productive countries per unit area

4. *Which country has the highest per capita production?*
   - Examined production relative to population size
   - Identified countries with highest sugarcane production per person

#### Correlation Analysis
- *Objective*: Understand relationships between different production metrics
- *Method*: Correlation matrix with heatmap visualization
- *Variables*: Production, Production per Person, Acreage, Yield per Hectare

#### Relationship Exploration
1. *Land Area vs Total Production*: Scatter plot analysis
2. *Yield Efficiency vs Total Production*: Examining if higher yield per hectare correlates with higher total production

### Continental Analysis

#### Aggregated Continental Metrics
- Grouped data by continent to analyze regional patterns
- Calculated total production, acreage, and average yields by continent

#### Key Continental Questions:
1. *Which continent produces the maximum sugarcane?*
   - Bar chart visualization of continental production totals
   - Comparison of total acreage by continent

2. *Does the number of countries in a continent affect total production?*
   - Added country count per continent
   - Line plot analysis showing relationship between number of countries and total production

3. *Continental production distribution*
   - Pie chart showing percentage contribution of each continent to global production

#### Continental Correlation Analysis
- Extended correlation analysis to include the number of countries per continent
- Examined relationships between continental metrics

## Key Findings and Insights

### Production Leaders
- Identification of top sugarcane producing countries
- Analysis of countries with most efficient production systems

### Regional Patterns
- Continental distribution of sugarcane production
- Relationship between number of producing countries and total continental output

### Efficiency Metrics
- Countries with highest yield per hectare (production efficiency)
- Per capita production leaders

### Correlations
- Strong correlation between total acreage and total production
- Relationship patterns between yield efficiency and total output
- Continental-level correlation patterns

## Visualizations Created

1. *Distribution Plots*: Histograms and box plots for all numeric variables
2. *Bar Charts*: Country rankings for various metrics
3. *Pie Charts*: Percentage contributions (country and continental level)
4. *Scatter Plots*: Relationship analysis between variables
5. *Correlation Heatmaps*: Visual correlation matrices
6. *Line Plots*: Trend analysis for continental data

## Technical Notes

### Data Quality Considerations
- Handled European number formatting (dots and commas)
- Addressed missing data through row removal
- Ensured proper data types for mathematical operations

### Visualization Approach
- Used seaborn and matplotlib for comprehensive visual analysis
- Implemented rotation for country labels to improve readability
- Applied color mapping for enhanced visual distinction

## Future Enhancements

Potential areas for extended analysis:
1. Time series analysis if historical data becomes available
2. Economic factor integration (GDP correlation with production)
3. Climate and geographical factor analysis
4. Export/import analysis for trade patterns
5. Sustainability metrics integration

## Conclusion

This analysis provides a comprehensive overview of global sugarcane production patterns, identifying key producing countries, regional distributions, and efficiency metrics. The insights can inform agricultural policy, trade decisions, and investment strategies in the sugarcane industry.

---

*Author*: Data Analysis Project  
*Date*: Analysis conducted using Python data science libraries  
*Dataset*: Global Sugarcane Production by Country
