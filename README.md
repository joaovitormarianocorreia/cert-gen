# Certificate Generator

The Certificate Generator is a Python script to automate the certificate task.

## Setup

In order to setup the enviroment use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary librarys.

```bash
# using pipenv
pipenv install
# using pip
pip install -r requirements.txt
```

## Usage

The project have a config.yaml file where you will enter the name of the event, input file, background image and date of the event.

```yaml
event_name: Teste # name of the event
input_name: input.csv # input file
output_directory_name: output_folder # name of the output folder
date: 20/01/2022 # date of the event to be used in the certificate
background_image: background.png # image to be used as background
attributes: [name, hours, ...] # attributes to be used in the certificate and present on csv file
certificate_text: | # text to be used in the certificate
  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

The input file must contain two columns, 'NAME' and 'HOURS' and be separate by commas.

Run the code in the terminal or in the IDE.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
