# Boilerplate for Python using Poetry + Conda


## Set up

### Poetry

Install Poetry:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/install.python-poetry.org/main/install-poetry.py | python3
```

This should install Poetry globally regardless of environments.

### Miniconda

Run the following bash script:

```bash
#!/usr/bin/env sh

echo "🚩🚩🚩 Installing Python/Miniconda3"

PYTHON_VERSION=39
CONDA_VERSION=4.12.0
CONDA_PYTHON_VERSION="$PYTHON_VERSION"_"$CONDAVERSION"
FILE=Miniconda3-py"$CONDA_PYTHON_VERSION"-Linux-x86_64.sh
cd /tmp
if [ -f "$FILE" ]; then
    echo "$FILE already exists."
else 
    wget https://repo.anaconda.com/miniconda/"$FILE"
fi

bash "$FILE" -b -p $HOME/miniconda3
```

### Mamba

From [mamba-forge](https://github.com/conda-forge/miniforge#mambaforge):

```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```

## How to use

### Initiating a new project

For a new project, we can create a new environment using `conda`:

```bash
# Create a new environment from the environment.yml file:
conda env create -f environment.yml

# Activate the environment:
conda activate boilerplate-python

# Create Conda lock file(s) from environment.yml
conda-lock -k explicit --conda mamba

# Initialize Poetry, python version has to be the same as the version in the environment.yml file:
poetry init --python=~3.10

# Fix package versions installed by Conda to prevent upgrades
poetry add --lock tensorflow=2.8.0 torch=1.11.0 torchaudio=0.11.0 torchvision=0.12.0

# Add conda-lock and other packages
poetry add --lock conda-lock pandas fastapi uvicorn
```

There are a few things to note:

	- We will leverage the expressive syntax of the `environment.yml` file to define a new environment, particularly to specify packages that we want to install outside of `pip`, such as `cuda` or CUDA-enabled versions of packages like `pytorch`. However, by default, we still use Poetry for adding Python dependencies. For CUDA-enabled versions of packages, it is best to specify the package's exact version in `environment.yml`, and after it's installed, to add an entry with the same version specification to Poetry's `pyproject.toml` (without `^` or `~` before the version number). This will let Poetry know that the package is there and should not be upgraded.
	- `conda-lock` is used to generate lock files for Conda dependencies, just like with poetry.lock for Poetry dependencies.
	- `mamba` is used as a better and faster alternative to `conda` for resolving conflicts. An additional benefit is that all contributors to the project will use the same package resolver, independent from the locally-installed version of Conda.

```yaml
name: boilerplate-python
channels:
  - pytorch
  - conda-forge
  # We want to have a reproducible setup, so we don't want default channels,
  # which may be different for different users. All required channels should
  # be listed explicitly here.
dependencies:
  - python=3.10.*  # or don't specify the version and use the latest stable Python
  # - conda-lock
  - pip  # pip must be mentioned explicitly, or conda-lock will fail
  - pip:
    - "conda-lock"
  - tensorflow=2.8.0
  - pytorch::pytorch=1.11.0
  - pytorch::torchaudio=0.11.0
  - pytorch::torchvision=0.12.0

# Non-standard section listing target platforms for conda-lock:
platforms:
  - linux-64
  ```

`virtual-packages.yml` can be used when we want `conda-lock` to generate CUDA-enabled lock files even on platforms without CUDA:

```yaml
subdirs:
  linux-64:
    packages:
      __cuda: 11.5
```

### Extra specifications for `pyproject.toml`

After the `pyproject.toml` file is created, we can add the following specifications for dev dependencies:

```toml
[tool.poetry.group.dev.dependencies]
black = "^22.10.0"
pytest = "^7.2.0"
pytest-cov = "^4.0.0"
ruff = "^0.0.219"
watchdog = "^2.1.9"
httpx = "^0.23.2"
```

These dev dependencies will be installed when we run:

```bash
# Install only dev dependencies
poetry install --only dev

# Install all dependencies, including both main and dev:
poetry install

# Install only main dependencies:
poetry install --without dev
```

Besides that, we can specify rules for formatting and testing:


```toml
[tool.ruff]
ignore = ["E402","F841","E501","F401"]
select = ["E", "F", "I", "W"]
line-length = 100
fixable = ["I"]
exclude = [".env", ".venv", "venv", "notebooks"]
show-source = true

[tool.coverage.paths]
source = ["src"]

[tool.coverage.run]
branch = true
relative_files = true

[tool.coverage.report]
show_missing = true
fail_under = 80

[tool.black]
line-length = 100
extend-exclude = '''
/(
	| .env
	| .venv
	| venv
	| notebooks
)/
'''
```

### Creating a new environment from an existing lock file

```bash
conda create --name boilerplate-python --file conda-linux-64.lock
conda activate boilerplate-python

# Install only dev dependencies
poetry install --only dev

# Install all dependencies, including both main and dev:
poetry install

# Install only main dependencies:
poetry install --without dev
```


### Updating the environment

```bash
# Re-generate Conda lock file(s) based on environment.yml
conda-lock -k explicit --conda mamba
# Update Conda packages based on re-generated lock file
mamba update --file conda-linux-64.lock
# Update Poetry packages and re-generate poetry.lock
poetry update
```
