# Carbon Emissions Analysis

This repository contains code and data for analyzing carbon emissions in England using a place-based carbon calculator. The data used in this analysis is sourced from the paper titled "A place-based carbon calculator for England" by Morgan, Malcolm, Anable, Jillian, & Lucas, Karen.

## Data Source
The data used in this analysis is available in the following publication:

Morgan, Malcolm, Anable, Jillian, & Lucas, Karen. (2021). A place-based carbon calculator for England. Presented at the 29th Annual GIS Research UK Conference (GISRUK), Cardiff, Wales, UK (Online): Zenodo. [http://doi.org/10.5281/zenodo.4665852](http://doi.org/10.5281/zenodo.4665852)

## Instructions

[![Docker Repository](https://img.shields.io/badge/Docker%20Hub-Repository-blue)](https://hub.docker.com/repository/docker/chrismcaballero/carbon-footprint-analysis/general) <br>
To download the image from my Docker Hub repository.

### Run with docker

1. Run **`docker build -t <image-name>`** or download the image linked above.
2. Run **`docker run -p 8888:8888 <image-name>`**.
2. Lastly, follow the link http://127.0.0.1:8888?token=docker.

### Local run using requirements.txt

1. Clone the repository to your local machine.
2. Set up the required dependencies and environment based on the **`requirements.txt`** file.
3. Run the Jupyter notebook **`carbon_emissions_analysis.ipynb`** to execute the analysis.

## The notebook performs the following tasks:

1. Loads and extracts the data files from the provided zip archives.
2. Loads the data into Pandas dataframes for further analysis.
3. Explores and visualizes the carbon emissions data at different levels of aggregation.
4. Analyzes the yearly distribution of carbon emissions per person.
5. Compares carbon emissions between local authorities and the national average.
6. Investigates environmental emission grades and their correlation with other attributes.
7. Tests classification techniques for predicting emission grades.
8. Imputes missing values in the emission grades columns.

Please refer to the notebook for detailed code and analysis.

## Contents

The repository contains the following files:

- `requirements.txt`: The necessary requirements for running the Jupyter Notebook.
- `carbon_emissions_analysis.ipynb`: Jupyter Notebook containing all relevant data exploration.
- `utils.py`: Utility functions for data loading and manipulation.
- `visutils.py`: Utility functions for data visualization.
- `data/`: Directory containing the data files.

## Data Citation

If you use the data or code in this repository, please cite the original data source:

Morgan, Malcolm, Anable, Jillian, & Lucas, Karen. (2021). A place-based carbon calculator for England. Presented at the 29th Annual GIS Research UK Conference (GISRUK), Cardiff, Wales, UK (Online): Zenodo. [http://doi.org/10.5281/zenodo.4665852](http://doi.org/10.5281/zenodo.4665852)
