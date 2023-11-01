from json import JSONDecodeError
from typing import Literal, List, Optional
from urllib.parse import urljoin

import ujson
from pydantic import BaseModel, AnyHttpUrl, parse_obj_as
from uc_http_requester.requester import Request

from node.schemas.enums import URL_API_V2, Path, Api, Resource, Operation, Parameters
from node.schemas.models import (
    CustomerId,
    CustomerName,
    CustomerBranchIds,
    CustomerTeacherIds,
    CustomerIsStudy,
    CustomerStudyStatusId,
    CustomerLeadSourceId,
    CustomerAssignedId,
    CustomerLegalType,
    CustomerLegalName,
    CustomerCompanyId,
    CustomerDob,
    CustomerBalance,
    CustomerPhone,
    CustomerEmail,
    CustomerWeb,
    CustomerNote,
    CustomerGender,
    CustomerAgeFrom,
    CustomerAgeTo,
    CustomerLessonCountFrom,
    CustomerLessonCountTo,
    CustomerBalanceContractFrom,
    CustomerBalanceContractTo,
    CustomerBalanceBonusFrom,
    CustomerBalanceBonusTo,
    CustomerRemoved,
    CustomerRemovedFrom,
    CustomerRemovedTo,
    CustomerLevelId,
    CustomerEmployeeId,
    CustomerColor,
    CustomerDateFrom,
    CustomerDateTo,
    CustomerNextLessonDateFrom,
    CustomerNextLessonDateTo,
    CustomerTariffTillFrom,
    CustomerTariffTillTo,
    CustomerRejectId,
    CustomerComment,
    CustomerDobFrom,
    CustomerDobTo,
    CustomerWithGroupsTrue,
    )


class Config:
    arbitrary_types_allowed = True

class BaseParameters(BaseModel):
    pass

class Action(BaseModel):
    path: Optional[str]
    api: Optional[str]
    resource: Optional[str]
    auth_key: Optional[dict]
    branch: Optional[str]

    @staticmethod
    def validate_response(response: dict) -> [dict, List[dict]]:
        try:
            if response.get('status_code') != 200:
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

    def get_request_url(self, base_url: str, branch: str = None) -> str:
        api_url: str = URL_API_V2
        if self.resource != Resource.authorization:
            api_url += f"{branch}/"
        url = urljoin(urljoin(base_url, api_url), self.path)

        return url
    
    def get_request_params(self) -> dict:
        return dict()

    def get_request(self, credential_id: str, credentials: dict) -> Request:
        if self.operation == Operation.update_customer:
            self.path += self.id_customer 
            
        return Request(
            auth=credential_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url(credentials['hostname'], self.branch)),
            method=Request.Method.post,
            headers={
                'X-ALFACRM-TOKEN': self.auth_key['token'],
            },
            json={
                **self.get_request_params(),
            },
        )

class Authorization(Action):
    path: str = Path.authorization
    api: Literal[Api.url_api_v2]
    resource: Literal[Resource.authorization]
        
    def get_request(self, credential_id: str, credentials: dict) -> Request:
        return Request(
            auth=credential_id,
            url=parse_obj_as(AnyHttpUrl, self.get_request_url(credentials['hostname'])),
            method=Request.Method.post,
            json={
                'email': credentials['email'],
                'api_key': credentials['api_key'],
            },
        )
    
