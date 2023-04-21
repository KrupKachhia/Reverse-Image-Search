from libraries import *
from config import *


def models():
    model=ResNet50(weights='imagenet',
                   include_top=False,
                    input_shape=(IMG_SIZE, IMG_SIZE,3),
                   pooling='max')

    img_gen = ImageDataGenerator(preprocessing_function = preprocess_input)
    datagen = img_gen.flow_from_directory(ROOT_DIR,
                                        target_size = (IMG_SIZE, IMG_SIZE),
                                        batch_size = BATCH_SIZE,
                                        class_mode = None,
                                        shuffle = False)
    
    return model, datagen

def feature():
    model, datagen = models()
    model.summary()

    num_images = len(datagen.filenames)
    num_epochs = int(math.ceil(num_images / BATCH_SIZE))

    feature_list = model.predict(datagen, num_epochs)
    print("Num images = ", len(datagen.filenames))
    print("Shape of feature_list = ", feature_list.shape)

    np.save(os.path.join('saver', 'feature_ResNet50.npy'),feature_list)
