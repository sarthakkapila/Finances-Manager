# financesmanager
 ```
# financesmanager

This Python script is a Personal Finance Manager that allows users to manage their financial information and make cryptocurrency investments. The script fetches market data for various cryptocurrencies, it prompts users for their financial details and investment choices.

## Installation

To install the script, clone the repository and install the required Python packages:

```
git clone https://github.com/your-username/financesmanager.git
cd financesmanager
pip install -r requirements.txt
```

## Usage

To use the script, run the following command:

```
python main.py
```

The script will prompt you for your financial details and investment choices. Once you have entered all the required information, the script will fetch market data for the cryptocurrencies you have selected and display your current portfolio value.

The script also allows you to make cryptocurrency investments. To do so, simply enter the amount of money you want to invest and the cryptocurrency you want to invest in. The script will then execute the trade and update your portfolio value.

## Features

The script has the following features:

* Fetches market data for various cryptocurrencies
* Prompts users for their financial details and investment choices
* Displays current portfolio value
* Allows users to make cryptocurrency investments
* Updates portfolio value after each trade

## Code Explanation

The script is written in Python and consists of the following files:

* `main.py`: The main script that runs the program.
* `cryptocurrency.py`: A class that represents a cryptocurrency.
* `portfolio.py`: A class that represents a portfolio of cryptocurrencies.
* `user.py`: A class that represents a user.

The `main.py` script is the entry point of the program. It creates a `User` object and a `Portfolio` object. It then prompts the user for their financial details and investment choices. Once the user has entered all the required information, the script fetches market data for the cryptocurrencies the user has selected and displays the user's current portfolio value.

The `cryptocurrency.py` file defines the `Cryptocurrency` class. This class represents a cryptocurrency and contains the following attributes:

* `name`: The name of the cryptocurrency.
* `symbol`: The symbol of the cryptocurrency.
* `price`: The current price of the cryptocurrency.
