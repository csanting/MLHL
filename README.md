# MLHL
Attempt at using ML to perform NHL fantasy drafts


## Data Source
[NHL.com](https://www.nhl.com/stats/skaters?aggregate=0&reportType=season&seasonFrom=20052006&seasonTo=20232024&gameType=2&sort=points,goals,assists&page=0&pageSize=100)

## Conda Environment setup

```bash
> conda create -n mlhl-env python=3.12
> conda activate mlhl-env
> conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
