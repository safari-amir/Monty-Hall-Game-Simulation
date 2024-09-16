# Monty Hall Simulation

This project simulates the famous **Monty Hall Problem**, using a web interface built with Streamlit. The Monty Hall problem is a probability puzzle that demonstrates how switching your choice can improve your chances of winning a car over a goat.

## Project Structure

The project consists of two main parts:

1. **Monty Hall Simulation (`monty_hall.py`)**: This Python script runs the Monty Hall game simulation. The function `monty_hall_game` takes two parameters: 
   - `switch_doors`: A boolean flag indicating whether the player switches doors.
   - `n`: The number of simulations to run.
   
   The function returns the probability of success (winning a car) based on the given strategy (switching or not).

2. **Streamlit App (`app.py`)**: This script builds the user interface using Streamlit. Users can:
   - Input the number of simulations to run.
   - Visualize the winning percentages for both strategies (switching vs. not switching) in real-time.

## How to Run the Project

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Streamlit

### Installation
1. Clone the repository or download the files.
2. Install the required libraries:
   ```bash
   pip install streamlit
