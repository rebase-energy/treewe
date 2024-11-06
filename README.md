<div align="center">
<h2 style="margin-top: 0px;">
    📈 Tree-based predictions for weather and energy
</h2>
</div>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/treewe.svg)](https://badge.fury.io/py/treewe) 
[![Join us on Slack](https://img.shields.io/badge/Join%20us%20on%20Slack-%2362BEAF?style=flat&logo=slack&logoColor=white)](https://join.slack.com/t/rebase-community/shared_invite/zt-1dtd0tdo6-sXuCEy~zPnvJw4uUe~tKeA) 
[![GitHub Repo stars](https://img.shields.io/github/stars/rebase-energy/treewe?style=social)](https://github.com/rebase-energy/treewe)

`treewe` is an open-source Python library that implements state-of-the-art energy and weather prediction models for use cases including as wind, solar and demand forecasting. It is using the [`enflow`](https://github.com/rebase-energy/enflow) structure to evaluate and benchmark prediction models in a reproducible manner. `treewe` lets you: 

* 🔄 Get a unified syntax for working with state-of-the-art tree-based predictor libraries such as [XGBoost](https://github.com/dmlc/xgboost), [LightGBM](https://github.com/microsoft/LightGBM), [CatBoost](https://github.com/catboost/catboost) and [Scikit-Learn](https://github.com/scikit-learn/scikit-learn);
* 📊 Run and evaluate pre-implemented prediction models on your own energy and weather datasets; and
* 📈 Create your own prediction model and benchmark it against pre-implemented prediction models;

**⬇️ [Installation](#installation)**
&ensp;|&ensp;
**📖 [Documentation](https://docs.energydatamodel.org/en/latest/)**
&ensp;|&ensp;
**🚀 [Try out now in Colab](https://colab.research.google.com/github/rebase-energy/treewe/blob/main/treewe/examples/gefcom2014-wind.ipynb)**
&ensp;|&ensp;
**👋 [Join Community Slack](https://join.slack.com/t/rebase-community/shared_invite/zt-1dtd0tdo6-sXuCEy~zPnvJw4uUe~tKeA)**

## Basic Usage
`treewe` uses [`enflow`](https://github.com/rebase-energy/enflow) structure for creating the basic evaluation loop that avoids data leakage and ensures reproducibility. An experiment is represented by the following 4 components: 

* [`Dataset`]()
* [`Environment`]()
* [`Objective`]()
* [`Predictor`]()

Given a defined `dataset`, `env` (environment), `agent` (model) and `obj` (objective), the sequential decision loop is given by: 

```python
# Create the env, agent and obj. Your code goes in defining these classes. 
env = GEFCom2014WindEnv()
obj = PinballLoss(quantiles=np.arange(0.1, 1, 0.1))
predictor = LGBGEFCom2014Predictor()

state = env.reset()
next_input, initial_df = env.reset()
predictor1.train(features=initial_df["features"], target=initial_df["target"])

done = False
while done is not True:
    prediction = predictor.predict(features=next_input)
    next_input, next_target, done = env.step()
    loss = obj.calculate(next_target, prediction)

env.close()
```

For a full walkthrough go to the [documentation](https://docs.enerflow.org/en/latest/walkthrough.html#) or open in [Colab](https://colab.research.google.com/github/rebase-energy/enerflow/blob/main/enerflow/examples/walkthrough/notebook.ipynb). 

## Installation
Install the **stable** release: 
```bash
pip install treewe
```

Install the **latest** release: 
```bash
pip install git+https://github.com/rebase-energy/treewe
```

Install in editable mode for **development**: 
```bash
git clone https://github.com/rebase-energy/treewe.git
cd treewe
pip install -e . 
```

## Ways to Contribute
We welcome contributions from anyone interested in this project! Here are some ways to contribute to **enerflow**:

* Create a new predictor; 
* Create a new benchmark dataset;
* Create a new objective function; or
* Add core functionality to `treewe`;

If you are interested in contributing, then feel free to join our [Community Slack](https://join.slack.com/t/rebase-community/shared_invite/zt-1dtd0tdo6-sXuCEy~zPnvJw4uUe~tKeA) so that we can discuss it. 

## Licence
This project uses the [MIT Licence](LICENCE.md).  


