from libraries import *
from config import *
from model import models

def train(N_PICS, feature_list):
    model, datagen = models()
    filenames = [ROOT_DIR + '/' + s for s in datagen.filenames]

    neighbors = NearestNeighbors(n_neighbors = N_PICS,
                             algorithm = 'ball_tree',
                             metric = 'euclidean')

    neighbors.fit(feature_list)    

    return model, neighbors, filenames

def upload(N_PICS, file_path):
    feature_list = np.load(os.path.join('saver', 'feature_ResNet50.npy'))
    model, neighbors, filename = train(N_PICS, feature_list)

    img_path = file_path  # To predict
    input_shape = (IMG_SIZE, IMG_SIZE, 3)
    img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    test_img_features = model.predict(preprocessed_img, batch_size=1)

    _, indices = neighbors.kneighbors(test_img_features)


    return indices[0], filename
        

