# predictMEE
Predicting missing metadata with using recurrent neural network (RNNs) based entity extraction

## Installation

Substituting your GH `username` below, you can clone this repo with
```bash
git clone https://username@github.com/aklie/predictMEE.git
```

Then, install the necessary requirement packages with
```bash
cd predictMEE
```

## Training models with colorme
If you want to train a model with `colorme`, you can use the CLI. For example, from the root `colorme` directory,
you can train using the test config in the following way:
```bash
cd colorme
colorme train baseline --config colorme/testing/data/test_generator_config.yml 
```

If you have already installed `colorme`, you may need to re-install it in order for the CLI to work.

If you are running on datahub (dsmlp), you probably need to revise the install instructions slightly:
```bash
# from your home directory, after starting gpu container
export PATH=$PATH:$(pwd)/.local/bin

# skip this step if its already on cloned
git clone https://username@github.com/gwarmstrong/cse253-final-project.git

cd cse253-final-project
pip install --user -e .

```

## Requirements (so far)

```text
torch>=1.4
numpy
pillow
pandas
click
pytorch-msssim
scikit-image
```

See the [torch page](https://pytorch.org/get-started/locally/) on installation
