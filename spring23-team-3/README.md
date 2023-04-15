# Bad Landlord II - Team 3

## Project Summary 

The goal of the Bad Landlord project is to increase the accessibility of Boston planning, zoning, and development by creating a watchlist of scofflaw property owners in the city. Our team is working on a piece of the project in conjunction with the other three teams and as a continuation of what was done in Fall ‘22. Our main focus is hazardous criteria violations, since when scofflaws commit these violations they pose a threat to the safety of their tenants. By analyzing where these violations occur most frequently, we are able to determine which landlords commit these violations and cross-reference these frequencies with demographic data. We hope to determine if more vulnerable communities are disproportionately affected by these types of violations.

Our base analysis is to study the hazardous criteria violations in Boston and rank buildings and neighborhoods based on their violations. Following the examples given and based on the information in the dictionary we identified 6 violations that represented hazardous conditions: Hot Water, Potable Water, Heating Facilities Required, Temperature Requirements, Asbestos Material, and Use of Lead Paint Prohibited.

For our extension project we are expanding our work with the hazardous criteria violations to understand the impact on vulnerable communities. We have done analysis on the violations of interest and seen where they occur and at what frequency. Now, we want to compare violation rates to the demographics of the neighborhoods where they occur. We want to see if certain violation classes are more common in certain areas where more vulnerable communities may be present since that would help us determine which landlords are potentially taking advantage of people who have fewer means of recourse.

## Team Contributions

### Jack Ruan (Team Lead)
- Determining the landlords (property companies, etc) with the most violations
- Compling all information into a README
- Extension: Comparing racial demographics  to violation frequency (race_analysis.ipynb)

### Isa Taboada
- Ranking building, cities, and zipcodes by the total number of harzardous criteria violations (vioaltions_analysis.ipynb).
- Comparing number of income restricted units to number of violations by city (income_restricted_analysis.ipynb)
- Extension: Comparing several different income demographics (income bracket, SNAP/food assistance) to violation frequency (income_demograohics.ipynb)

### Li Xi
- Plotting correlations between the total number of affordable units vs total number of violations (vioaltions_analysis.ipynb).
- Creating a map of hazardous criteria violation frequency by violation type (maps.ipynb)
- Extension: Comparing several different education demographics (level of education) to violation frequency (education_violation_analysis.ipynb)

## How to Navigate

We have divided our repo into two folders: data & analysis. The data folder include all the csv files used in the different analysis done in the analysis folder. 

### violations.csv, affordable_rental_units.csv, buildings_df.csv, cities_df.csv & violations_analysis.ipynb
This includes our preliminary analysis done on the Building and Property Violations Dataset. We first plotted the number of violations per building per violation type. We then created graphs to rank buildings by the number of violations based on all the hazardous criteria together. In addition, we created graphs to rank cities by the number of violations based on all the hazardous criteria together. Both buildings_df and cities_df are exported as buildings_df.csv and cities_df.csv in the data folder. Lastly, we did some analysis to create a graph to show correlations between the total number of affordable units vs total number of violations. 

### violations.csv, maps.ipynb & violations.html
This includes a map to visualize all violation types in the spatial context. We plotted different types violations with different color on a map of Boston. This gives a sense of where all the types of violations occur in Boston. You can see the map by opening violations.html in your browser.

### income-restricted-inventory-2021.csv, cities_df.csv & income_restricted_analysis.ipynb
The csv file income-restricted-inventory-2021 contains information about the location of income restricted units throughout the boston area. We created the cities_df.csv contains the results of our violation frequency analysis. Both of these csvs are used in the income_restricted_analysis notebook to see the correlation between the presence of affordable housing and the frequency of violations commited in those areas.


### income_demogpraphics.ipynb
This is part of the extension project to understand the impact on vulnerable communities (lower income communities). 

### education_violation_analysis.ipynb
This is part of the extension project to understand the impact on vulnerable communities (lower education communities).

### race_analysis.ipynb
This is part of the extension project to understand the impact on vulnerable communities (racial minority communities).
