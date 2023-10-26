from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (Property,
                                  OptionValue, 
                                  DisplayOptions)

from node.schemas.enums import FirstField, SecondField


class NodeType(flow.NodeType):
    id: str = '2cfb402c-5a5e-4686-b0a6-3f9de7aa74b7'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'holihop'
    displayName: str = 'Example holihop'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    version: int = 1
    description: str = 'Example holihop'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Переключатель',
            name='toggle',
            type=Property.Type.BOOLEAN,
            required=True,
            default=False,
        ),
        Property(
            displayName='Первое поле со значением',
            name='first_field',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=FirstField.first_value,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=FirstField.second_value,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ]
                }
            )
        ),
        Property(
            displayName='Второе поле со значением',
            name='second_field',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=SecondField.first_value,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=SecondField.second_value,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ]
                }
            )

        ),
        Property(
            displayName='Поле для ввода почты',
            name='email_field',
            type=Property.Type.STRING,
            placeholder='example@mail.ru',
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ],
                    'first_field': [
                        FirstField.first_value,
                    ],
                    'second_field': [
                        SecondField.first_value,
                    ]
                }
            )
        ),
        Property(
            displayName='Поле для ввода даты и времени',
            name='datetime_field',
            type=Property.Type.DATETIME,
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ],
                    'first_field': [
                        FirstField.second_value,
                    ],
                    'second_field': [
                        SecondField.second_value,
                    ]
                }
            )
        )
    ]
