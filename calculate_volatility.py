# # Filename: calculate_volatility.py

# import pandas as pd
# import numpy as np
# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# def calculate_volatility(data):
#     # Task 1: Calculate Daily and Annualized Volatility
#     data['Daily Returns'] = data['Close'].pct_change()
#     daily_volatility = np.std(data['Daily Returns'])
#     annualized_volatility = daily_volatility * np.sqrt(len(data))

#     return daily_volatility, annualized_volatility

# @app.post("/calculate_volatility")
# async def calculate_volatility_endpoint(file: UploadFile = File(...)):
#     """
#     Endpoint to calculate Daily and Annualized Volatility from a CSV file.

#     Parameters:
#     - file: UploadFile, CSV file containing columns: Date, Open, High, Low, Close, Shares Traded, Turnover(in Cr.)

#     Returns:
#     - dict: {'daily_volatility': float, 'annualized_volatility': float}
#     """

#     filename = "NIFTY 50-20-01-2023-to-20-01-2024.csv"
#     # Read CSV file
#     data = pd.read_csv(filename)

#     # Calculate Daily and Annualized Volatility
#     daily_volatility, annualized_volatility = calculate_volatility(data)

#     return {'daily_volatility': daily_volatility, 'annualized_volatility': annualized_volatility}

# Filename: calculate_volatility.py


#approach 2
# import pandas as pd
# import numpy as np
# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# def calculate_volatility(data):
#     # Task 1: Calculate Daily and Annualized Volatility
#     data['Daily Returns'] = data['Close'].pct_change()
#     daily_volatility = np.std(data['Daily Returns'])
#     annualized_volatility = daily_volatility * np.sqrt(len(data))

#     return daily_volatility, annualized_volatility

# @app.post("/calculate_volatility")
# async def calculate_volatility_endpoint(file: UploadFile = File(...)):
#     """
#     Endpoint to calculate Daily and Annualized Volatility from a CSV file.

#     Parameters:
#     - file: UploadFile, CSV file containing columns: Date, Open, High, Low, Close, Shares Traded, Turnover(in Cr.)

#     Returns:
#     - dict: {'daily_volatility': float, 'annualized_volatility': float}
#     """
#     try:
#         # Read CSV file using the file object
#         data = pd.read_csv(file.file)

#         # Calculate Daily and Annualized Volatility
#         daily_volatility, annualized_volatility = calculate_volatility(data)

#         return {'daily_volatility': daily_volatility, 'annualized_volatility': annualized_volatility}

#     except Exception as e:
#         return {'error': str(e)}


#approach 3

# Filename: calculate_volatility.py

# import pandas as pd
# import numpy as np
# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# def calculate_volatility(data):
#     # Task 1: Calculate Daily and Annualized Volatility
#     if 'Close' not in data.columns:
#         raise ValueError("Column 'Close' not found in the CSV file.")

#     data['Daily Returns'] = data['Close'].pct_change()
#     daily_volatility = np.std(data['Daily Returns'])
#     annualized_volatility = daily_volatility * np.sqrt(len(data))

#     return daily_volatility, annualized_volatility

# @app.post("/calculate_volatility")
# async def calculate_volatility_endpoint(file: UploadFile = File(...)):
#     """
#     Endpoint to calculate Daily and Annualized Volatility from a CSV file.

#     Parameters:
#     - file: UploadFile, CSV file containing columns: Date, Open, High, Low, Close, Shares Traded, Turnover(in Cr.)

#     Returns:
#     - dict: {'daily_volatility': float, 'annualized_volatility': float}
#     """
#     try:
#         # Read CSV file using the file object
#         #data = pd.read_csv(file.file)
#         data = pd.read_csv(file.file, header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover(in Cr.)'])


#         # Calculate Daily and Annualized Volatility
#         daily_volatility, annualized_volatility = calculate_volatility(data)

#         # Return calculated values
#         return {
#             'daily_volatility': daily_volatility,
#             'annualized_volatility': annualized_volatility
#         }

#     except ValueError as ve:
#         return {'error': str(ve)}

#     except Exception as e:
#         return {'error': str(e)}

#4
# Filename: calculate_volatility.py

# import pandas as pd
# import numpy as np
# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# def calculate_volatility(data):
#     # Task 1: Calculate Daily and Annualized Volatility
#     if 'Close' not in data.columns:
#         raise ValueError("Column 'Close' not found in the CSV file.")

#     # Convert 'Close' column to numeric
#     data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

#     if data['Close'].isnull().any():
#         raise ValueError("Invalid numeric values found in the 'Close' column.")

#     data['Daily Returns'] = data['Close'].pct_change()
#     daily_volatility = np.std(data['Daily Returns'])
#     annualized_volatility = daily_volatility * np.sqrt(len(data))

#     return daily_volatility, annualized_volatility

# @app.post("/calculate_volatility")
# async def calculate_volatility_endpoint(file: UploadFile = File(...)):
#     """
#     Endpoint to calculate Daily and Annualized Volatility from a CSV file.

#     Parameters:
#     - file: UploadFile, CSV file containing columns: Date, Open, High, Low, Close, Shares Traded, Turnover(in Cr.)

#     Returns:
#     - dict: {'daily_volatility': float, 'annualized_volatility': float}
#     """
#     try:
#         # Read CSV file using the file object
#         #data = pd.read_csv(file.file)
#         data = pd.read_csv(file.file, header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover'])


#         # Calculate Daily and Annualized Volatility
#         daily_volatility, annualized_volatility = calculate_volatility(data)

#         # Return calculated values
#         return {
#             'daily_volatility': daily_volatility,
#             'annualized_volatility': annualized_volatility
#         }

#     except ValueError as ve:
#         return {'error': str(ve)}

#     except Exception as e:
#         return {'error': str(e)}

#_____5

# Filename: calculate_volatility.py

import pandas as pd
import numpy as np
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

def calculate_volatility(data):
    # Task 1: Calculate Daily and Annualized Volatility
    if 'Close' not in data.columns:
        raise ValueError("Column 'Close' not found in the CSV file.")

    # Convert 'Close' column to numeric
    #data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce', downcast='float')


    invalid_rows = data[data['Close'].isnull()]
    if not invalid_rows.empty:
        print("Invalid numeric values found in the 'Close' column:")
        print(invalid_rows)

        raise ValueError("Invalid numeric values found in the 'Close' column.")

    data['Daily Returns'] = data['Close'].pct_change()
    daily_volatility = np.std(data['Daily Returns'])
    annualized_volatility = daily_volatility * np.sqrt(len(data))

    return daily_volatility, annualized_volatility

@app.post("/calculate_volatility")
async def calculate_volatility_endpoint(file: UploadFile = File(...)):
    """
    Endpoint to calculate Daily and Annualized Volatility from a CSV file.

    Parameters:
    - file: UploadFile, CSV file containing columns: Date, Open, High, Low, Close, Shares Traded, Turnover(in Cr.)

    Returns:
    - dict: {'daily_volatility': float, 'annualized_volatility': float}
    """
    try:
        # Read CSV file using the file object
        data = pd.read_csv(file.file, header=None, names=['Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover'])

        # Calculate Daily and Annualized Volatility
        daily_volatility, annualized_volatility = calculate_volatility(data)

        # Return calculated values
        return {
            'daily_volatility': daily_volatility,
            'annualized_volatility': annualized_volatility
        }

    except ValueError as ve:
        return {'error': str(ve)}

    except Exception as e:
        return {'error': str(e)}
