import requests
from bs4 import BeautifulSoup

def scrape_data():
    
    # Setting the URL we want to scrape the data from
    URL = "https://www.formula1.com/en/results.html/2023/races/1226/abu-dhabi/race-result.html"

    # Sending a GET request to the URL
    page = requests.get(URL)
    
    # Checking if the GET request completed successfully (returning status_code as 200)
    if page.status_code == 200:
    
        # Parsing the content
        soup = BeautifulSoup(page.text, "html.parser")

        # Saving the title and the date
        race_title = soup.find('h1', class_='ResultsArchiveTitle').text.strip()
        race_date = soup.find('span', class_='full-date').text.strip()
        results_table = soup.find('table', class_='resultsarchive-table').find('tbody')

        data_list = []

        # Iterating through rows in the results table
        for row in results_table.find_all('tr'):

            # Extracting data
            position_element = row.find('td', class_='dark')
            driver_first_name_element = row.find('span', class_='hide-for-tablet')
            driver_last_name_element = row.find('span', class_='hide-for-mobile')
            number_element = row.find('td', class_='dark hide-for-mobile')
            car_element = row.find('td', class_='semi-bold uppercase hide-for-tablet')
            laps_element = row.find('td', class_='bold hide-for-mobile')
            
            # Handling the case where the data may be missing, setting it as "N/A"
            position = position_element.text.strip() if position_element else "N/A"
            driver_first_name = driver_first_name_element.text.strip() if driver_first_name_element else "N/A"
            driver_last_name = driver_last_name_element.text.strip() if driver_last_name_element else "N/A"
            number = number_element.text.strip() if number_element.text.strip() else "N/A"
            car = car_element.text.strip() if car_element.text.strip() else "N/A"
            laps = laps_element.text.strip() if laps_element.text.strip() else "N/A"

            # Formatting the data
            data_list.append("Position: {:<5} | No.: {:<5} | Driver: {:<25} | Car: {:<35} | Laps: {:<5}".format(position, number, f"{driver_first_name} {driver_last_name}", car, laps))
    
        return race_title, race_date, data_list

    else:

        # If the GET request fails, print the following message
        print(f"Failed to retrieve the webpage.")
        return None


# Method to write data to file
def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))

# Method for reading from file
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_path} not found ...")
        return None

# Setting the file_path
file_path = "race_results.txt"

race_title, race_date, scraped_data = scrape_data()

if scraped_data:
    write_to_file(file_path, [f"Race Title: {race_title}", f"Race Date: {race_date}"] + scraped_data)

read_data = read_from_file(file_path)
if read_data:
    print(read_data)
