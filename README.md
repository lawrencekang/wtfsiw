Where the F^@$ Should I Work?
========

WTFSIW, for quick and easy wifi cafe recommendations.

## Team

  - __Product Owner__: Lawrence Kang

## Table of Contents

1. [Usage](#Usage)
1. [Requirements](#requirements)
1. [Development](#development)
    1. [Installing Dependencies](#installing-dependencies)
    1. [Tasks](#tasks)
1. [Team](#team)
1. [Contributing](#contributing)

## Usage

> WTFSIW can provide you a local wifi cafe to work at based on your location.  Your location can be detected through your browser, or entered manually.  If you don't like the recommendation, click on the button to get additional recommendations.

## Requirements

1.  Python
1.  Django
1.  Django Response library (see Installing Dependencies, below)
1.  Jquery (CDN linked in JS file)
1.  Yelp API (Local file included as yelp.py; GET requests are encoded in views.py)
1.  Google Reverse Geocode API (GET requests are encoded in views.py)
1.  Google Embed Maps API (GET requests are encoded in views.py)

## Development

### Installing Dependencies

1.  Clone the repo
1.  Navigate to the folder
1.  At the command line, enter: "pip install -r requirements.txt"

### Roadmap

View the project roadmap [here](LINK_TO_PROJECT_ISSUES)


## Contributing

See [Contributing.md](Contributing.md) for contribution guidelines.

## Testing

A testing framework has been set up using Mocha and Chai.  The files can be found in the app/test/ folder in this repo.  From within the app/test/ folder, run npm install angular-mocks to install this dependency.  