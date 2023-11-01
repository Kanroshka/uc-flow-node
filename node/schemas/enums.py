from enum import Enum


URL_API_V2 = '/v2api/'


class Api(str, Enum):
    url_api_v2 = 'url_api_v2'

class Resource(str, Enum):
    customer = 'customer'
    authorization = 'authorization'

class Operation(str, Enum):
    get_customers_filtered_and_paging  = 'get_customers_filtered_and_paging'
    create_customer = 'create_customer'
    update_customer = 'update_customer'
    authorization = 'authorization'

class Path(str, Enum):
    authorization = 'auth/login'
    get_customers_filtered_and_paging = 'location/index'
    create_customer = 'location/create'
    update_customer = 'location/update?id='

class Parameters(str, Enum):
    customer_id = 'customer_id'
    customer_is_study = 'customer_is_study'
    customer_study_status_id = 'customer_study_status_id'
    customer_name = 'customer_name'
    customer_branch_ids = 'customer_branch_ids'
    customer_teacher_ids = 'customer_teacher_ids'
    customer_lead_status_id = 'customer_lead_status_id'
    customer_lead_source_id = 'customer_lead_source_id'
    customer_assigned_id = 'customer_assigned_id'
    customer_dob = 'customer_dob'
    customer_gender = 'customer_gender'
    customer_age_from = 'customer_age_from'
    customer_age_to = 'customer_age_to'
    customer_phone = 'customer_phone'
    customer_email = 'customer_email'
    customer_web = 'customer_web'
    customer_addr = 'customer_addr'
    customer_legal_type = 'customer_legal_type'
    customer_legal_name = 'customer_legal_name'
    customer_company_id = 'customer_company_id'
    customer_paid_lesson_count = 'customer_paid_lesson_count'
    customer_lesson_count_from = 'customer_lesson_count_from'
    customer_lesson_count_to = 'customer_lesson_count_to'
    customer_balance = 'customer_balance'
    customer_balance_contract_from = 'customer_balance_contract_from'
    customer_balance_contract_to = 'customer_balance_contract_to'
    customer_balance_bonus_from = 'customer_balance_bonus_from'
    customer_balance_bonus_to = 'customer_balance_bonus_to'
    customer_removed = 'customer_removed'
    customer_removed_from = 'customer_removed_from'
    customer_removed_to = 'customer_removed_to'
    customer_level_id = 'customer_level_id'
    customer_employee_id = 'customer_employee_id'
    customer_color = 'customer_color'
    customer_note = 'customer_note'
    customer_date_from = 'customer_date_from'
    customer_date_to = 'customer_date_to'
    customer_next_lesson_date_from = 'customer_next_lesson_date_from'
    customer_next_lesson_date_to = 'customer_next_lesson_date_to'
    customer_tariff_till_from = 'customer_tariff_till_from'
    customer_tariff_till_to = 'customer_tariff_till_to'
    customer_reject_id = 'customer_reject_id'
    customer_comment = 'customer_comment'
    customer_dob_from = 'customer_dob_from'
    customer_dob_to = 'customer_dob_to'
    customer_with_groups_true = 'customer_withGroups:true'
