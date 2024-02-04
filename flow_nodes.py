
from .any import Any

any = Any("*")

from .globals import DIRECTORY_NAME

GROUP_NAME = "flow-control"
class Swap: 
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"val1":(any,),
                     "val2":(any,),
                     "doSwap":("BOOLEAN",)
                     }
                }
    RETURN_TYPES = (any,any)
    RETURN_NAMES = ("valA","valB")
    FUNCTION = "swap"
    CATEGORY = DIRECTORY_NAME+'/'+GROUP_NAME

    def swap(self, val1, val2, doSwap: bool):
        if doSwap:
            return val2, val1
        else:
            return val1, val2
        
NODE_CLASS_MAPPINGS: dict = {
    "Swap": Swap
}