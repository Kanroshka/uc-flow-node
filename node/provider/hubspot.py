from json import JSONDecodeError
from typing import Literal, List, Optional
from urllib.parse import urljoin

import ujson
from pydantic import BaseModel, AnyHttpUrl, parse_obj_as
from uc_http_requester.requester import Request

from node.schemas.enums import (
    Path, 
    Resource, 
    Operation, 
    BASE_URL_API, 
    Properties, 
    Association, 
    BASE_URL_API_v3, 
    JsonMethods
    )
from node.schemas.models import (
    DealAmount,
    DealCloseDate,
    DealCloseDate,
    DealName,
    DealPipeline,
    DealStage,
    AssociationImmediatelyToId,
    AssociationImmediatelyCategory,
    AssociationImmediatelyTypeId,
    ContactCompany,
    ContactEmail,
    ContactFirstname,
    ContactLastname,
    ContactLifecyclestage,
    ContactPhone,
    ContactWebsite,
    AssociationsFirst,
    AssociationsSecond,
    AssociationSeparatelyFromId,
    AssociationSeparatelyToId,
    AssociationSeparatelyType,
    )


class Config:
    arbitrary_types_allowed = True


class BaseProperties(BaseModel):
    pass


class BaseAssociations(BaseModel):
    pass


class Action(BaseModel):
    path: Optional[str]
    json_methods: Optional[Request.Method]
    resource: Optional[str]
    access_token: str

    @staticmethod
    def validate_response(response: dict) -> [dict, List[dict]]:
        try:
            print(str(response.get('status_code')))
            if str(response.get('status_code'))[0] != '2':
                raise Exception(f'{response.get("status_code")=} {response.get("content")=}')
            
            if response.get('content'):
                content = ujson.loads(response.get('content'))
                if content.get('errors'):
                    raise Exception(f'content errors: {content=}')
            else:
                content = dict()

        except JSONDecodeError:
            raise Exception(JSONDecodeError)
        
        return content
    
    @staticmethod
    def get_attr(params, attr):
        obj = params.__getattribute__(attr)
        return obj[0].__getattribute__(attr) if obj else None
    
    @staticmethod
    def params_delete_none_object(params) -> dict:
        res: dict = {}
        for key, value in params.items():
            res.update({key: value}) if value is not None else ...

        return res
    
    @staticmethod
    def associations_delete_none_object(associations: list) -> bool:
        for value in associations:
            return False if value is None else ...
        
        return True

    def get_request_url(self) -> str:
        url = urljoin(BASE_URL_API_v3, self.path)

        return url
    
    def get_request_params(self) -> dict:
        return dict()

    def get_request(self, credentials_id: str) -> Request:
        if self.operation in [Operation.update_contact, Operation.delate_contact]:
            self.path += self.id_object['id'] 

        elif self.operation in [Operation.update_deal, Operation.delate_deal]:
            self.path += self.id_object['results'][0]['id']

        return Request(
            auth=credentials_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=self.json_methods,
            headers={
                'authorization': f'Bearer {self.access_token}'
            },
            json={
                **self.get_request_params(),
            },
        )

class Authorization(Action):
    path: str = Path.check_authorization
    json_methods: str = JsonMethods.check_authorization
    resource: Literal[Resource.check_authorization]
        
    def get_request(self, cr_id: str) -> Request:
        return Request(
            auth=cr_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=self.json_methods,
            headers={
                'Content-Type': 'application/json'
            },
            json={
                'tokenKey': self.access_token,
            },
        )
    
    def get_request_url(self) -> str:
        url = urljoin(BASE_URL_API, self.path)

        return url
    
