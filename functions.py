import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, plot_confusion_matrix, \
                            accuracy_score, roc_auc_score, precision_score,\
                            recall_score, f1_score
from sklearn.utils.validation import check_is_fitted


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
    plot_confusion_matrix(model, 
                          X_train, 
                          y_train, 
                          ax=ax[0], 
                          normalize=normalize)
    ax[0].set_title('Train Results', size=15)

    # Test Confusion Matrix
    plot_confusion_matrix(model, 
                          X_test, 
                          y_test, 
                          ax=ax[1],
                          normalize=normalize)
    ax[1].set_title('Test Results', size=15)



    
    
    # setting it to check if scorecard entered or just running a quick run
    
    score_dict = {'Name': model_name, 
                  'Accuracy':accuracy_score(y_test, model.predict(X_test)),
                  'Precision': precision_score(y_test, model.predict(X_test), zero_division=0),
                  'Recall': recall_score(y_test, model.predict(X_test), zero_division=0),
                  'F1 Score': f1_score(y_test, model.predict(X_test), zero_division=0),
                  'ROC/AUC Score': roc_auc_score(y_test, model.predict(X_test))}
    if type(score_card) == pd.core.frame.DataFrame:
        score_card = score_card.append(score_dict, ignore_index=True)
        return(score_card.drop_duplicates())
    else:
        print(pd.DataFrame([score_dict]))