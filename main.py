from typing import Any
import tensorflow as tf
import importlib.util


"""
Explaination for the service.
The model platform service provide several available tasks once the service is deployed:
1. Build a model with given model file path, save it with given path.
2. Load a model if exist in the path and show avaliable call functions.
3. Train the current model with given data.
4. 
"""



class Model_platform_service:
    def __init__(self) -> None:
        self._has_model = 0
        self._train_epoch = 0
        print("accept function: 1. build_and_save_model, 2. load model, ")
    
    def save_model(self, model, save_path) -> bool:
        if self._has_model == 0:
            print("Failed to save the model.")
            return False
        tf.saved_model.save(model, save_path)
        print("Save the model successfully.")
        return True

    def build_and_save_model(self, model_def, model_path = "./src/model/model.py", save_path = "./src/save") -> bool:
        # Cannot build one if there exist one.
        if self._has_model == 1:
            return False 
        
        # import the model module
        spec = importlib.util.spec_from_file_location("model_module", model_path)
        md = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(md)

        # Otherwise build the model and save it 
        model = md.model_def()
        self._has_model = 1

        # Save the model
        if self.save_model(model, save_path):
            return True
        return False
    
    def load_model(self, model_path, )

