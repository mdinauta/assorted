### quandl_case_shiller.r  

A R script for downloading the Case-Shiller Housing Index data from Quandl. All of Quandl's data sets are time series, so they make the Case-Shiller dataset available per individual state. This script downloads each state and consolidates them into one data frame for easy analysis.

See [here](http://www.quandl.com/usa/usa-housing-real-estate) for details on the dataset. 

Also in the script is an example for making a choropleth from the data, using my colleague Ari's [choroplethr](https://github.com/trulia/choroplethr) package.

### sfdc_object_schema.py  

Python script that accesses the schema (the names and data types of every field) of a Salesforce object via the API and writes it to a .csv file. Alternatively, you can print the schema to the terminal.
There is no way to download or export a schema via the Salesforce UI, so this script can be quite handy.
It uses the [beatbox](https://code.google.com/p/salesforce-beatbox/) module to connect to the Salesforce API.

