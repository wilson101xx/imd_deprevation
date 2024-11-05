import requests

def get_lsoa_code(postcode):
    """
    Retrieves the LSOA code for a given UK postcode using the Postcodes.io API.
    """
    postcode_api_url = f"https://api.postcodes.io/postcodes/{postcode}"

    response = requests.get(postcode_api_url)
    if response.status_code != 200:
        return None, "Invalid postcode or postcode not found."
    else:
        data = response.json()
        if data['status'] == 200:
            lsoa_code = data['result']['codes']['lsoa']
            return lsoa_code, None
        else:
            return None, "Error retrieving postcode data."

def get_imd_data(lsoa_code):
    """
    Queries the ArcGIS REST API using the LSOA code to retrieve deprivation statistics.
    """
    feature_layer_url = (
        "https://services-eu1.arcgis.com/EbKcOS6EXZroSyoi/arcgis/rest/services/"
        "Indices_of_Multiple_Deprivation_(IMD)_2019/FeatureServer/0/query"
    )

    params = {
        'where': f"lsoa11cd='{lsoa_code}'",
        'outFields': '*',
        'returnGeometry': False,
        'f': 'json'
    }

    response = requests.get(feature_layer_url, params=params)
    if response.status_code != 200:
        return None, "Error querying the feature layer."
    else:
        data = response.json()
        if 'features' in data and data['features']:
            attributes = data['features'][0]['attributes']
            return attributes, None
        else:
            return None, "No IMD data found for the given LSOA code."

if __name__ == "__main__":
    postcode = "SW1A 1AA"
    lsoa_code, error = get_lsoa_code(postcode)
    if error:
        print(f"Error: {error}")
    else:
        print(f"LSOA code: {lsoa_code}")

        imd_data, error = get_imd_data(lsoa_code)
        if error:
            print(f"Error: {error}")
        else:
            print(f"IMD data: {imd_data}")