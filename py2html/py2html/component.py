from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Component:
    children: Any = None
    classes: str = None
    style: Dict = None
    id: str = None

    def generate_html(self):
        '''
        '''
        # open tag
        list_ = [f"<{self.tag}"]

        # set html component attributes
        attrs_ = [x for x in list(self.__dict__.keys()) if x not in ['tag', 'children']]
        for attr_ in attrs_:
            if getattr(self, attr_) is not None:
                list_.append(f"{attr_}='{getattr(self, attr_)}'")
        list_.append(f">")

        # create children
        if isinstance(self.children, str):
            list_.append(f"{self.children}")
        elif isinstance(self.children, list):
            for child_ in self.children:
                list_.append(child_.generate_html())
        else:
            pass

        # close tag
        list_.append(f"</{self.tag}>")

        return ' '.join(list_)

@dataclass
class Div(Component):
    tag: str = 'div'

@dataclass
class P(Component):
    tag: str = 'p'

@dataclass
class Img(Component):
    tag: str = 'img'
    src: str = None
    alt: str = None

@dataclass
class A(Component):
    tag: str = 'a'
    target: str = None
    title: str = None
