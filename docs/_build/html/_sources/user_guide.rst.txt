User Guide
==========

This user guide will show you a step-by-step guide on how to install the Helstrom Quantum Centroid (HQC) classifier's API, how to use the HQC classifier's API and how the algorithm behind the HQC classifier works. 

How to install the API
----------------------

To install the HQC classifier's Python package, you will first need to install a Python-based package manager called Pip. See instructions `in this link <https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation>`_ (under 'Pip install') on how to install Pip.

Once you have Pip installed, open the command prompt (or cmd) window on your computer. Change directories to the folder that contains the Python file ``get-pip.py`` that you have just downloaded. Then run the following command in the command prompt:

.. code:: bash

    

    pip install hqc

You have now installed the HQC classifier's Python package in your computer and you are now able to use it in Python Interpreter.

You can also install the HQC classifier's Python package in Anaconda. Pip is already pre-installed in Anaconda so you do not need to install Pip if you are using Anaconda. To install the HQC classifier's Python package in Anaconda, open the Anaconda Prompt window and run the following command:

.. code:: bash

    

    pip install hqc

You have now installed the HQC classifier's Python package in Anaconda and you are now able to use it in Anaconda.

Tip: If there is a never version of the HQC classifier's Python package released, you can run the following command in the command prompt or Anaconda Prompt window to upgrade to a newer version:

.. code:: bash

    

    pip install hqc --upgrade

How to use the API
------------------

First, import the HQC classifier's Python package into Python Interpreter or Anaconda:

.. code:: python

    import hqc

Then specify the two parameters required by the HQC classifier, the rescaling factor, *rescale* and the number of copies to take for each quantum density, *n_copies*. Say, *rescale* = 1.5 and *n_copies* = 2, the HQC classifier would look like:

.. code:: python

    hqc.HQC(rescale=1.5, n_copies=2)

If either *rescale* and/or *n_copies* are not specified, they would both default to 1. The HQC classifier would look like:

.. code:: python

    hqc.HQC()

where *rescale* = 1, *n_copies* = 1

or

.. code:: python

    hqc.HQC(rescale=1.5)

where *n_copies* = 1

or

.. code:: python

    hqc.HQC(n_copies=2)

where *rescale* = 1

From here on, we will be using *rescale* = 1.5 and *n_copies* = 2 as an example. To get your HQC classification model, fit the features matrix X and binary target vector y, as below:

.. code:: python

    model = hqc.HQC(rescale=1.5, n_copies=2).fit(X, y)

The fitted attributes of your model can be obtained by calling the following methods:

=======================   ============================================================================================================
Method                    Fitted Attribute
=======================   ============================================================================================================
model.classes_            Gives the sorted binary classes.
model.centroid_class_0_   Gives the Quantum Centroid for classes_ with index 0.
model.centroid_class_1_   Gives the Quantum Centroid for classes_ with index 1.
model.q_Hels_obs_         Gives the Quantum Helstrom observable.
model.proj_pos_           Gives the sum of the projectors of the Quantum Helstrom observable's eigenvectors, which has corresponding positive eigenvalues.
model.proj_neg_           Gives the sum of the projectors of the Quantum Helstrom observable's eigenvectors, which has corresponding negative eigenvalues.
model.Hels_bound_         Gives the Helstrom bound.
=======================   ============================================================================================================

For prediction, you can obtain the trace matrix where column index 0 corresponds to the trace values for class 0 and column index 1 corresponds to the trace values for class 1, by using:

.. code:: python

    model.predict_proba(X)

You can then obtain the class predictions by using:

.. code:: python

    model.predict(X)

You can obtain the accuracy score or the Jaccard similarity score using:

.. code:: python

    model.score(X,y)

You can use scikit-learn's GridSearchCV tool to do an exhaustive search to find the optimal values for the parameters *rescale* and *n_copies*. For eg.:

.. code:: python

    from sklearn.model_selection import GridSearchCV
    import pandas as pd

    param_grid = {'rescale':[0.5, 1, 1.5], 'n_copies':[1, 2]}
    models = GridSearchCV(hqc.HQC(), param_grid).fit(X,y)

    # To ouput a dataframe table of all the models specified in param_grid
    pd.DataFrame(models.cv_results_)

More information about scikit-learn's GridSearchCV tool can be found `here <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_.        

How does the HQC classifier works
---------------------------------

Below is a step-by-step guide to the algorithm behind the HQC classifier. The source code can be found in this `link <https://github.com/leockl/helstrom-quantum-centroid-classifier/blob/master/HQC/HQC.py>`_.

1. First the algorithm perform checks on the features matrix X and binary target vector y, such as checking if X and y have the same number of rows (samples/observations) and y is of a categorical type variable.

2. Then it encodes y into binary classes 0 and 1.

3. Because the following calculations from here on would involve decimal places, X is converted to float to allow for floating point calculations.

4. X is then multiplied by the rescaling factor, *rescale* (chosen by the user).

5. The algorithm then calculates the sum of squares for each row (sample/observation) in X.

6. Next the algorithm determines the number of rows and columns in X.

7. X' is then calculated and seperated into two groups, one with binary class 0 and the other with binary class 1.

8. After this, the algorithm determines the number of rows (samples/observations) in X', X' with binary class 0 and X' with binary class 1.

9. For X' with binary class 0, the algorithm calculates the quantum centroid for binary class 0 by combining these steps: first calculate the quantum densities for each row (sample/observation) in X', then calculate the *n_copies* or the n-fold Kronecker product (chosen by the user) for each quantum density and then summing the n-fold quantum densities and deviding by the number of rows (samples/observations) in X' with binary class 0 to get the quantum centroid for binary class 0.

10. Step 9 is repeated for X' in the group with binary class 1.

11. Next, the algorithm calculates the *quantum Helstrom observable* matrix.

12. This is followed by determining the eigenvalues and eigenvectors of the *quantum Helstrom observable* matrix as well as determining the number of eigenvalues.

13. The algorithm then calculates sum of all the projectors of the eigenvectors with corresponding positive and negative eigenvalues, respectively. The projector of an eigenvector is defined as the dot product between the unit eigenvector and its transpose, ie. ``np.dot(v, np.transpose(v))`` where v is a column vector of the unit eigenvector. The projector of an eigenvector is a matrix.

14. Now, the algorithm calculates the Helstrom bound.

15. Moving into prediction, the algorithm first perform checks such as to see if a model have already been fitted and the matrix X we are predicting on has the same number of columns as the features matrix X. 

16. The algorithm then repeats Steps 3, 4, 5, 6 and 7 (with no seperation into the two groups, binary class 0 and binary class 1).

17. Next, the algorithm calculates the trace matrix which contains the trace values corresponding to binary class 0 in the first column and the trace values corresponding to binary class 1 in the second column of the trace matrix. This is done by combining these steps: first calculate the quantum densities for each row (sample/observation) in X' that we want to predict, then calculate the *n_copies* or the n-fold Kronecker product (chosen by the user) for each quantum density and then calculate the trace of the dot product between the n-fold quantum densities and the sum of projectors with corresponding positive and negative eigenvalues, respectively. 

18. Finally, the algorithm determines the predicted binary class 0 or 1 by comparing the trace values in the trace matrix. If the trace values in the first column of the trace matrix is higher than (or the same as) the trace values in the second column, the predicted binary class is 0, otherwise the predicted binary class is 1.