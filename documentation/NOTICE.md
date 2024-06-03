# Steps to reproduce the project

1. Clone the repository and install the requirements
    ```bash
    git clone https://github.com/pierre-jezegou/fib-ml-project
    cd fib-ml-project

    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```
2. Get the non-preprocessed dataset
    - If you want to use the dataset that we built, you can download it from [here](https://github.com/pierre-jezegou/fib-ml-project/releases/tag/build-dataset-1.0.3)
    - If you want to build the dataset yourself, you can follow the instructions in the [BUILD_DATASET.md](https://github.com/pierre-jezegou/fib-ml-project/blob/main/documentation/BUILD_DATASET.md)

3. Preprocess the dataset
    - Run each cell of the `Preprocessing.ipynb` notebook to preprocess the dataset

4. Train and evaluate the models. All the models notebooks are located in the `models` folder of the repo
    - Run each cell of the `linear-models.ipynb` notebook to train and evaluate the linear models
    - Run each cell of the `knn.ipynb` notebook to train and evaluate the KNN model
    - Run each cell of the `randomforest.ipynb` notebook to train and evaluate the Random Forest model
    - Run each cell of the `svm.ipynb` notebook to train and evaluate the SVM model

5. Generate the report
All the metrics are gathered in the `metrics.csv` file. You can make further analysis.
