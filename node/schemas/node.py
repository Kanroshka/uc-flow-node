from typing import Union

from uc_flow_nodes.schemas import NodeRunContext as BaseNodeRunContext
from uc_flow_schemas.flow import Node as BaseNode

from node.provider.hubspot import (
    Authorization,
    CreateContact, 
    CreateDeal, 
    CreateAssociation, 
    UpdateContact, 
    UpdateDeal, 
    DeleteContact, 
    DeleteDeal, 
    ReadDeal,
    )


class NodeRunContext(BaseNodeRunContext):
    class Node(BaseNode):
        class Data(BaseNode.Data):
            properties: Union[
                Authorization,
                CreateContact,
                CreateDeal,
                CreateAssociation, 
                UpdateContact, 
                UpdateDeal, 
                DeleteContact, 
                DeleteDeal,
                ReadDeal,
            ]
        data: Data
    node: Node
    