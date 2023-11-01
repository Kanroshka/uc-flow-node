from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)


class CredentialType(flow.CredentialType):
    id: str = 'alfacrm_api_auth'
    is_public: bool = True
    displayName: str = 'AlfaCRM API Auth'
    protocol: CredentialProtocol = CredentialProtocol.ApiKey
    protected_properties: List[Property] = []
    properties: List[Property] = [
        Property(
            displayName='hostname',
            name='hostname',
            type=Property.Type.STRING,
            default='https://(hostname)',
        ),
        Property(
            displayName='API key',
            name='api_key',
            type=Property.Type.STRING,
        ),
        Property(
            displayName='email',
            name='auth_email',
            type=Property.Type.STRING,
            default='example@mail.com',
        ),
    ]
    extends: Optional[List[str]] = []
    