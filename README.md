# MLHL
Attempt at using ML and DL to perform NHL fantasy drafts for the 2024-2025 Season

## Data Sources
[Skater Data - NHL.com](https://www.nhl.com/stats/skaters?aggregate=0&reportType=season&seasonFrom=20052006&seasonTo=20232024&gameType=2&sort=points,goals,assists&page=0&pageSize=100)

[Goalie Data - NHL.com](https://www.nhl.com/stats/goalies?aggregate=0&report=advanced&reportType=season&seasonFrom=20052006&seasonTo=20232024&gameType=2&status=active&sort=qualityStart,a_goalsAgainstAverage&page=0&pageSize=100)

## Setup

Development was performed on Fedora 40 with no dedicated GPU. Adapt the below commands to your preferred platform.

### Conda Environment setup

```bash
conda create -n mlhl-env python=3.12
conda activate mlhl-env
```

### Scraping Dynamic Data

Scraping is unnecessary unless you want to collect your own dataset. CSV files are available and scraping can be skipped if desired.

```bash
conda install selenium pandas
python -m pip install webdriver-manager
python -m pip install --upgrade selenium
```

### Pytorch Forecasting

```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
python -m pip install pytorch-forecasting
```