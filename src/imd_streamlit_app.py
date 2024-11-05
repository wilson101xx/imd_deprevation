import streamlit as st
import pandas as pd
from imd_backend import get_lsoa_code, get_imd_data

st.title("UK Postcode Deprivation Statistics")

# Create tabs
tab1, tab2 = st.tabs(["Lookup Deprivation Statistics", "Descriptions of Statistics"])

with tab1:
    # Step 1: Get user input
    postcode = st.text_input("Enter a UK postcode:", "").strip().replace(" ", "").upper()

    if postcode:
        # Display a loading spinner while processing
        with st.spinner('Fetching data...'):
            # Step 2: Get LSOA code
            lsoa_code, error = get_lsoa_code(postcode)
            if error:
                st.error(error)
            else:
                st.write(f"**LSOA Code:** {lsoa_code}")

                # Step 3: Get IMD data
                attributes, error = get_imd_data(lsoa_code)
                if error:
                    st.error(error)
                else:
                    st.subheader("Deprivation Statistics for the Given Postcode:")
                    # Display selected fields in a table
                    fields_to_display = {
                        'IMD_Rank': 'IMD Rank',
                        'IMD_Decile': 'IMD Decile',
                        'IMDScore': 'IMD Score',
                        'IncScore': 'Income Score',
                        'EmpScore': 'Employment Score',
                        'EduScore': 'Education Score',
                        'HDDScore': 'Health Score',
                        'CriScore': 'Crime Score',
                        'BHSScore': 'Barriers to Housing Score',
                        'EnvScore': 'Environment Score',
                        'TotPop': 'Total Population',
                        'DepChi': 'Dependent Children',
                        'Pop16_59': 'Population Aged 16-59',
                        'Pop60_': 'Population Aged 60+',
                        'WorkPop': 'Working Population'
                    }

                    df = pd.DataFrame.from_dict({fields_to_display[k]: [attributes[k]] for k in fields_to_display})
                    st.table(df.T)

with tab2:
    st.subheader("Descriptions of Deprivation Statistics")
    descriptions = {
        'IMD Rank': 'The rank of the area in the Index of Multiple Deprivation (1 = most deprived area).',
        'IMD Decile': 'The decile of deprivation (1 = most deprived 10% of areas, 10 = least deprived 10%).',
        'IMD Score': 'The overall deprivation score for the area.',
        'Income Score': 'Measures the proportion of the population experiencing deprivation related to low income.',
        'Employment Score': 'Measures the proportion of the working-age population in involuntary exclusion from the labor market.',
        'Education Score': 'Measures the lack of attainment and skills in the local population.',
        'Health Score': 'Measures the risk of premature death and the impairment of quality of life through poor physical or mental health.',
        'Crime Score': 'Measures the risk of personal and material victimization at local level.',
        'Barriers to Housing Score': 'Measures the physical and financial accessibility of housing and local services.',
        'Environment Score': 'Measures the quality of the local environment.',
        'Total Population': 'The total number of people living in the area.',
        'Dependent Children': 'The number of dependent children aged 0-15 living in the area.',
        'Population Aged 16-59': 'The number of people aged 16 to 59 in the area.',
        'Population Aged 60+': 'The number of people aged 60 and over in the area.',
        'Working Population': 'The number of people of working age in the area.'
    }

    for key, desc in descriptions.items():
        st.write(f"**{key}:** {desc}")
