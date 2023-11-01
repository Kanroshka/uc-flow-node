from typing import Union

from uc_flow_nodes.schemas import NodeRunContext as BaseNodeRunContext
from uc_flow_schemas.flow import Node as BaseNode

from node.provider.alfacrm import Authorization, GetCustomersFilteredAndPaging, UpdateCustomer, CreateCustomer


class NodeRunContext(BaseNodeRunContext):
    class Node(BaseNode):
        class Data(BaseNode.Data):
            properties: Union[
                Authorization,
                GetCustomersFilteredAndPaging,
                UpdateCustomer,
                CreateCustomer,
            ]
        data: Data
    node: Node
    