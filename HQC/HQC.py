import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import check_classification_targets

class HQC(BaseEstimator, ClassifierMixin):
    """The Helstrom Quantum Centroid (HQC) classifier is a quantum-inspired supervised classification 
    approach for data with binary classes (ie. data with 2 classes only).
                         
    Parameters
    ----------
    rescale : int, default = 1
        The dataset rescaling factor. A parameter used for rescaling the dataset. 
    n_copies : int, default = 1
        The number of copies to take for each quantum density. This is equivalent to taking the 
        n-fold Kronecker tensor product for each quantum density.       

    Attributes
    ----------
    classes_ : ndarray, shape (2,)
        Sorted binary classes.
    centroid_class_0_ : ndarray, shape (n_features + 1, n_features + 1)
        Quantum Centroid for class with index 0.
    centroid_class_1_ : ndarray, shape (n_features + 1, n_features + 1)
        Quantum Centroid for class with index 1.
    q_Hels_obs_ : ndarray, shape (n_features + 1, n_features + 1)
        Quantum Helstrom observable.
    proj_pos_ : ndarray, shape (n_features + 1, n_features + 1)
        Sum of the projectors of the Quantum Helstrom observable's eigenvectors, which has 
        corresponding positive eigenvalues.
    proj_neg_ : ndarray, shape (n_features + 1, n_features + 1)
        Sum of the projectors of the Quantum Helstrom observable's eigenvectors, which has 
        corresponding negative eigenvalues.
    Hels_bound_ : float
        Helstrom bound is the upper bound of the probability that one can correctly discriminate 
        whether a quantum density is of which of the two binary quantum density pattern.          
    """
    # Added binary_only tag as required by sklearn check_estimator
    def _more_tags(self):
        return {'binary_only': True}
    
    
    def __init__(self, rescale=1, n_copies=1):
        self.rescale = rescale
        self.n_copies = n_copies
        
        
    def fit(self, X, y):
        """Perform HQC classification with the inverse of the standard stereographic projection encoding, 
        with the option to rescale the dataset prior to encoding.
                
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The training input samples. An array of int or float.
        y : array-like, shape (n_samples,)
            The training input binary target values. An array of str, int or float.
            
        Returns
        -------
        self : object
            Returns self.
        """
        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        
        # Ensure target y is of non-regression type
        # Added as required by sklearn check_estimator
        check_classification_targets(y)
    
        # Store binary classes and encode y into binary class indexes 0 and 1
        self.classes_, y_class_index = np.unique(y, return_inverse=True)
        
        # Cast X to float to ensure all following calculations below are done in float rather than int 
        X = X.astype(float)
        
        # Rescale X
        X = self.rescale*X
        
        # Calculate sum of squares of each row (sample) in X
        X_sq_sum = (X**2).sum(axis=1)
        
        # Number of rows in X
        m = X.shape[0]
        
        # Number of columns in X
        n = X.shape[1]
        
        # Initialize array X_prime
        X_prime = np.empty((m,n+1))
        # Calculate X'
        for i in range(0,m):
            X_prime[i,:] = (1/(X_sq_sum[i]+1))*(np.concatenate((2*X,(X_sq_sum-1).reshape((-1,1))),axis=1)[i,:])
        
        # Determine rows (samples) in X' belonging to class index 0
        X_prime_class_0 = X_prime[y_class_index==0]
        
        # Determine rows (samples) in X' belonging to class index 1
        X_prime_class_1 = X_prime[y_class_index==1]
        
        # Number of rows (samples) in X'
        M = m
        
        # Number of rows (samples) in X' belonging to class index 0
        M_class_0 = X_prime_class_0.shape[0]
        
        # Number of rows (samples) in X' belonging to class index 1
        M_class_1 = X_prime_class_1.shape[0]
        
        # Initialize array density_class_0
        density_class_0 = np.zeros(((n+1)**self.n_copies,(n+1)**self.n_copies))
        for i in range(0,M_class_0):
            # Encode into quantum densities by using the inverse of the standard stereographic projection 
            # encoding method 
            density_each_row = np.dot(X_prime_class_0[i,:].reshape(-1,1),X_prime_class_0[i,:].reshape(1,-1))
            
            # Calculate n-fold Kronecker tensor product
            if self.n_copies==1:
                density_each_row = density_each_row
            else:
                density_each_row_copy = density_each_row
                for j in range(0,self.n_copies-1):
                    density_each_row = np.kron(density_each_row,density_each_row_copy)
                    
            # Calculate sum of quantum densities belonging to class index 0
            density_class_0 = density_class_0 + density_each_row
            
        # Calculate Quantum Centroid for class index 0
        self.centroid_class_0_ = (1/M_class_0)*density_class_0
        
        # Initialize array density_class_1
        density_class_1 = np.zeros(((n+1)**self.n_copies,(n+1)**self.n_copies))
        for i in range(0,M_class_1):
            # Encode into quantum densities by using the inverse of the standard stereographic projection 
            # encoding method
            density_each_row = np.dot(X_prime_class_1[i,:].reshape(-1,1),X_prime_class_1[i,:].reshape(1,-1))
            
            # Calculate n-fold Kronecker tensor product
            if self.n_copies==1:
                density_each_row = density_each_row
            else:
                density_each_row_copy = density_each_row
                for j in range(0,self.n_copies-1):
                    density_each_row = np.kron(density_each_row,density_each_row_copy)
                    
            # Calculate sum of quantum densities belonging to class index 1        
            density_class_1 = density_class_1 + density_each_row
            
        # Calculate Quantum Centroid for class index 1
        # Added ZeroDivisionError as required by sklearn check_estimator
        try:
            self.centroid_class_1_ = (1/M_class_1)*density_class_1
        except ZeroDivisionError:
            self.centroid_class_1_ = 0

        # Calculate quantum Helstrom observable
        self.q_Hels_obs_ = (M_class_0/M)*self.centroid_class_0_ - (M_class_1/M)*self.centroid_class_1_
        
        # Calculate eigenvalues w and eigenvectors v of the quantum Helstrom observable
        w, v = np.linalg.eig(self.q_Hels_obs_)
        
        # Length of w
        len_w = len(w)
        
        # Initialize arrays self.proj_pos_ and self.proj_neg_
        self.proj_pos_ = np.zeros_like(self.q_Hels_obs_)
        self.proj_neg_ = np.zeros_like(self.q_Hels_obs_)
        # Calculate sum of projectors of eigenvectors with corresponding positive and negative 
        # eigenvalues, respectively
        for i in range(0,len_w):
            if w[i] > 0:
                self.proj_pos_ = self.proj_pos_ + np.dot(v[:,i].reshape(-1,1),v[:,i].reshape(1,-1))
            else:
                self.proj_neg_ = self.proj_neg_ + np.dot(v[:,i].reshape(-1,1),v[:,i].reshape(1,-1))
    
        # Calculate Helstrom bound
        self.Hels_bound_ = (M_class_0/M)*np.trace(np.dot(self.centroid_class_0_,self.proj_pos_)) \
                           + (M_class_1/M)*np.trace(np.dot(self.centroid_class_1_,self.proj_neg_))
        return self
        
        
    def predict_proba(self, X):
        """Performs HQC classification on X and returns the trace of the dot product of the densities and the 
        sum of the projectors with corresponding positive and negative eigenvalues, respectively.
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples. An array of int or float.       
            
        Returns
        -------
        trace_matrix : array-like, shape (n_samples, 2)
            Column index 0 corresponds to the trace of the dot product of the densities and the sum of 
            projectors with positive eigenvalues. Column index 1 corresponds to the trace of the dot 
            product of the densities and the sum of projectors with negative eigenvalues. An array of float.
        """
        # Check if fit had been called
        check_is_fitted(self, ['proj_pos_', 'proj_neg_'])

        # Input validation
        X = check_array(X)
        
        # Cast X to float to ensure all following calculations below are done in float rather than int 
        X = X.astype(float)        
        
        # Rescale X
        X = self.rescale*X        
        
        # Calculate sum of squares of each row (sample) in X
        X_sq_sum = (X**2).sum(axis=1)
        
        # Number of rows in X
        m = X.shape[0]
        
        # Number of columns in X
        n = X.shape[1]
        
        # Initialize array X_prime
        X_prime = np.empty((m,n+1))
        # Calculate X'
        for i in range(0,m):
            X_prime[i,:] = (1/(X_sq_sum[i]+1))*(np.concatenate((2*X,(X_sq_sum-1).reshape((-1,1))),axis=1)[i,:])
            
        # Initialize array trace_matrix (which can contain complex numbers)
        trace_matrix = np.empty((m,2), dtype=np.complex)
        for i in range (0,m):
            # Encode into quantum densities by using the inverse of the standard stereographic projection 
            # encoding method
            density_each_row = np.dot(X_prime[i,:].reshape(-1,1),X_prime[i,:].reshape(1,-1))
            
            # Calculate n-fold Kronecker tensor product
            if self.n_copies==1:
                density_each_row = density_each_row
            else:
                density_each_row_copy = density_each_row
                for j in range(0,self.n_copies-1):
                    density_each_row = np.kron(density_each_row,density_each_row_copy)
                    
            # Calculate trace of the dot product of density of each row and sum of projectors with corresponding 
            # positive and negative eigenvalues, respectively
            trace_matrix[i,0] = np.trace(np.dot(density_each_row,self.proj_pos_))
            trace_matrix[i,1] = np.trace(np.dot(density_each_row,self.proj_neg_))
        return trace_matrix
    
    
    def predict(self, X):
        """Performs HQC classification on X and returns the binary classes.
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples. An array of int or float.
            
        Returns
        -------
        self.classes_[predict_trace_index] : array-like, shape (n_samples,)
            The predicted binary classes. An array of str, int or float.
        """
        # Determine column index with the higher trace value in trace_matrix
        # If both columns have the same trace value, returns column index 0
        predict_trace_index = np.argmax(self.predict_proba(X), axis=1)
        # Returns the predicted binary classes
        return self.classes_[predict_trace_index]
