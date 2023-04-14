# Team 4

## Team members:
* [Maria Shevchuk ('23)](https://github.com/mariashev) - Team Rep
* [Francesco Ciraolo (I PhD)](https://github.com/FrancescoCiraolo)
* [Aaron Liauw ('23)](https://github.com/aliau-cmyk)
* [Eddie Jones ('23)](https://github.com/ewj327)

## Project Summary

In collaboration with councilor Breadon, we are performing data analysis on Boston’s property and renting datasets to determine which landlords in the area are so-called “bad landlords”. The stated aim of the project is to build a trackable system for property violations throughout Boston and create a matrix that determines whether a given landlord is a “bad landlord.” Finding a specific ordinance that can be used to define a threshold for a “bad landlord” was also a stated goal of the project. The overall motivation and impact of the project is to increase transparency and accessibility for the housing development process in the greater Boston area so that the public can make informed decisions about where to live and understand the shifting landscape of their city.


### Extension Project
For the extension analysis, we reviewed the Climate Ready Boston Social Vulnerability dataset to investigate whether there’s a higher correlation with any of the predictors (disabilities, low income, english proficiency, POC, children, older adults) and the response variable (medical illness). In essence, our goal was to perform an inference task — opposed to prediction — to find the most influential factors to medical illness. We chose medical illness as our response variable because the Boston city council is most interested in CM410 violations, which are public health violations. By identifying these factors, aimed to find what communities are most vulnerable to Bad Landlords and violations.

It is important to note that results of the analysis are not prescriptive — they do not perform methods of scientific inquiry and testing in the real world — so we should not infer anything about the results of the analysis or anything about these demographic groups. However, they could shed some light on what groups we might what to consider, for example, when tracking resource allocation or vulnerability. 

## Contents 

In this repository you can find: 


|  |      **File/Directory**                   |    **Description**                                                              |
|-:|:---------------------------------:|---------------------------------------------------------------------------|
| 1| [code](./code)  | Data analysis code (notebook format) and helper functions |
| 2| [data](./data)  | Datasets we used for this project and any transformed versions of the data |
| 3| [deliverables](./deliverables)    | Course-related deliverables detailing our progress |
| 4| [visualizations](./visualizations)  | Various visualizations we have generated during the data analysis process |



## Project Webpage/Dashboard

We created a dashboard for our project that demonstrates our findings and various visualizations. Click [here](https://francescociraolo.github.io/bad-landlords-team4/plots.html) to access the dashboard.

Here you will find 3 pages: 
1. Maps - select a dataset and view the data in a map format
2. Plots - various visualizations we have created throughout the project 
3. Landlors - list of identified scofflaw landlors and a search option to view violations for a given landlord

### Demo
![demo gif](./visualizations/dashboard_demo.gif)

