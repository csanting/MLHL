# MLHL
Attempt at using ML and DL to perform NHL fantasy drafts


## Data Source
[NHL.com](https://www.nhl.com/stats/skaters?aggregate=0&reportType=season&seasonFrom=20052006&seasonTo=20232024&gameType=2&sort=points,goals,assists&page=0&pageSize=100)

## Conda Environment setup

```bash
conda create -n mlhl-env python=3.12
conda activate mlhl-env
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

## More Deps

### Scraping Dynamic Data
```bash
conda install selenium pandas
python -m pip install webdriver-manager
python -m pip install --upgrade selenium
```
