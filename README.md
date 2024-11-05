# UK Postcode Deprivation Statistics Streamlit APP

### Description

This streamlit application allows users to input a UK postcode and retrieve deprivation statistics for that area based on the indicies of Multiple deprivation (IMD) 2019 data. 
- https://imd-by-postcode.opendatacommunities.org/imd/2019
- https://communitiesopendata-communities.hub.arcgis.com/datasets/45e05901e0a14cca9ab180975e2e8194_0/api


- Look up deprivation statistics by postcode
- View detailed descriptions of each statistic to understand their meaning

The application is organized into two modules for better code organization and maintainability:

- Front end module (imd_streamlit_app.py): Contains the streamlit app code for user interaction and display
- Back end module (imd_backend.py): Contains functions responsible for data retrieval and processing. 

---

### Features

- Interactive postcode lookup: Input any UK postcode to retrieve the corresponding deprivation statistics.
- Deprivation statistics Display: Show key statistics such as IMD Rank, IMD Decile, Income score, emloyement scor.
- Descriptions tabs: Provides detailed explanations of each description 

---

### Prerequisites

- Python 3.10 or hight: ensure python is installed on your system
- Requried python libaries
    - streamlit
    - requests
    - pandas

---

### Installation

1. Clone or download repo <br>
``` git clone https://github.com/wilson101xx/imd_deprevation.git ```
2. Create a virtual enviroment (This is optional) <br>
```python -m venv venv```
3. Activate
    - Windows: <br>
    ``` venv/scripts/activate```
    - Mac/Linux:
    ``` source venv/bin/activate```
4. Install required libaries <br>
``` pip install -r requirments.txt```

--- 

### Code Structure

- ```imd_streamlit_app.py```: The main streamlit application file containing the user interface
- ```imd_backend.py```: Contains the backend functions for data retrieval and processing.

---

### Usage
1. ensure both files are in same directory
2. run the streamlit app <br>
    ```streamlit run imd_streamlit_app.py```
3. Access the app on your browser  http://localhost:8501


---


