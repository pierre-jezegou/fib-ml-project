# Project
- Pierre Jézégou : pierre.jezegou@estudiantat.upc.edu
- *(?) Unknown*

## Project ideas


## Documents
- `project_proposal`: first deliverable
- `main`: final report

## Usage
- Install working environment
    - Install virtual environment (`venv`): `python3 -m venv .venv && source .venv/bin/activate`
    - Install dependencies & libraries : `pip install -r requirements.txt`

- Train the model
- Use the model



## Features

| Feature                    | Description                                           | Data Type | Number of Unique Values|
| -------------------------- | ----------------------------------------------------- | --------- | ---------------------- |
| Transporteur               | Name of the railway company                           | string    | Categorical : 3        |
| Gare origine               | Departure city                                        | string    | String : 229 values    |
| Gare origine - code UIC    | Unique identifier code for the departure station      | string    | same                   |
| Destination                | Destination city                                      | string    | String : 234 values    |
| Gare destination - code UIC| Unique identifier code for the destination station    | string    | same                   |
| Classe                     | Service class (e.g., first class, second class)       | string    | Categorical : 2        |
| Profil tarifaire           | Type of fare (e.g., standard fare, discounted fare)   | string    | Categorical : 2        |
| Prix minimum               | Minimum ticket price                                  | float     | float (target)         |
| Prix maximum               | Maximum ticket price                                  | float     | float (target)         |