from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

def create_nn_models(nn_hlayer_info):
    "Create NN model architectures."
    num_nns = len(nn_hlayer_info)
    all_models = []
    for info in nn_hlayer_info:
        # create the sequential model
        model = keras.models.Sequential()
        # Add a flattening layer
        model.add(keras.layers.Flatten(input_shape=[28,28]))
        # Add the hidden layers with relu activation
        for hh_units in info:
            model.add(keras.layers.Dense(hh_units, activation='relu'))
        # Add the output layer with softmax activation (we have 10 independent and exclusive outcomes: digits 0 to 9)
        model.add(keras.layers.Dense(10, activation='softmax'))
        # compile the model
        model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
        # Add the model to the list of models
        all_models.append(model)
        
    return all_models
        
def run_nn_models(nn_info, epochs=10, verbose=0):
    nn_models = create_nn_models(nn_info)
    case_names = ['hidden_layers' + str(info) for info in nn_info]
    model_outputs = []
    for model, info in zip(nn_models, nn_info):
        history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_valid, y_valid), verbose=verbose)        
        model_outputs.append((info, history, model))
    
    for (info, history,_) in model_outputs:
        train_loss = history.history['loss']
        train_accu = history.history['accuracy']
        val_loss = history.history['val_loss']
        val_accu = history.history['val_accuracy']
        print(f'#hidden_layer(s)={info} Cost={train_loss}, Accuracy={train_accu} Val_Cost={val_loss}, Val_Accuracy={val_accu}')
    
    # plot the model training and validation accuracy
    plot_info(model_outputs, case_names)
    
    return model_outputs

def plot_info(model_outputs, case_names):
    for (_,history,_) in model_outputs:        
        plt.plot(range(len(history.history['accuracy'])), history.history['accuracy'])
    plt.title('Training Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend(case_names)
    plt.grid(True)
    plt.gca().set_ylim(0,1)
    plt.show()
    
    for (_,history,_) in model_outputs:
        #pd.DataFrame(history.history).plot(figsize=(8,5))
        plt.plot(range(len(history.history['val_accuracy'])), history.history['val_accuracy'])
    plt.title('Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend(case_names)
    plt.grid(True)
    plt.gca().set_ylim(0,1)
    plt.show()
    
