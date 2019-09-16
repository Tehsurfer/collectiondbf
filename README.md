# collectiondbf

### Collection Downloads from BlackFynn 

A tool for downloading a collection of files from Blackfynn

## Installation 
Python 3.3+ and tkinter is required for collectiondbf to work

#### Windows
`pip install collectiondbf`

#### Linux 
```
sudo apt-get install python3-tk
pip3 install collectiondbf
```

#### MacOS
`pip install collectiondbf`
**Note that since macOS python does not come with tkinter, only command line usage is supported


## Usage

### Command Line
The commands below will download the desired directory at the command prompts location.
```
pip install collectiondbf
python -m collectiondbf <api-key> <api-secret> <collection:ID>
```

If you cannot find the collection ID for the folder you wish to download, check for it in the url like so:

![collectionID](https://user-images.githubusercontent.com/37255664/64832679-fe039c80-d62e-11e9-96db-38a54cbd6c55.jpg)

### User Interface
Running `python -m collectiondbf`will start the following ui to input keys and collection ID
![select_channel_2019-09-13 16-24-58 (2)](https://user-images.githubusercontent.com/37255664/64837534-1a113900-d643-11e9-9ba7-3cd37ca74151.jpg)



