from typing import List, Optional
from dataclasses import dataclass
from .login_emp import LoginEmp  

@dataclass
class WIDManagerListModel:
    W_ID: int
    managerList: Optional[List[LoginEmp]] = None
