# ef23-ai-carrace

This is part of a school project - please ignore.

## Setup

Clone this repository to your local machine.

Optional: Set the `TRACES_PATH` environment variable to point to the directory where the traces are stored. (can also be overriden in the code)

### Install dependencies

```sh
python -m pip install -r requirements.txt
```

Alternative in case of name conflicts: Clone/Download `python-neural-network` from [GitHub](https://github.com/rafaelurben/python-neural-network), move the `neural_network` folder into the same folder where `evaluation.py` lives and install `tqdm` via pip.

## Run

Run the `evaluation.py` script to generate traces inside the tracespath folder.

## Source

Python module for the neural network features: (created by me)
https://github.com/rafaelurben/python-neural-network

Source code for the `pyworld` folder: (created by @gymburgdorf-ef23)
https://github.com/gymburgdorf-ef23/NeuralRacingV1/tree/main/pyworld
