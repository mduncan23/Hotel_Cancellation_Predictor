import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, \
                            accuracy_score, roc_auc_score, precision_score,\
                            recall_score, f1_score
from sklearn.utils.validation import check_is_fitted
from sklearn.model_selection import cross_validate

# Making a function to automate results
def score_model(model, 
                model_name,
                score_card = None,
                X_train=None, 
                X_test=None, 
                y_train=None, 
                y_test=None,
                normalize=None):
    
    '''
    Input an sklearn model and model name (string).
    Returns a Confusion Matrix and classification Reports for
    train and test sets.  
    
    Input a score_card DataFrame to save results of train and test sets.
    Set Normalize (True or None) to normalize the confusion matrix.
    '''
    
    #Check if model is already fit
    try:
        check_is_fitted(model)
        fit = True
    except:
        fit = False
    
    #fit the model
    if fit == False:
        model.fit(X_train, y_train)
    
    # setting up the plot
    fig, ax = plt.subplots(1,2, figsize=(12,6))
    fig.suptitle(f'{model_name} Results', size=25)
    
    
    #Train Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(model, 
                                          X_train, 
                                          y_train, 
                                          ax=ax[0], 
                                          normalize=normalize)
    ax[0].set_title('Train Results', size=15)

    # Test Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(model, 
                                          X_test, 
                                          y_test, 
                                          ax=ax[1],
                                          normalize=normalize)
    ax[1].set_title('Test Results', size=15)



    
    
    # setting it to check if scorecard entered or just running a quick run
    
    score_dict = {'Name': [model_name], 
                  'Accuracy':[accuracy_score(y_test, model.predict(X_test))],
                  'Precision': [precision_score(y_test, model.predict(X_test), zero_division=0)],
                  'Recall': [recall_score(y_test, model.predict(X_test), zero_division=0)],
                  'F1 Score': [f1_score(y_test, model.predict(X_test), zero_division=0)],
                  'ROC/AUC Score': [roc_auc_score(y_test, model.predict(X_test))]}
    if type(score_card) == pd.core.frame.DataFrame:
        score_card = pd.concat([score_card, pd.DataFrame(score_dict)], ignore_index=True)
        return(score_card.drop_duplicates())
    else:
        print(pd.DataFrame([score_dict]))
        
        
        
        
        
        
def cv_score(model, 
             model_name,
             cv_score_card = None,
             X_train=None, 
             y_train=None):
    
    
    # setting up crossval function with custom score list
    cv = cross_validate(model,
                       X_train,
                       y_train,
                       scoring={'accuracy':'accuracy', 
                                'precision':'precision', 
                                'recall':'recall', 
                                'f1':'f1', 
                                'roc_auc':'roc_auc'},
                                return_train_score=True)
    
    # creating dict from results
    cv_results_dict = {'Name': [model_name], 
                       'Train Accuracy':[cv['train_accuracy'].mean()],
                       'Test Accuracy':[cv['test_accuracy'].mean()],
                       'Train Precision': [cv['train_precision'].mean()],
                       'Test Precision': [cv['test_precision'].mean()],
                       'Train Recall': [cv['train_recall'].mean()],
                       'Test Recall': [cv['test_recall'].mean()],
                       'Train F1 Score': [cv['train_f1'].mean()],
                       'Test F1 Score': [cv['test_f1'].mean()],
                       'Train ROC/AUC Score': [cv['train_roc_auc'].mean()],
                       'Test ROC/AUC Score': [cv['test_roc_auc'].mean()]}
    
    
    # checking for overfit
    if abs(cv_results_dict['Train Accuracy'] - cv_results_dict['Test Accuracy']) > .5 or\
       abs(cv_results_dict['Train Precision'] - cv_results_dict['Test Precision']) > .5 or\
       abs(cv_results_dict['Train Recall'] - cv_results_dict['Test Recall']) > .5 or\
       abs(cv_results_dict['Train F1 Score'] - cv_results_dict['Test F1 Score']) > .5 or\
       abs(cv_results_dict['Train ROC/AUC Score'] - cv_results_dict['Test ROC/AUC Score']) > .5:
           cv_results_dict['Overfit?'] = ['True']
    else:
        cv_results_dict['Overfit?'] = ['False']
    
    
    
    
    if type(cv_score_card) == pd.core.frame.DataFrame:
        cv_score_card = pd.concat([cv_score_card, pd.DataFrame(cv_results_dict)], ignore_index=True)
        return(cv_score_card.drop_duplicates())
    else:
        print(pd.DataFrame([cv_score_card]))