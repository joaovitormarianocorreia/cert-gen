# Certificate Generator

The Certificate Generator is a Python script to automate the certificate task.

## Setup

In order to setup the enviroment use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary librarys.

```bash
pip install pandas
pip install reportlab
```

## Usage

The project have a config.yaml file where you will enter the name of the event, input file, background image and date of the event.

```yaml
event_name: Teste
input_name: input.csv
date: 20/01/2022
background_image: background.png
```
The input file must contain two columns, 'NAME' and 'HOURS' and be separate by commas.

Run the code in the terminal or in the IDE. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)