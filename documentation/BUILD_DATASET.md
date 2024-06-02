# Build yourself the dataset
- The CI automagically compile the data to create the dataset in release (in GitHub) if the commit if tagged `'build-dataset-*'`. Download the artifact and put it at the root of the project.
- If you want to build manually the dataset:
  - Change directory to `build-dataset`
  - Run the first part of the dataset construction related to cities informations
    ```sh
    python consolidate_cities.py
    ```
  - Run the second and last part of the dataset
    ```sh
    python build_dataframe.py 
    ```
You can then use the other scripts and notebooks
