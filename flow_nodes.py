
from .utils.globals import DIRECTORY_NAME, Any
from nodes import ConditioningConcat
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
GROUP_NAME = "flow-control"
any = Any("*")
class Swap: 
    @classmethod
    def INPUT_TYPES(cls):
        return {"required":
                    {"val1":(any,),
                     "val2":(any,),
                     "doSwap":("BOOLEAN",)
                     }
                }
    RETURN_TYPES = (any,any)
    RETURN_NAMES = ("valA","valB")
    FUNCTION = "swap"

    def swap(self, val1, val2, doSwap: bool):
        if doSwap:
            return val2, val1
        else:
            return val1, val2
class OptionalConditioningConcat(ConditioningConcat):
    @classmethod
    def INPUT_TYPES(cls):
        return {
                "required":{},
                "optional":
                    {"conditioning_to":("CONDITIONING",),
                     "conditioning_from":("CONDITIONING",)}
        }
    def concat(self, conditioning_to = None, conditioning_from = None) -> tuple:
        if conditioning_from is None and conditioning_to is None:
            raise Exception("conditioning_to and conditioning_from cannot both be None")
        if conditioning_from is None:
            return (conditioning_to,)
        if conditioning_to is None:
            return (conditioning_from,)
        return super().concat(conditioning_to, conditioning_from)
class OptionalBasicPipe:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                "required":{},
                "optional":{
                    "MODEL":("MODEL",),
                    "CLIP":("CLIP",),
                    "VAE":("VAE",),
                    "POSITIVE":("CONDITIONING",),
                    "NEGATIVE":("CONDITIONING",)
                    }
        }
    RETURN_TYPES = ("BASIC_PIPE",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "pipe"
    def pipe(self, model = None, clip = None, vae = None, positive = None, negative = None):
        return ((model, clip, vae, positive, negative),)
    
def register(node_class: type,class_name : str, display_name : str):
    NODE_CLASS_MAPPINGS[class_name] = node_class
    NODE_DISPLAY_NAME_MAPPINGS[class_name] = display_name
    node_class.CATEGORY = DIRECTORY_NAME+'/'+GROUP_NAME

register(Swap, "Swap", "Swap")
register(OptionalConditioningConcat, "OptionalConditioningConcat", "Op. Conditioning (Concat)")
register(OptionalBasicPipe, "OptionalBasicPipe", "Op. Basic Pipe")