class CreateDeal(Action):
    class Associations(BaseAssociations):
        association_immediately_to_id: Optional[List[AssociationImmediatelyToId]]
        association_immediately_category: Optional[List[AssociationImmediatelyCategory]]
        association_immediately_type_id: Optional[List[AssociationImmediatelyTypeId]]

    class Properties(BaseProperties):
        deal_amount: Optional[List[DealAmount]]
        deal_close_date: Optional[List[DealCloseDate]]
        deal_name: Optional[List[DealName]]
        deal_pipeline: Optional[List[DealPipeline]]
        deal_stage: Optional[List[DealStage]]

        
    path: str = Path.create_deal
    json_methods: str = JsonMethods.create_deal
    resource: Literal[Resource.deal]
    operation: Literal[Operation.create_deal]
    associations: Optional[Associations]
    properties: Optional[Properties]

    def get_request_params(self) -> dict:
        params = {}
        ass = self.associations
        f = self.properties
        
        if f:
            params['properties'] = {}
            params['properties']['amount']  = self.get_attr(f, Properties.deal_amount)
            params['properties']['closedate']  = self.get_attr(f, Properties.deal_close_date)
            params['properties']['dealname']  = self.get_attr(f, Properties.deal_name)
            params['properties']['pipeline']  = self.get_attr(f, Properties.deal_pipeline)
            params['properties']['dealstage']  = self.get_attr(f, Properties.deal_stage)
            params['properties']: dict = self.params_delete_none_object(params['properties'])

        
        if ass:
            associations_id = self.get_attr(ass, Association.association_immediately_to_id)
            associations_category = self.get_attr(ass, Association.association_immediately_category)
            associations_type_id  = self.get_attr(ass, Association.association_immediately_type_id)
            if self.associations_delete_none_object([associations_id, associations_category, associations_type_id]):
                params['associations']: dict = [{"to": {"id": associations_id}, "types":[{"associationCategory": associations_category, "associationTypeId": associations_type_id}]}]

        return params


class UpdateDeal(Action):
    class Properties(BaseProperties):
        deal_amount: Optional[List[DealAmount]]
        deal_close_date: Optional[List[DealCloseDate]]
        deal_name: Optional[List[DealName]]
        deal_pipeline: Optional[List[DealPipeline]]
        deal_stage: Optional[List[DealStage]]

    path: str = Path.update_deal
    json_methods: str = JsonMethods.update_deal
    resource: Literal[Resource.deal]
    operation: Literal[Operation.update_deal]
    properties: Optional[Properties]
    id_object: dict

    def get_request_params(self) -> dict:
        params = {}
        f = self.properties
        
        if f:
            params['properties'] = {}
            params['properties']['amount']  = self.get_attr(f, Properties.deal_amount)
            params['properties']['closedate']  = self.get_attr(f, Properties.deal_close_date)
            params['properties']['dealname']  = self.get_attr(f, Properties.deal_name)
            params['properties']['pipeline']  = self.get_attr(f, Properties.deal_pipeline)
            params['properties']['dealstage']  = self.get_attr(f, Properties.deal_stage)

            params['properties']: dict = self.params_delete_none_object(params['properties'])

        return params


class ReadDeal(Action):
    path: str = Path.read_deal
    json_methods: str = JsonMethods.read_deal
    resource: Literal[Resource.deal]
    operation: Literal[Operation.read_deal]
    id_object: dict

    
class DeleteDeal(Action):
    path: str = Path.delate_deal
    json_methods: str = JsonMethods.delate_deal
    resource: Literal[Resource.deal]
    operation: Literal[Operation.delate_deal]
    id_object: dict
    

class CreateContact(Action):
    class Properties(BaseProperties):
        contact_email: Optional[List[ContactEmail]]
        contact_firstname: Optional[List[ContactFirstname]]
        contact_lastname: Optional[List[ContactLastname]]
        contact_phone: Optional[List[ContactPhone]]
        contact_company: Optional[List[ContactCompany]]
        contact_website: Optional[List[ContactWebsite]]
        contact_lifecyclestage: Optional[List[ContactLifecyclestage]]


    class Associations(BaseAssociations):
        association_immediately_to_id: Optional[List[AssociationImmediatelyToId]]
        association_immediately_category: Optional[List[AssociationImmediatelyCategory]]
        association_immediately_type_id: Optional[List[AssociationImmediatelyTypeId]]
        
    path: str = Path.create_contact
    json_methods: str = JsonMethods.create_contact
    resource: Literal[Resource.contact]
    operation: Literal[Operation.create_contact]
    properties: Optional[Properties]
    associations: Optional[Associations]
    
    def get_request_params(self) -> dict:
        params = {}
        f = self.properties
        ass = self.associations
        
        if f:
            params['properties'] = {}
            params['properties']['email']  = self.get_attr(f, Properties.contact_email)
            params['properties']['firstname']  = self.get_attr(f, Properties.contact_firstname)
            params['properties']['lastname']  = self.get_attr(f, Properties.contact_lastname)
            params['properties']['phone']  = self.get_attr(f, Properties.contact_phone)
            params['properties']['company']  = self.get_attr(f, Properties.contact_company)
            params['properties']['website']  = self.get_attr(f, Properties.contact_website)
            params['properties']['lifecyclestage']  = self.get_attr(f, Properties.contact_lifecyclestage)

            params['properties']: dict = self.params_delete_none_object(params['properties'])
        
        if ass:
            associations_id = self.get_attr(ass, Association.association_immediately_to_id)
            associations_category = self.get_attr(ass, Association.association_immediately_category)
            associations_type_id  = self.get_attr(ass, Association.association_immediately_type_id)
            if self.associations_delete_none_object([associations_id, associations_category, associations_type_id]):
                params['associations']: dict = [{"to": {"id": associations_id}, "types":[{"associationCategory": associations_category, "associationTypeId": associations_type_id}]}]

        return params


