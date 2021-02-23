### Report 
  - **Model**: CRNN  + Connectionist temporal loss (CTC) loss
  - **Reason**: CRNN worked very well in similar license plate dataset. which makes it better baseline to start with.
  Since dataset size is small,heavy models such as efficient-backbone will prone to overfit 
  - **Possible Improvements that can done**:
    - using LPRNet  instead of CRNN
    - adding more data
    - training data augumentation
  - **Accuracy**: 73% (Test Set) 
  - hyper parameters and other training details are in notebooks/training&evaulation.ipynb 
