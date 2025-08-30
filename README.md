# Project Title
Weather Application

## Description
A simple weather application built using Tkinter for the graphical user interface (GUI) and the OpenWeatherMap API to retrieve weather data.

## Python Version
This project uses Python 3.12.

## Features
* Retrieves current weather data for a specified city using the OpenWeatherMap API
* Displays weather information in a GUI with a background image
* Downloads and displays weather icons corresponding to the current weather condition

## File Descriptions

### `get_weather_icons.py`
`get_weather_icons.py` is a Python script that downloads weather icons from OpenWeatherMap and saves them to a local directory.

* The script defines a `download_weather_icons` function that takes a base URL, image directory, and list of icon names, and downloads the icons if they don't already exist locally.
* The `main` function uses this function to download day and night weather icons from OpenWeatherMap.
* Icons are saved to a local directory `./img/`, which is created if it doesn't exist.

### `main.py`
`main.py` is a simple weather application built using Tkinter for the graphical user interface (GUI) and the OpenWeatherMap API to retrieve weather data.

* The application allows users to enter a city name, retrieve its current weather, and display the result along with an icon representing the weather condition.
* The application uses a hardcoded API key for OpenWeatherMap, which should be replaced with a secure and personalized key for production use.
* The application assumes that the weather icon images are stored in a local directory (`./img/`).

## Getting Started

```
tkinter
urllib3
```
1. **Run the script to download weather icons**: Run `python get_weather_icons.py` to download weather icons.
2. **Run the application**: Run `python main.py` to launch the GUI application.

## Usage
To use the application, simply run `python main.py` and enter a city name in the text box. Click the button to retrieve the weather information, and the application will display the result along with a weather icon.

## Note
Replace the hardcoded API key in `main.py` with a secure and personalized key from OpenWeatherMap for production use.
