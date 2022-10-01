## this file provides examples of using hydra for hyperparameters sweeps

# we need to specify the values we want to explore and then the options -m ("multi-run"). So for example:

> mlflow run . -P hydra_options="-m parameters.a=3,4,5"

# Of course, we can step through multiple parameters and generate a grid:

> mlflow run . -P hydra_options="-m parameters.a=3,4 parameters.b=2,3,4"

# This can also be expressed using the range() syntax of Hydra:

> mlflow run . -P hydra_options="-m parameters.a=3,4 parameters.b=range(2,4,1)

# If we want our jobs to run in parallel, we can just add the hydra/launcher=joblib specification, like:

> mlflow run . -P hydra_options="hydra/launcher=joblib parameters.a=3,4 parameters.b=range(2,4,1) -m"