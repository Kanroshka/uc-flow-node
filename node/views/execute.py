from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState

from node.schemas.enums import FirstField, SecondField


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            data = json.node.data.properties
            json_response = {}

            match data:
                case {'email_field': json_email, 
                      'first_field': FirstField.first_value,
                      'second_field': SecondField.first_value}:
                    json_response['email'] = json_email


            await json.save_result(json_response)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
    