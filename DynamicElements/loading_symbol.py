from dynamic_element import DynamicElement

class LoadingSymbol(DynamicElement):
    def __init__(self, frame:int =0) -> None:
        self.frame = frame
    
    def render(self) -> str:
        match self.frame % 4:
            case 0:
                return '/'
            case 1:
                return '-'
            case 2:
                return "\\"
            case 3:
                return '|'
        return ''
        
    def increment_frame(self):
        self.frame += 1