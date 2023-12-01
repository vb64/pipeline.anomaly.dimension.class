# Python class for pipeline anomaly dimension classification
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.anomaly.dimension.class/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/pipeline.anomaly.dimension.class/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.anomaly.dimension.class/py2.yml?label=Python%202.7&style=plastic&branch=main)](https://github.com/vb64/pipeline.anomaly.dimension.class/actions?query=workflow%3Apy2)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/pipeline.anomaly.dimension.class/py3.yml?label=Python%203.7-3.11&style=plastic&branch=main)](https://github.com/vb64/pipeline.anomaly.dimension.class/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0fc99b84d0434a22b687bfdc1dd4281b)](https://app.codacy.com/gh/vb64/pipeline.anomaly.dimension.class/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/0fc99b84d0434a22b687bfdc1dd4281b)](https://app.codacy.com/gh/vb64/pipeline.anomaly.dimension.class/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

This Python module implements the definition of the "defect dimension class" of a pipeline according to [Specifications and requirements for intelligent pig inspection of pipelines](https://www.researchgate.net/figure/a-Graphical-presentation-of-surface-dimensions-of-metal-loss-anomalies-per-dimension_fig1_370191037).

![Anomaly dimension classification](img/class_table.PNG)

![Graphical presentation of metal loss anomalies per dimension class](img/class_chart.PNG)

## Installation

```bash
pip install pipeline-anomaly-dimension-class
```

## Usage

```python
from pipeline_anomaly_dimension_class import size_class, FeatureClass

# a defect measuring 100x100 mm on a pipe wall 10 mm thick is a defect of the "GENE" class
assert size_class(100, 100, 10) == FeatureClass.GENE

# defects with zero dimensions are not allowed
size_class(0, 100, 10)
pipeline_anomaly_dimension_class.Error: Wrong FeatureClass params. l=0 w=100 t=10

```

## Development

```bash
git clone git@github.com:vb64/pipeline.anomaly.dimension.class.git
cd pipeline.anomaly.dimension.class
```

With Python 2
```bash
make setup2 PYTHON_BIN=/path/to/python27/executable
make tests2
```

With Python 3
```bash
make setup PYTHON_BIN=/path/to/python3/executable
make tests
```