class GetCustomersFilteredAndPaging(Action):
    class Parameters(BaseParameters):
        customer_id: Optional[List[CustomerId]]
        customer_is_study: Optional[List[CustomerIsStudy]]
        customer_study_status_id: Optional[List[CustomerStudyStatusId]]
        customer_name: Optional[List[CustomerName]]
        customer_gender: Optional[List[CustomerGender]]
        customer_age_from: Optional[List[CustomerAgeFrom]]
        customer_age_to: Optional[List[CustomerAgeTo]]
        customer_phone: Optional[List[CustomerPhone]]
        customer_legal_type: Optional[List[CustomerLegalType]]
        customer_legal_name: Optional[List[CustomerLegalName]]
        customer_company_id: Optional[List[CustomerCompanyId]]
        customer_lesson_count_from: Optional[List[CustomerLessonCountFrom]]
        customer_lesson_count_to: Optional[List[CustomerLessonCountTo]]
        customer_balance_contract_from: Optional[List[CustomerBalanceContractFrom]]
        customer_balance_contract_to: Optional[List[CustomerBalanceContractTo]]
        customer_balance_bonus_from: Optional[List[CustomerBalanceBonusFrom]]
        customer_balance_bonus_to: Optional[List[CustomerBalanceBonusTo]]
        customer_lead_source_id: Optional[List[CustomerLeadSourceId]]
        customer_assigned_id: Optional[List[CustomerAssignedId]]
        customer_note: Optional[List[CustomerNote]]
        customer_removed: Optional[List[CustomerRemoved]]
        customer_removed_from: Optional[List[CustomerRemovedFrom]]
        customer_removed_to: Optional[List[CustomerRemovedTo]]
        customer_level_id: Optional[List[CustomerLevelId]]
        customer_employee_id: Optional[List[CustomerEmployeeId]]
        customer_color: Optional[List[CustomerColor]]
        customer_date_from: Optional[List[CustomerDateFrom]]
        customer_date_to: Optional[List[CustomerDateTo]]
        customer_next_lesson_date_from: Optional[List[CustomerNextLessonDateFrom]]
        customer_next_lesson_date_to: Optional[List[CustomerNextLessonDateTo]]
        customer_tariff_till_from: Optional[List[CustomerTariffTillFrom]]
        customer_tariff_till_to: Optional[List[CustomerTariffTillTo]]
        customer_reject_id: Optional[List[CustomerRejectId]]
        customer_comment: Optional[List[CustomerComment]]
        customer_dob_from: Optional[List[CustomerDobFrom]]
        customer_dob_to: Optional[List[CustomerDobTo]]
        customer_with_groups_true: Optional[List[CustomerWithGroupsTrue]] 

    path: str = Path.get_customers_filtered_and_paging
    api: Literal[Api.url_api_v2]
    resource: Literal[Resource.customer]
    operation: Literal[Operation.get_customers_filtered_and_paging]
    parameters: Optional[Parameters]
    page: Optional[int]
    

    def get_request_params(self) -> dict:
        params = {}
        f = self.parameters
        
        if f:
            params["id"] = self.get_attr(f, Parameters.customer_id)
            params["is_study"] = self.get_attr(f, Parameters.customer_is_study)
            params["study_status_id"] = self.get_attr(f, Parameters.customer_study_status_id)
            params["name"] = self.get_attr(f,Parameters.customer_name)
            params["gender"] = self.get_attr(f, Parameters.customer_gender)
            params["age_from"] = self.get_attr(f, Parameters.customer_age_from)
            params["age_to"] = self.get_attr(f, Parameters.customer_age_to)
            params["phone"] = self.get_attr(f, Parameters.customer_phone)
            params["legal_type"] = self.get_attr(f, Parameters.customer_legal_type)
            params["legal_name"] = self.get_attr(f, Parameters.customer_legal_name)
            params["company_id"] = self.get_attr(f, Parameters.customer_company_id)
            params["lesson_count_from"] = self.get_attr(f, Parameters.customer_lesson_count_from)
            params["lesson_count_to"] = self.get_attr(f, Parameters.customer_lesson_count_to)
            params["balance_contract_from"] = self.get_attr(f, Parameters.customer_balance_contract_from)
            params["balance_contract_to"] = self.get_attr(f, Parameters.customer_balance_contract_to)
            params["balance_bonus_from"] = self.get_attr(f, Parameters.customer_balance_bonus_from)
            params["balance_bonus_to"] = self.get_attr(f, Parameters.customer_balance_bonus_to)
            params["lead_source_id"] = self.get_attr(f, Parameters.customer_lead_source_id)
            params["assigned_id"] = self.get_attr(f, Parameters.customer_assigned_id)
            params["note"] = self.get_attr(f, Parameters.customer_note)
            params["removed"] = self.get_attr(f, Parameters.customer_removed)
            params["removed_from"] = self.get_attr(f, Parameters.customer_removed_from)
            params["removed_to"] = self.get_attr(f, Parameters.customer_removed_to)
            params["level_id"] = self.get_attr(f, Parameters.customer_level_id)
            params["employee_id"] = self.get_attr(f, Parameters.customer_employee_id)
            params["color"] = self.get_attr(f, Parameters.customer_color)
            params["date_from"] = self.get_attr(f, Parameters.customer_date_from)
            params["date_to"] = self.get_attr(f, Parameters.customer_date_to)
            params["next_lesson_date_from"] = self.get_attr(f, Parameters.customer_next_lesson_date_from)
            params["next_lesson_date_to"] = self.get_attr(f, Parameters.customer_next_lesson_date_to)
            params["tariff_till_from"] = self.get_attr(f, Parameters.customer_tariff_till_from)
            params["tariff_till_to"] = self.get_attr(f, Parameters.customer_tariff_till_to)
            params["reject_id"] = self.get_attr(f, Parameters.customer_reject_id)
            params["comment"] = self.get_attr(f, Parameters.customer_comment)
            params["dob_from"] = self.get_attr(f, Parameters.customer_dob_from)
            params["dob_to"] = self.get_attr(f, Parameters.customer_dob_to)
            # params["withGroups:true"] = self.get_attr(f, Parameters.customer_with_groups_true)

        if self.page:
            params["page"] = self.page


        params: dict = self.params_delete_none_object(params)

        return params
    
