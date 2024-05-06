# sqlalchemy-challenge
### Andrew Mack | DU Data Analytics | April 2024

UPDATES 5.6.2024:
    - Originally, single quotation marks around 'start' and 'end' relating to the two dynamic routes' date format lead to user confusion, and were removed.
    - A screenshot of dynamic start/end date API route added to the repo to show it is functioning after clarifying the correct format in the index.HTML file for the API URLs.
    - The static 'precipitation' API route has been fixed

## Summary
This repository contains the files to meet the requirements of the SQL Alchemy module 10 homework challenge.

The challenge consists of two parts: analysis (Jupyter notebook) and endpoints through a Flask server app (Python file). An html template is used to improve the API landing page.

UPDATES 5.6.2024: Originally, single quotation marks around 'start' and 'end' relating to the dynamic routes' date format lead to user confusion, and were removed. A screenshot of dynamic start/end date API route added to the repo to show it is functioning after clarifying the correct format in the index.HTML file for the API URLs.

## Repo Contents
- README
- Dynamic Route Screenshot 2024_05_06.png
- Surfsup
    - /climate_starter.ipynb
    - /app.py
    - /Resources
        - /hawaii_measurements.csv
        - /hawaii_stations.csv
        - /hawaii.sqlite
    - /templates
        - /index.html

## Resources
- Initial notebook and python files as well as datasets provided
- Class instruction and module activities
- Tutor assistance with html and datetime code implementation
- HTML template starter code to beautify API landing page: https://getbootstrap.com/
- Flask documentation for rendering html: https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates
- Strptime() method utilized to convert string to datetime object for start and end dates from API endpoint URLs: https://www.programiz.com/python-programming/datetime/strptime
