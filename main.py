import sys
from tensorflow import keras

MODEL_PATH='modelPulsar.h5'


# Load Tensorflow model
model = keras.models.load_model(MODEL_PATH)
print(model.summary())


if len(sys.argv)>0:
    try:

        arguments = sys.argv[1:]
        print(arguments)

        # Process the arguments
        #for arg in arguments:
        #    print(arg)


        print(model.predict([[float(i) for i in arguments]]))
    except:

        print("Error!")


else:
    print('0 or more than 1 arguments received')