class UpdateContact(Action):
    class Properties(BaseProperties):
        contact_email: Optional[List[ContactEmail]]
        contact_firstname: Optional[List[ContactFirstname]]
        contact_lastname: Optional[List[ContactLastname]]
        contact_phone: Optional[List[ContactPhone]]
        contact_company: Optional[List[ContactCompany]]
        contact_website: Optional[List[ContactWebsite]]
        contact_lifecyclestage: Optional[List[ContactLifecyclestage]]

    path: str = Path.update_contact
    json_methods: str = JsonMethods.update_contact
    resource: Literal[Resource.contact]
    operation: Literal[Operation.update_contact]
    properties: Optional[Properties]
    id_object: dict

    def get_request_params(self) -> dict:
        params = {}
        f = self.properties
        
        if f:
            params['properties'] = {}
            params['properties']['email']  = self.get_attr(f, Properties.contact_email)
            params['properties']['firstname']  = self.get_attr(f, Properties.contact_firstname)
            params['properties']['lastname']  = self.get_attr(f, Properties.contact_lastname)
            params['properties']['phone']  = self.get_attr(f, Properties.contact_phone)
            params['properties']['company']  = self.get_attr(f, Properties.contact_company)
            params['properties']['website']  = self.get_attr(f, Properties.contact_website)
            params['properties']['lifecyclestage']  = self.get_attr(f, Properties.contact_lifecyclestage)

            params['properties']: dict = self.params_delete_none_object(params['properties'])

        return params
    
class DeleteContact(Action):
    path: str = Path.delate_contact
    json_methods: str = JsonMethods.delate_contact
    resource: Literal[Resource.contact]
    operation: Literal[Operation.delate_contact]
    id_object: dict


class CreateAssociation(Action):
    class Associations(BaseAssociations):
        association_separately_from_id: Optional[List[AssociationSeparatelyFromId]]
        association_separately_to_id: Optional[List[AssociationSeparatelyToId]]
        association_separately_type: Optional[List[AssociationSeparatelyType]]
        associations_first: Optional[List[AssociationsFirst]]
        associations_second: Optional[List[AssociationsSecond]]

    path: str = Path.create_association
    json_methods: str = JsonMethods.check_authorization
    resource: Literal[Resource.association]
    operation: Literal[Operation.create_association]
    associations: Optional[Associations]

    def get_request_url(self) -> str:
        ass = self.associations
        associations_first = self.get_attr(ass, Association.associations_first) + '/'
        associations_second = self.get_attr(ass, Association.associations_second) + Path.create_association_end

        first_part_url: str = urljoin(BASE_URL_API_v3, self.path)
        second_part_url: str = urljoin(associations_first, associations_second)

        return urljoin(first_part_url, second_part_url)

    def get_request(self, credentials_id: str) -> Request:
        return Request(
            auth=credentials_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url()),
            method=self.json_methods,
            headers={
                'authorization': f'Bearer {self.access_token}'
            },
            json={
                **self.get_request_params(),
            },
        )
    
    def get_request_params(self) -> dict:
        params = {}
        ass = self.associations

        if ass:
            from_id = self.get_attr(ass, Association.association_separately_from_id)['id']
            to_id = self.get_attr(ass, Association.association_separately_to_id)['results'][0]['id']
            type_objects = self.get_attr(ass, Association.association_separately_type)
            print(to_id)
            print(type(to_id))
            if self.associations_delete_none_object([from_id, to_id, type_objects]):
                params: dict = {
                    "inputs": [
                        {
                            "from": {"id": from_id},
                            "to": {"id": to_id},
                            "type": type_objects
                        }
                    ]
                }

        return params
