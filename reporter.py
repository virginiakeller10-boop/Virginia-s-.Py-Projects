import requests
import csv
import os

API_KEY = " Unique API"


def get_weather_data(city):
    """Fetches and processes weather data from the OpenWeatherMap API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Check if the API call was successful
        if data["cod"] == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]

            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": main_data["temp"],
                "humidity": main_data["humidity"],
                "description": weather_data["description"]
            }
        else:
            print(f"Error: City not found or API issue. Code: {data['cod']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None


def write_to_csv(city_data):
    """Writes weather data to a CSV file."""
    file_exists = os.path.isfile("city_data.csv")
    try:
        with open("city_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(
                    ["City", "Country", "Temperature (C)", "Humidity (%)", "Description"])
            writer.writerow([
                city_data["city"],
                city_data["country"],
                city_data["temperature"],
                city_data["humidity"],
                city_data["description"]
            ])
        print(
            f"\nSuccessfully wrote data for {city_data['city']} to city_data.csv.")
    except IOError as e:
        print(f"An error occurred while writing to the CSV file: {e}")


def read_and_report_from_csv():
    """Reads data from the CSV file and reports a summary."""
    if not os.path.isfile("city_data.csv"):
        print("\nNo city_data.csv file found to report from.")
        return
    try:
        with open("city_data.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row

            cities_count = 0
            print("\n--- Current Cities in city_data.csv ---")
            for row in reader:
                if row:
                    cities_count += 1
                    city, _, temp, _, _ = row
                    print(f"  • {city}: {temp}°C")
            print(f"\nTotal number of cities in the file: {cities_count}.")
    except IOError as e:
        print(f"An error occurred while reading the CSV file: {e}")


def main():
    """Main function to run the weather program."""
    while True:
        city_name = input("\nEnter a city name (or 'q' to quit): ").strip()
        if city_name.lower() == 'q':
            break

        if not city_name:
            print("City name cannot be empty. Please try again.")
            continue

        weather_info = get_weather_data(city_name)

        if weather_info:
            print("\n--- Weather Summary ---")
            print(f"City: {weather_info['city']}, {weather_info['country']}")
            print(f"Temperature: {weather_info['temperature']}°C")
            print(f"Humidity: {weather_info['humidity']}%")
            print(f"Description: {weather_info['description']}")

            write_to_csv(weather_info)

    read_and_report_from_csv()


if __name__ == "__main__":
    main()

