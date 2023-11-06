from enum import Enum

from uc_http_requester.requester import Request


BASE_URL_API = 'https://api.hubapi.com/'
BASE_URL_API_v3 = 'https://api.hubapi.com/crm/v3/'


class Resource(str, Enum):
    check_authorization = 'check_authorization'
    deal = 'deal'
    contact = 'contact'
    association = 'association'


class Operation(str, Enum):
    create_deal = 'create_deal'
    update_deal = 'update_deal'
    delate_deal = 'delete_deal'
    create_contact = 'create_contact'
    update_contact = 'update_contact'
    delate_contact = 'delete_contact'
    create_association = 'create_association'
    read_deal = 'read_deal'


class Path(str, Enum):
    check_authorization = 'oauth/v2/private-apps/get/access-token-info'
    create_deal = 'objects/deals'
    update_deal = 'objects/deals/'
    delate_deal = 'objects/deals/'
    read_deal = 'objects/deals/'
    create_contact = 'objects/contacts'
    update_contact = 'objects/contacts/'
    delate_contact = 'objects/contacts/'
    create_association = 'associations/'
    create_association_end = '/batch/create'


class JsonMethods(str):
    check_authorization = Request.Method.post
    create_contact = Request.Method.post
    create_deal = Request.Method.post
    update_deal = Request.Method.patch
    update_contact = Request.Method.patch
    delate_deal = Request.Method.delete
    delate_contact = Request.Method.delete
    create_association = Request.Method.post
    read_deal = Request.Method.get


class Properties(str, Enum):
    #  CREATE | UPDATE DEAL
    deal_amount = 'deal_amount'
    deal_close_date = 'deal_close_date'
    deal_name = 'deal_name'
    deal_pipeline = 'deal_pipeline'
    deal_stage = 'deal_stage'

    # CREATE | UPDATE CONTACT
    contact_email = 'contact_email'
    contact_firstname = 'contact_firstname'
    contact_lastname = 'contact_lastname'
    contact_phone = 'contact_phone'
    contact_company = 'contact_company'
    contact_website = 'contact_website'
    contact_lifecyclestage = 'contact_lifecyclestage'


class Association(str, Enum):
    # CREATE AS. SEPARATELY
    association_separately_from_id = 'association_separately_from_id'
    association_separately_to_id = 'association_separately_to_id'
    association_separately_type = 'association_separately_type'
    associations_first = 'associations_first'
    associations_second = 'associations_second'

    # CREATE AS. WITH OTHER OBJECT
    association_immediately_to_id = 'association_immediately_to_id'
    association_immediately_category = 'association_immediately_category'
    association_immediately_type_id = 'association_immediately_type_id'


class ContactLifecyclestage(str, Enum):
    subscriber = 'subscriber'
    lead = 'lead'
    marketingqualifiedlead = 'marketingqualifiedlead'
    salesqualifiedlead = 'salesqualifiedlead'
    opportunity = 'opportunity'
    customer = 'customer'
    evangelist = 'evangelist'
    other = 'other'


class DealStage(str, Enum):
    appointmentscheduled = 'appointmentscheduled'
    qualifiedtobuy = 'qualifiedtobuy'
    presentationscheduled = 'presentationscheduled'
    decisionmakerboughtin = 'decisionmakerboughtin'
    contractsent = 'contractsent'
    closedwon = 'closedwon'
    closedlost = 'closedlost'


class ObjectsAssociationsAPI(str, Enum):
    contacts = 'Contacts'
    deals = 'Deals'


class AssociationsType(str, Enum):
    deal_to_contact = 'deal_to_contact'
    contact_to_deal = 'contact_to_deal'
    