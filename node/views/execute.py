from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState

from node.provider.alfacrm import Action
from node.schemas.node import NodeRunContext
from node.schemas.enums import Resource

class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            credentials = await json.get_credentials()

            action: Action = json.node.data.properties 
            request = action.get_request(credentials.id, credentials.data)
            
            base_response = await json.requester.request(request)
            response = json.node.data.properties.validate_response(base_response)

            await self.request_json.save_result(response)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
    