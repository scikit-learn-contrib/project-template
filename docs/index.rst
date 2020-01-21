.. Helstrom Quantum Centroid classifier documentation master file, created by
   sphinx-quickstart on Mon Jan 13 11:11:04 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Helstrom Quantum Centroid Classifier's Documentation!
====================================================================

The Helstrom Quantum Centroid (HQC) classifier is a quantum-inspired supervised classification approach for data with binary classes (ie. data with 2 classes only). By quantum-inspired, we mean a classification process which employs and exploits Quantum Theory.

It is inspired by the *quantum Helstrom observable* which acts on the distinguishability between quantum patterns rather than classical patterns of a dataset.

The HQC classifier is based on research undertaken by Giuseppe Sergioli, Roberto Giuntini and Hector Freytes, in their paper:

    Sergioli G, Giuntini R, Freytes H (2019) A new quantum approach to binary classification. PLoS ONE 14(5): e0216224.
    https://doi.org/10.1371/journal.pone.0216224

In this Python package, the classical dataset is encoded into quantum densities using the *inverse of the standard stereographic projection* encoding method. 

This Python package includes the option to vary two parameters that are used to optimize the performance of the HQC classifier. First, there is an option to rescale the dataset. Second, there is an option to choose the number of copies to take for the quantum densities. These two parameters are used in combination together to fine tune and optimize the accuracy of the HQC classifier to a given dataset.

.. toctree::
   :maxdepth: 3
   :caption: User Guide

   user_guide

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api

.. toctree::
   :maxdepth: 2
   :caption: Example

   auto_examples/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
