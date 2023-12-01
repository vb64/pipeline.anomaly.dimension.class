python -m flake8 --max-line-length=120 pipeline_anomaly_dimension_class
python -m flake8 --max-line-length=120 tests/test
python -m pydocstyle pipeline_anomaly_dimension_class
python -m pydocstyle --match='.*\.py' tests/test
python -m pylint --rcfile .pylintrc2 pipeline_anomaly_dimension_class
python -m pylint --rcfile .pylintrc2 tests/test
pytest --cov=pipeline_anomaly_dimension_class --cov-report term:skip-covered --durations=5 tests
