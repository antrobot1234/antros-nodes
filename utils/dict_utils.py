from collections import UserDict
class Entry:
    def __init__(self, value = None, typedef = None, default = None):
        if typedef == None and value == None and default == None: self.unsafe = True
        else: self.unsafe = False
        if default != None and value == None: value = default
        if value != None:
            if typedef != None: 
                try: value = typedef(value)
                except: raise Exception(f"Could not convert {value} to {typedef}")
            else: typedef = type(value)
        if typedef != None:
            try: default = typedef() if default == None else typedef(default)
            except: print("could not populate default")
        
        self.typedef = typedef
        self.default = default
        self.value = value
    def __repr__(self) -> str:
        return f"{self.value}::{self.typedef.__name__}[{self.default}]"
    def is_type(self, type):
        return self.typedef == type
    def type_equals(self, other):
        if self.unsafe or other.unsafe: return True
        return self.typedef == other.typedef
    def get_value(self):
        if self.value == None: return self.default
        return self.value
    def cast_value(self, type):
        try:
            self.value = type(self.value)
        except: raise Exception(f"Could not cast {self.value} to {type}")
class EntryDict(UserDict):
    def __setitem__(self, key,item) -> None:
        if not isinstance(item, Entry):
            try:
                item = Entry(item)
            except ValueError:
                raise Exception(f"Could not convert {item} to Entry")
        return super().__setitem__(key, item)
    def get_by_reference(self, key, reference : Entry) -> Entry:
        entry = self.get(key, reference)
        if entry is not reference:
            if entry.type_equals(reference):
                return entry
            #try to cast entry to reference type
            else: entry.cast_value(reference.typedef)
        return entry

def get_pipe_value(pipe, name):
    if name == "model": return pipe[0]
    if name == "clip": return pipe[1]
    if name == "vae": return pipe[2]
    if name == "positive": return pipe[3]
    if name == "negative": return pipe[4]
    return None