# NFS Payback AI
 AI plays NFS Payback

It uses image recognition to predict the next best action

[RR, FL, RL, FR,] ->  Are different possible values that the model predicts.

It uses alexNet model architechture preferably because it performs well on tensor.

All the model details are logged using tensorboard.

The model has been trained for 1000 epochs, and it performs well, particualrly in predicting FR, FL.

The inferencing is made on the go, using the imageGrab, the image is converted to array as needed by the model and the model returs a list of possible actions as mentioned above, the keyPress is taken care by  the microsoft keyPress winAPI simulating a keyPress while the game is in the active window. 