class CreateCustomer(Action):
    class Parameters(BaseParameters):
        customer_name: Optional[List[CustomerName]]
        customer_is_study: Optional[List[CustomerIsStudy]]
        customer_legal_type: Optional[List[CustomerLegalType]]
        customer_branch_ids: Optional[List[CustomerBranchIds]]
    
    path: str = Path.create_customer
    api: Literal[Api.url_api_v2]
    resource: Literal[Resource.customer]
    operation: Literal[Operation.create_customer]
    parameters: Optional[Parameters]
    auth_key: Optional[dict]
    branch: Optional[str]

    def get_request_params(self) -> dict:
        params = {}
        f = self.parameters
        
        if f:
            params["name"] = self.get_attr(f, Parameters.customer_name)
            params["is_study"] = self.get_attr(f, Parameters.customer_is_study)
            params["legal_type"] = self.get_attr(f, Parameters.customer_legal_type)
            params["branch_id"] = self.get_attr(f, Parameters.customer_branch_ids)

        params: dict = self.params_delete_none_object(params)

        return params
    
class UpdateCustomer(Action):
    class Parameters(BaseParameters):
        customer_name: Optional[List[CustomerName]]
        customer_phone: Optional[List[CustomerPhone]]
        customer_gender: Optional[List[CustomerGender]]
        customer_is_study: Optional[List[CustomerIsStudy]]
        customer_company_id: Optional[List[CustomerCompanyId]]
        customer_dob: Optional[List[CustomerDob]]
        customer_balance: Optional[List[CustomerBalance]]
        customer_email: Optional[List[CustomerEmail]]
        customer_web: Optional[List[CustomerWeb]]
        customer_legal_name: Optional[List[CustomerLegalName]]
        customer_legal_type: Optional[List[CustomerLegalType]]

    path: str = Path.update_customer
    api: Literal[Api.url_api_v2]
    resource: Literal[Resource.customer]
    operation: Literal[Operation.update_customer]
    parameters: Optional[Parameters]
    id_customer: str

    def get_request_params(self) -> dict:
        params = {}
        f = self.parameters
        
        if f:
            params["name"] = self.get_attr(f, Parameters.customer_name)
            params["is_study"] = self.get_attr(f, Parameters.customer_is_study)
            params["legal_type"] = self.get_attr(f, Parameters.customer_legal_type)
            params["phone"] = self.get_attr(f, Parameters.customer_phone)
            params["balance"] = self.get_attr(f, Parameters.customer_balance)
            params["legal_name"] = self.get_attr(f, Parameters.customer_legal_name)
            params["web"] = self.get_attr(f, Parameters.customer_web)
            params["email"] = self.get_attr(f, Parameters.customer_email)
            params["dob"] = self.get_attr(f, Parameters.customer_dob)
            params["company_id"] = self.get_attr(f, Parameters.customer_company_id)
            params["gender"] = self.get_attr(f, Parameters.customer_gender)

        params: dict = self.params_delete_none_object(params)

        return params
