[![Build Status](https://travis-ci.com/leockl/helstrom-quantum-centroid-classifier.svg?branch=master)](https://travis-ci.com/leockl/helstrom-quantum-centroid-classifier)
[![Build status](https://ci.appveyor.com/api/projects/status/7lmgxf21o6atqs25?svg=true)](https://ci.appveyor.com/project/leockl/helstrom-quantum-centroid-classifier)

# Helstrom Quantum Centroid Classifier
The Helstrom Quantum Centroid (HQC) classifier is a quantum-inspired supervised classification approach for data with binary classes (ie. data with 2 classes only). By quantum-inspired, we mean a classification process which employs and exploits Quantum Theory.

It is inspired by the *quantum Helstrom observable* which acts on the distinguishability between quantum patterns rather than classical patterns of a dataset.

The HQC classifier is based on research undertaken by Giuseppe Sergioli, Roberto Giuntini and Hector Freytes, in their paper:

    Sergioli G, Giuntini R, Freytes H (2019) A new quantum approach to binary classification. PLoS ONE 14(5): e0216224.
    https://doi.org/10.1371/journal.pone.0216224

In this Python package, the classical dataset is encoded into quantum densities using the *inverse of the standard stereographic projection* encoding method. 

This Python package includes the option to vary two parameters that are used to optimize the performance of the HQC classifier. First, there is an option to rescale the dataset. Second, there is an option to choose the number of copies to take for the quantum densities. These two parameters are used in combination together to fine tune and optimize the accuracy of the HQC classifier to a given dataset.

It is shown in [the paper by Sergioli G, Giuntini R and Freytes H](https://doi.org/10.1371/journal.pone.0216224) that the HQC classifier, on average, **_outperforms_** a variety of commonly used classifiers over 14 real-world and artificial datasets. A summary of the performances of the different classifiers examined are shown in the table below:

| Rank | Classifier                    | Average Success Rate (%) |
|:----:| ----------------------------- |:------------------------:|
| 1    | HelstromQuantumCentroid4      | 72.8                     |
| 2    | HelstromQuantumCentroid3      | 65.13                    |
| 3    | GaussianNB                    | 58                       |
| 4    | HelstromQuantumCentroid2      | 57.07                    |
| 5    | HelstromQuantumCentroid1      | 56.6                     |
| 5    | QuadraticDiscriminantAnalysis | 56.6                     |
| 6    | GradientBoostingClassifier    | 52.73                    |
| 7    | ExtreTreesClassifier          | 51.93                    |
| 8    | KNeighborsClassifier          | 51.47                    |
| 9    | NearestCentroid               | 49.13                    |
| 10   | RandomForestClassifier        | 45.87                    |
| 11   | QuantumNearestMeanCentroid    | 43.93                    |
| 12   | AdaBoostClassifier            | 42.93                    |
| 13   | LinearDiscriminantAnalysis    | 42                       |
| 14   | LogisticRegression            | 36.4                     |
| 15   | BernoulliNB                   | 17.4                     |

Average success rate is the average of the number of datasets where the specified classifier outperforms the other classifiers over 14 real-world and artificial datasets.

HelstromQuantumCentroidn is the HQC classifier corresponding to the n number of copies to take for the quantum densities.

## Source Code
The Python package's source code for the HQC classifier is available here: 
https://github.com/leockl/helstrom-quantum-centroid-classifier/blob/master/HQC/HQC.py

## Documentation
The documentation, including how to install the Python package, how to use the Python package and how the HQC classifier algorithm works, are available here: 
https://helstrom-quantum-centroid-classifier.readthedocs.io/en/latest/

## License
This Python package is licensed under the BSD 3-Clause License, available here: 
https://github.com/leockl/helstrom-quantum-centroid-classifier/blob/master/LICENSE

## References
Sergioli G, Giuntini R, Freytes H (2019) A new quantum approach to binary classification. PLoS ONE 14(5): e0216224.
https://doi.org/10.1371/journal.pone.0216224
