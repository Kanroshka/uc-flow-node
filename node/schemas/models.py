from datetime import datetime

from pydantic import BaseModel


# DEAL

class DealAmount(BaseModel):
    deal_amount: int


class DealCloseDate(BaseModel):
    deal_close_date: datetime


class DealName(BaseModel):
    deal_name: str


class DealPipeline(BaseModel):
    deal_pipeline: str


class DealStage(BaseModel):
    deal_stage: str


# CONTACT

class ContactEmail(BaseModel):
    contact_email: str


class ContactFirstname(BaseModel):
    contact_firstname: str


class ContactLastname(BaseModel):
    contact_lastname: str


class ContactPhone(BaseModel):
    contact_phone: int


class ContactCompany(BaseModel):
    contact_company: str


class ContactWebsite(BaseModel):
    contact_website: str


class ContactLifecyclestage(BaseModel):
    contact_lifecyclestage: str

# AS. WITH OBJECT

class AssociationImmediatelyToId(BaseModel): 
    association_immediately_to_id: int


class AssociationImmediatelyCategory(BaseModel): 
    association_immediately_category: str


class AssociationImmediatelyTypeId(BaseModel):
    association_immediately_type_id: int

# AS.SEPARATELY

class AssociationsFirst(BaseModel):
    associations_first: str


class AssociationsSecond(BaseModel):
    associations_second: str


class AssociationSeparatelyFromId(BaseModel):
    association_separately_from_id: dict


class AssociationSeparatelyToId(BaseModel):
    association_separately_to_id: dict


class AssociationSeparatelyType(BaseModel):
    association_separately_type: str

