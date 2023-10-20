import re

from typing import List

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, OptionValue, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '5c39bc6c-7921-4296-a6b6-5445436b2c6c'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'summing_node'
    displayName: str = 'Summing node'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'Суммирует 2 числа, одно из которых в формате строки'
    properties: List[Property] = [
        Property(
            displayName='Введите число',
            name='number_in_line',
            type=Property.Type.STRING,
            description='Данное число будет считываться в виде строки. Если ' \
                        'в строке будут найдены символы, то число будет разделено ' \
                        'Пример: 123d2 -> 123 и 2',
            required=True,
            default='0',
        ),
        Property(
            displayName='Введите число',
            name='number',
            type=Property.Type.NUMBER,
            required=True,
            default=0,
        ),
        Property(
            displayName='Переключатель',
            name='switch',
            type=Property.Type.OPTIONS,
            description='Формат вывода результата',
            required=True,
            options=[
                OptionValue(name='Вывод в формате строки',value='string'), 
                OptionValue(name='Вывод в формате числа', value='number')
                ],
        )
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            _find_numbers = re.findall(r"-\d+|\d+", json.node.data.properties['number_in_line'])    
            _sum_numbers = sum([int(number) for number in _find_numbers])\
                           + json.node.data.properties['number']
            _dictionary_of_conclusions = {
                'string': str(_sum_numbers),
                'number': _sum_numbers
                }
            _json_response = {"result": _dictionary_of_conclusions[json.node.data.properties['switch']]}
            
            if len(_find_numbers) != 1:
                _warning_text = "Возможно вы имели в виду число "  \
                f"{0 if len(_find_numbers) == 0 else ''.join(_find_numbers)} " \
                "в текстовом формате? Если да, то оставьте в поле ввода только цифры"
                _json_response['warning_message'] = _warning_text

            await json.save_result(_json_response)
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
