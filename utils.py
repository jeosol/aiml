from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

def create_nn_model(hidden_layers_units, output_layer_unit):
    "Create an NN model architectures."
    # create the sequential model
    model = keras.models.Sequential()
    # Add a flattening layer
    model.add(keras.layers.Flatten(input_shape=[28,28]))
    # Loop over the hidden layers
    for hidden_layer_unit in hidden_layers_units:
        # Add the hidden layers with relu activation
        model.add(keras.layers.Dense(hidden_layer_unit, activation='relu'))
        
    # Add the output layer with softmax activation (we have 10 independent and exclusive outcomes: digits 0 to 9)
    model.add(keras.layers.Dense(output_layer_unit, activation='softmax'))
    # compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
    # Add the model to the list of models
    return model, 'hidden_layers_neurons' + str(hidden_layers_units)

def create_nn_models(hidden_layer_infos, output_layer_unit):
    "Create multiple hidden NN model architectures"
    num_nns = len(hidden_layer_infos)
    models = []
    casenames=[]
    for hidden_layer_units in hidden_layer_infos:
        model, casename = create_nn_model(hidden_layer_units, output_layer_unit)
        models.append(model)
        casenames.append(casename)

    return models, casenames
                
def run_nn_models(X_train, y_train, X_valid, y_valid, hidden_layers_infos, output_layer_unit, epochs=10, verbose=0):
    models, casenames = create_nn_models(hidden_layers_infos, output_layer_unit)

    model_outputs = []
    for model, info in zip(models, casenames):
        history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_valid, y_valid), verbose=verbose)        
        model_outputs.append((info, history, model))
    
    for (info, history,_) in model_outputs:
        train_loss = history.history['loss']
        train_accu = history.history['accuracy']
        val_loss = history.history['val_loss']
        val_accu = history.history['val_accuracy']
        print(f'#hidden_layer(s)={info} Cost={train_loss}, Accuracy={train_accu} Val_Cost={val_loss}, Val_Accuracy={val_accu}')

    return model_outputs, casenames
    # plot the model training and validation accuracy
    # plot_info(model_outputs, case_names)
    
def plot_info(model_outputs, case_names):
    fig, axs = plt.subplots(2,2, figsize=(15,15))
    for (_,history,_) in model_outputs:        
        axs[0,0].plot(range(len(history.history['accuracy'])), history.history['accuracy'])
    axs[0,0].set_title('Training Accuracy')
    axs[0,0].set_xlabel('Epochs')
    axs[0,0].set_ylabel('Accuracy')
    axs[0,0].legend(case_names)
    axs[0,0].grid(True)
    axs[0,0].set_ylim(0,1)
    #axs[0,0].show()
    
    for (_,history,_) in model_outputs:
        #pd.DataFrame(history.history).plot(figsize=(8,5))
        axs[0,1].plot(range(len(history.history['val_accuracy'])), history.history['val_accuracy'])
    axs[0,1].set_title('Validation Accuracy')
    axs[0,1].set_xlabel('Epochs')
    axs[0,1].set_ylabel('Accuracy')
    axs[0,1].legend(case_names)
    axs[0,1].grid(True)
    #axs[0,1].gca().set_ylim(0,1)
    axs[0,1].set_ylim(0,1)
    #axs[0,1].show()

    for (_,history,_) in model_outputs:        
        axs[1,0].plot(range(len(history.history['loss'])), history.history['loss'])
    axs[1,0].set_title('Training Loss')
    axs[1,0].set_xlabel('Epochs')
    axs[1,0].set_ylabel('Loss')
    axs[1,0].legend(case_names)
    axs[1,0].grid(True)
    axs[1,0].set_ylim(0,1)
    #axs[1,0].show()
    
    for (_,history,_) in model_outputs:
        #pd.DataFrame(history.history).plot(figsize=(8,5))
        axs[1,1].plot(range(len(history.history['val_loss'])), history.history['val_loss'])
    axs[1,1].set_title('Validation Loss')
    axs[1,1].set_xlabel('Epochs')
    axs[1,1].set_ylabel('Loss')
    axs[1,1].legend(case_names)
    axs[1,1].grid(True)
    axs[1,1].set_ylim(0,1)
    #axs[1,1].show()

